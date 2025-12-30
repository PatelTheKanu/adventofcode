import math
from heapq import heappush, heappop

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

def main():
    f = open('example.txt')
    coords = getCoords(f.readlines())
    h = getAreaHeap(coords)
    print(heappop(h))
    h = getRestrictedAreaHeap(coords)
    print(heappop(h))

if __name__ == '__main__':
    main()