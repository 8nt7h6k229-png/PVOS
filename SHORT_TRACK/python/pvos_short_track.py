#!/usr/bin/env python3
"""PVOS Python Short Track v0.1; preview only, never Product authority."""
from __future__ import annotations
import argparse, hashlib, json, math, subprocess, sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION="0.1.1"; EPS=1e-9; ORIENTATIONS={"WidthAlongLocalX","LengthAlongLocalX"}
class InputBlocked(Exception): pass
@dataclass(frozen=True)
class Point: x: float; y: float

def number(v:Any,p:str)->float:
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v): raise InputBlocked(f"{p} must be a finite number")
    return float(v)
def text(o:dict,k:str,p:str)->str:
    v=o.get(k)
    if not isinstance(v,str) or not v.strip(): raise InputBlocked(f"{p}.{k} is required")
    return v
def point(v:Any,p:str)->Point:
    if not isinstance(v,dict): raise InputBlocked(f"{p} must be an object")
    return Point(number(v.get("x"),p+".x"),number(v.get("y"),p+".y"))
def same(a,b): return abs(a.x-b.x)<=EPS and abs(a.y-b.y)<=EPS
def orient(a,b,c):
    z=(b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x)
    return 0 if abs(z)<=EPS else (1 if z>0 else -1)
def on(p,a,b): return orient(a,b,p)==0 and min(a.x,b.x)-EPS<=p.x<=max(a.x,b.x)+EPS and min(a.y,b.y)-EPS<=p.y<=max(a.y,b.y)+EPS
def intersects(a,b,c,d):
    o1,o2,o3,o4=orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)
    return o1*o2<0 and o3*o4<0 or o1==0 and on(c,a,b) or o2==0 and on(d,a,b) or o3==0 and on(a,c,d) or o4==0 and on(b,c,d)
def proper(a,b,c,d): return orient(a,b,c)*orient(a,b,d)<0 and orient(c,d,a)*orient(c,d,b)<0
def area(p): return sum(a.x*b.y-b.x*a.y for a,b in zip(p,p[1:]+p[:1]))/2
def simple(p):
    n=len(p)
    return not any(intersects(p[i],p[(i+1)%n],p[j],p[(j+1)%n]) for i in range(n) for j in range(i+1,n) if j!=(i+1)%n and (j+1)%n!=i)
def polygon(v:Any,p:str)->list[Point]:
    if not isinstance(v,list) or len(v)<3: raise InputBlocked(f"{p} requires at least three vertices")
    q=[point(x,f"{p}[{i}]") for i,x in enumerate(v)]
    if any(same(q[i],q[(i+1)%len(q)]) for i in range(len(q))): raise InputBlocked(f"{p} contains a zero-length edge")
    if abs(area(q))<=EPS: raise InputBlocked(f"{p} has zero enclosed area")
    if not simple(q): raise InputBlocked(f"{p} is not a simple polygon")
    return q
def inside(p,poly):
    state=False
    for a,b in zip(poly,poly[1:]+poly[:1]):
        if on(p,a,b): return True
        if (a.y>p.y)!=(b.y>p.y) and p.x<(b.x-a.x)*(p.y-a.y)/(b.y-a.y)+a.x: state=not state
    return state
def contained(subject,container):
    if any(not inside(p,container) for p in subject): return False
    for a,b in zip(subject,subject[1:]+subject[:1]):
        if any(proper(a,b,c,d) for c,d in zip(container,container[1:]+container[:1])): return False
        if not inside(Point((a.x+b.x)/2,(a.y+b.y)/2),container): return False
    return True
def local(p,o,d):
    c,s=math.cos(math.radians(d)),math.sin(math.radians(d)); x,y=p.x-o.x,p.y-o.y
    return Point(x*c+y*s,-x*s+y*c)
def global_(p,o,d):
    c,s=math.cos(math.radians(d)),math.sin(math.radians(d))
    return Point(o.x+p.x*c-p.y*s,o.y+p.x*s+p.y*c)
def coords(p): return {"x":round(p.x,6),"y":round(p.y,6)}

