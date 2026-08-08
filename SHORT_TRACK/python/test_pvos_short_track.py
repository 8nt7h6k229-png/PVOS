import copy,json,tempfile,unittest
from pathlib import Path
import pvos_short_track as track
def fixture(): return {"caseId":"TEST-ONLY-NOT-A-REAL-CASE","linearUnit":"mm","partitions":[{"partitionId":"P1","boundary":[{"x":0,"y":0},{"x":4000,"y":0},{"x":4000,"y":3000},{"x":0,"y":3000}],"localAxis":{"origin":{"x":0,"y":0},"rotationDegrees":0},"module":{"physicalWidthMm":1000,"physicalLengthMm":1500,"orientation":"WidthAlongLocalX","gapXmm":100,"gapYmm":100,"edgeMarginMm":0}},{"partitionId":"P2","boundary":[{"x":10000,"y":0},{"x":13000,"y":3000},{"x":11500,"y":4500},{"x":8500,"y":1500}],"localAxis":{"origin":{"x":10000,"y":0},"rotationDegrees":45},"module":{"physicalWidthMm":1000,"physicalLengthMm":1500,"orientation":"LengthAlongLocalX","gapXmm":25,"gapYmm":10,"edgeMarginMm":0}}]}
class Tests(unittest.TestCase):
 def test_multi_partition_and_repeatability(self):
  a=track.calculate(fixture(),"a"*40); self.assertEqual(a,track.calculate(fixture(),"a"*40)); self.assertEqual(["P1","P2"],[p["partitionId"] for p in a["partitionResults"]]); self.assertGreater(a["totalModuleCount"],0)
 def test_axis_orientation_and_gaps(self):
  a=fixture(); b=copy.deepcopy(a); b["partitions"][0]["module"].update(orientation="LengthAlongLocalX",gapXmm=600); self.assertNotEqual(track.calculate(a)["partitionResults"][0]["placements"],track.calculate(b)["partitionResults"][0]["placements"]); self.assertEqual(45,track.calculate(a)["partitionResults"][1]["localAxis"]["rotationDegrees"])
 def test_missing_field(self):
  a=fixture(); del a["partitions"][0]["localAxis"]
  with self.assertRaisesRegex(track.InputBlocked,"localAxis is required"): track.calculate(a)
 def test_bad_geometry(self):
  a=fixture(); a["partitions"][0]["boundary"]=[{"x":0,"y":0},{"x":2,"y":2},{"x":0,"y":2},{"x":2,"y":0}]
  with self.assertRaises(track.InputBlocked): track.calculate(a)
 def test_result_serialization_and_report(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d); s=r/"input.json"; s.write_text(json.dumps(fixture()),encoding="utf-8"); code,result=track.run(s,r/"out",r); self.assertEqual(0,code); self.assertEqual(result,json.loads((r/"out/LATEST.json").read_text())); self.assertIn("ENGINEERING PREVIEW",(r/"out/LATEST.md").read_text())
if __name__=="__main__": unittest.main()
