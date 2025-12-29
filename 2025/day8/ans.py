import math
from itertools import combinations
from heapq import heappush, heappop

def getCoords(lines):
    coords = []
    for line in lines:
        x,y,z = line.split(',')
        coords.append((int(x), int(y), int(z)))
    return coords

def getEuclidDistance(p,q):
    return math.sqrt(math.pow(p[0] - q[0], 2) + math.pow(p[1] - q[1], 2) + math.pow(p[2] - q[2], 2))

def merge(circuits, num_connections, seen_circuits, p, q):
    new_set = {p,q}
    for key in seen_circuits:
        new_set.update(circuits[key])
        del circuits[key]
    circuits[num_connections] = new_set

def getThreeLargestCircuitSizes(distances):
    num_connections = 0
    circuits = {}
    while num_connections < 1000:
        distance, p, q = heappop(distances)
        seen_circuits = set()
        for key in circuits:
            c = circuits[key]
            if (p in c):
                seen_circuits.add(key)
            if (q in c):
                seen_circuits.add(key)

        if len(seen_circuits) == 0:
            circuits[num_connections] = {p, q}
        else:
            merge(circuits, num_connections, seen_circuits, p, q)
        num_connections += 1

    circuit_sizes = sorted([len(c) for c in circuits.values()], reverse=True)

    print(circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])

def getLastJunctionBoxes(num_circuits, distances):
    p,q = None, None
    num_connections = 0
    circuits = {}
    while not (len(circuits) == 1 and len(list(circuits.values())[0]) == num_circuits):
        distance, p, q = heappop(distances)
        seen_circuits = set()
        for key in circuits:
            c = circuits[key]
            if (p in c):
                seen_circuits.add(key)
            if (q in c):
                seen_circuits.add(key)

        if len(seen_circuits) == 0:
            circuits[num_connections] = {p, q}
        else:
            merge(circuits, num_connections, seen_circuits, p, q)
        num_connections += 1
    print(circuits) 
    print(p)
    print(q)
    print(p[0] * q[0])

def main():
    f = open('input.txt')
    lines = f.readlines()
    coords = getCoords(lines)
    distances = []
    pqs = combinations(coords, 2)
    for pq in pqs:
        p, q = pq[0], pq[1]
        distance = getEuclidDistance(p, q)
        heappush(distances, (distance, p, q))
    #getThreeLargestCircuitSizes(distances)
    num_circuits = len(coords)
    getLastJunctionBoxes(num_circuits, distances)


if __name__ == '__main__':
    main()