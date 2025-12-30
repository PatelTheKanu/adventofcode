from heapq import heappush, heappop
import matplotlib.pyplot as plt
import matplotlib.path as mpltPath
from shapely.geometry import Polygon, Point

def getArea(p,q):
    x = abs(p[0] - q[0]) + 1
    y = abs(p[1] - q[1]) + 1
    return x * y

def getCoords(lines):
    coords = []
    for line in lines:
        x,y = line.split(',')
        coords.append((int(x), int(y)))
    return coords

def getAreaHeap(coords):
    h = []
    for i in range(len(coords)):
        p = coords[i]
        for j in range(i+1, len(coords)):
            q = coords[j]
            heappush(h, (-getArea(p,q), p, q))
    return h

def getRangeOfNums(n1,n2):
    if n1 < n2:
        return range(n1, n2+1)
    return range(n2, n1+1)

def getLineCoords(p,q):
    if p[0] == q[0]:
        r = getRangeOfNums(p[1], q[1])
        return [(p[0], n) for n in r]
    elif p[1] == q[1]:
        r = getRangeOfNums(p[0], q[0])
        return [(n, p[1]) for n in r]
    else:
        return []
    
def getRestrictedCoords(coords):
    permiterCoords = []

    prevCoord = coords[-1]
    for coord in coords:
        for c in getLineCoords(prevCoord, coord):
            permiterCoords.append(c)
        prevCoord = coord

    areaCoords = set()
    for i in range(len(permiterCoords)):
        ci = permiterCoords[i]
        for j in range(i, len(permiterCoords)):
            cj = permiterCoords[j]
            for c in getLineCoords(ci, cj):
                areaCoords.add(c)

    return areaCoords.union(set(permiterCoords))

def getCorners(p, q):
    if p[0] == q[0] or p[1] == q[1]:
        return {p, q}
    return {p, q, (p[0], q[1]), (q[0], p[1])}

def coorInsideRestrictedArea(restrictedCoords, coor):
    return coor in restrictedCoords 

def getRestrictedAreaHeap(coords):
    restrictedCoords = getRestrictedCoords(coords)
    print(restrictedCoords)
    h = []
    for i in range(len(coords)):
        p = coords[i]
        for j in range(i+1, len(coords)):
            q = coords[j]
            corners = getCorners(p, q)
            if all([coorInsideRestrictedArea(restrictedCoords, c) for c in corners]):
                heappush(h, (-getArea(p,q), p, q))
    return h



def rectangle_in_polygon(rect_points, polygon):
    """
    rect_points: list of (x, y) for the 4 rectangle corners in order
    poly_points: list of (x, y) for the polygon boundary (all edge points)
    """

    # Build geometric objects
    rectangle = Polygon(rect_points)

    # --- 1. Check if every rectangle corner is inside or on boundary
    for pt in rect_points:
        p = Point(pt)
        if not (polygon.contains(p) or polygon.touches(p)):
            return False  # A corner is outside

    # --- 2. Check if any rectangle edge intersects polygon boundary
    # (this catches the cases you were missing)
    if rectangle.crosses(polygon):
        return False

    # --- 3. Final containment check: rectangle must be fully inside
    return polygon.contains(rectangle) or polygon.covers(rectangle)

def getRectCorners(p, q):
    if p[0] == q[0] or p[1] == q[1]:
        return [p, q]  # degenerate edge case
    return [
        (p[0], p[1]),
        (q[0], p[1]),
        (q[0], q[1]),
        (p[0], q[1])
    ]

def main():
    f = open('input.txt')
    coords = getCoords(f.readlines())
    #path = mpltPath.Path(coords)
    h = getAreaHeap(coords)
    found = False
    area, p, q = heappop(h)
    corners = getRectCorners(p, q)


    polygon = Polygon(coords + [coords[0]])
    while len(corners) == 4 and not rectangle_in_polygon(corners, polygon):
        area, p, q = heappop(h)
        corners = getRectCorners(p, q)
        #found = True
        #for c in corners:
        #    if c not in coords and not path.contains_point(c):
        #        found = False
        #        break
        #if found:
        #    print(f'{area}, {corners}')
        #else:
        #    area, p, q = heappop(h)
        #    corners = getCorners(p, q)
    print(f'{area}, {corners}')
    plt.figure()
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    plt.plot(xs, ys, 's', color='red')
    plt.fill(xs, ys, color='skyblue')
    xs = [c[0] for c in corners]
    ys = [c[1] for c in corners]
    plt.plot(xs, ys, '*', color='yellow')
    plt.fill(xs, ys, color='green')
    plt.show()

    
        
if __name__ == '__main__':
    main()