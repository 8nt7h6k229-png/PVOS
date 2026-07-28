import math

def point_in_polygon(point, polygon):
    x, y = point
    inside = False
    for i, a in enumerate(polygon):
        b = polygon[(i + 1) % len(polygon)]
        if ((a[1] > y) != (b[1] > y)):
            cross_x = (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]
            if x < cross_x:
                inside = not inside
    return inside

def to_local(p, deg):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return (p[0]*c + p[1]*s, -p[0]*s + p[1]*c)

poly = [to_local(p, 15) for p in [(0,0),(20000,0),(20000,10000),(0,10000)]]
xs, ys = zip(*poly)
minx,miny,maxx,maxy=min(xs),min(ys),max(xs),max(ys)
w,h,gx,gy,m=1133,1907,10,20,300
count=0
y=miny+m
while y+h <= maxy-m+1e-9:
    x=minx+m
    while x+w <= maxx-m+1e-9:
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
        if all(point_in_polygon(p,poly) for p in corners):
            count+=1
        x += w+gx
    y += h+gy
print(count)