def partition(raw:Any,index:int)->dict:
    path=f"partitions[{index}]"
    if not isinstance(raw,dict): raise InputBlocked(f"{path} must be an object")
    pid=text(raw,"partitionId",path); boundary=polygon(raw.get("boundary"),path+".boundary"); axis=raw.get("localAxis"); mod=raw.get("module")
    if not isinstance(axis,dict): raise InputBlocked(path+".localAxis is required")
    if not isinstance(mod,dict): raise InputBlocked(path+".module is required")
    origin=point(axis.get("origin"),path+".localAxis.origin"); rotation=number(axis.get("rotationDegrees"),path+".localAxis.rotationDegrees"); orientation=text(mod,"orientation",path+".module")
    if orientation not in ORIENTATIONS: raise InputBlocked(path+".module.orientation is unsupported")
    w=number(mod.get("physicalWidthMm"),path+".module.physicalWidthMm"); h=number(mod.get("physicalLengthMm"),path+".module.physicalLengthMm"); gx=number(mod.get("gapXmm"),path+".module.gapXmm"); gy=number(mod.get("gapYmm"),path+".module.gapYmm"); margin=number(mod.get("edgeMarginMm",0),path+".module.edgeMarginMm")
    if w<=0 or h<=0 or gx<0 or gy<0 or margin<0: raise InputBlocked(path+".module dimensions must be positive and gaps/margin non-negative")
    ex,ey=(w,h) if orientation=="WidthAlongLocalX" else (h,w); lb=[local(p,origin,rotation) for p in boundary]; minx,maxx=min(p.x for p in lb)+margin,max(p.x for p in lb)-margin; miny,maxy=min(p.y for p in lb)+margin,max(p.y for p in lb)-margin
    placements=[]; candidate=0; row=0; y=miny
    while y+ey<=maxy+EPS:
        row+=1; col=0; x=minx
        while x+ex<=maxx+EPS:
            col+=1; candidate+=1; corners=[Point(x,y),Point(x+ex,y),Point(x+ex,y+ey),Point(x,y+ey)]
            if contained(corners,lb):
                n=len(placements)+1; placements.append({"placementId":f"{pid}-PNL-{n:06d}","order":n,"candidateIndex":candidate,"row":row,"column":col,"corners":[coords(global_(p,origin,rotation)) for p in corners]})
            x+=ex+gx
        y+=ey+gy
    warnings=[]
    if not placements: warnings.append({"code":"PLC_NO_PANEL_FITS","message":"No complete module fits this partition."})
    if candidate>len(placements): warnings.append({"code":"PLC_UNUSED_AREA_REMAINS","message":"At least one candidate was rejected by partition containment."})
    return {"partitionId":pid,"status":"PASS","localAxis":{"origin":coords(origin),"rotationDegrees":rotation},"module":{"physicalWidthMm":w,"physicalLengthMm":h,"orientation":orientation,"gapXmm":gx,"gapYmm":gy,"edgeMarginMm":margin},"placementCount":len(placements),"placements":placements,"warnings":warnings,"blockedReasons":[]}

