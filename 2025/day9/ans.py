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

def main():
    f = open('input.txt')
    coords = getCoords(f.readlines())
    h = getAreaHeap(coords)
    print(heappop(h))

if __name__ == '__main__':
    main()