def calculate(doc:Any,commit="UNKNOWN"):
    if not isinstance(doc,dict): raise InputBlocked("input root must be an object")
    case=text(doc,"caseId","input")
    if doc.get("linearUnit")!="mm": raise InputBlocked("input.linearUnit must be 'mm'")
    raw=doc.get("partitions")
    if not isinstance(raw,list) or not raw: raise InputBlocked("input.partitions requires at least one partition")
    acquisition=doc.get("inputAcquisition",{})
    if not isinstance(acquisition,dict): raise InputBlocked("input.inputAcquisition must be an object when supplied")
    source_type=acquisition.get("sourceType","OPERATOR_SUPPLIED_JSON")
    if source_type != "OPERATOR_SUPPLIED_JSON": raise InputBlocked("input.inputAcquisition.sourceType must be 'OPERATOR_SUPPLIED_JSON'")
    results=[partition(v,i) for i,v in enumerate(raw)]; ids=[v["partitionId"] for v in results]
    if len(ids)!=len(set(ids)): raise InputBlocked("partitionId values must be unique")
    digest=hashlib.sha256(json.dumps(doc,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {"schemaVersion":"pvos-python-short-track-result-v0.1","pythonStatus":"ENGINEERING PREVIEW / SHORT TRACK","csharpMainlineAuthority":"PRESERVED","caseId":case,"inputAcquisition":{"method":"EXPERIMENTAL_OPERATOR_JSON_ADAPTER","sourceType":source_type,"provenance":acquisition.get("provenance","NOT_SUPPLIED"),"deidentification":acquisition.get("deidentification","NOT_SUPPLIED"),"referenceMethod":acquisition.get("referenceMethod","NOT_SUPPLIED")},"result":"PASS","validationStatus":"PASS","partitionResults":results,"totalModuleCount":sum(v["placementCount"] for v in results),"warnings":[w for v in results for w in v["warnings"]],"blockedReasons":[],"evidence":{"toolVersion":VERSION,"sourceCommit":commit,"inputSha256":digest,"knowledgeGap":"GAP-017","ruleSources":["src/PVOS.Core/AxisTransform.cs","src/PVOS.Core/Geometry2D.cs","src/PVOS.Core/Domain.cs","src/PVOS.Layout/LayoutEngine.cs","ENGINEERING/PE-LAY-002_SPEC.md"],"authorityBoundary":"Experimental operator JSON adapter and Python preview re-expression; C# Mainline remains formal Product behavior authority."}}
def blocked(case,message,commit): return {"schemaVersion":"pvos-python-short-track-result-v0.1","pythonStatus":"ENGINEERING PREVIEW / SHORT TRACK","csharpMainlineAuthority":"PRESERVED","caseId":case,"result":"BLOCKED","validationStatus":"BLOCKED","partitionResults":[],"totalModuleCount":0,"warnings":[],"blockedReasons":[{"code":"INPUT_BLOCKED","message":message}],"evidence":{"toolVersion":VERSION,"sourceCommit":commit,"authorityBoundary":"No Product result was produced."}}
def report(r):
    lines=[f"# PVOS Python Short-Track v0.1 — {r['caseId']}","",f"- Result: **{r['result']}**",f"- Status: {r['pythonStatus']}",f"- C# Mainline authority: {r['csharpMainlineAuthority']}",f"- Total modules: **{r['totalModuleCount']}**",""]
    if "inputAcquisition" in r: lines += ["## Input acquisition","",f"- Method: {r['inputAcquisition']['method']}",f"- Provenance: {r['inputAcquisition']['provenance']}",f"- De-identification: {r['inputAcquisition']['deidentification']}",f"- Reference method: {r['inputAcquisition']['referenceMethod']}",""]
    for p in r["partitionResults"]: lines += [f"## Partition {p['partitionId']}","",f"- Placement count: **{p['placementCount']}**",f"- Local Axis rotation: {p['localAxis']['rotationDegrees']}°",f"- Orientation: {p['module']['orientation']}",f"- X/Y gap: {p['module']['gapXmm']} / {p['module']['gapYmm']} mm",""]
    if r["blockedReasons"]: lines += ["## Blocked reasons",""]+[f"- `{x['code']}` — {x['message']}" for x in r["blockedReasons"]]+[""]
    return "\n".join(lines+["## Engineering boundary","","This output is Engineering Preview evidence. It does not establish or replace formal C# PVOS Product behavior.","",f"Evidence source commit: `{r['evidence']['sourceCommit']}`",""])
def head(repo):
    try: return subprocess.run(["git","rev-parse","HEAD"],cwd=repo,check=True,capture_output=True,text=True).stdout.strip()
    except (OSError,subprocess.CalledProcessError): return "UNKNOWN"
def run(source,out,repo):
    commit=head(repo); case=source.stem
    try:
        doc=json.loads(source.read_text(encoding="utf-8")); case=doc.get("caseId",case) if isinstance(doc,dict) else case; result=calculate(doc,commit); code=0
    except (OSError,json.JSONDecodeError,InputBlocked) as e: result=blocked(case,str(e),commit); code=2
    out.mkdir(parents=True,exist_ok=True); stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"); stem=f"{case}-{stamp}"
    for name,data in [(stem+".json",json.dumps(result,indent=2,ensure_ascii=False)+"\n"),(stem+".md",report(result)),("LATEST.json",json.dumps(result,indent=2,ensure_ascii=False)+"\n"),("LATEST.md",report(result))]: (out/name).write_text(data,encoding="utf-8")
    return code,result
def main():
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path,default=Path("SHORT_TRACK_OUTPUT")); p.add_argument("--repo",type=Path,default=Path(__file__).resolve().parents[2]); a=p.parse_args(); code,r=run(a.input,a.output,a.repo); print(f"{r['result']}: case={r['caseId']} modules={r['totalModuleCount']} output={a.output.resolve()}"); return code
if __name__=="__main__": sys.exit(main())
