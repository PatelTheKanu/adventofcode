from heapq import heappush, heappop, heapify

def findLargestJoltage(line):
    h = []
    for i in range(len(line[:-1])):
        heappush(h, (-int(line[i]),i))
    if not h or len(h) < 2:
        return 0
    first = heappop(h)
    second = heappop(h)
    if first[1] < second[1]:
        out =  int(f'{abs(first[0])}{abs(second[0])}')
    else:
        out = int(f'{abs(second[0])}{abs(first[0])}')
        if first[1] > 1:
            out =  max(out, findLargestJoltage(line[first[1]:]))

    return out

def part1(lines):
    tot = 0
    for line in lines:
        tot += findLargestJoltage(line)
    print(tot)

def findLargestJoltageArb(line, joltLen):
    if joltLen == 0:
        return 0
    h = []
    numC = len(line[:-1])
    for i in range(numC):
        heappush(h, (-int(line[i]),i))
    while h:
        largestDigit,ldIndex = heappop(h)
        if ldIndex + joltLen - 1 <= numC:
            return int(f'{abs(largestDigit) + findLargestJoltageArb(line[ldIndex+1:], joltLen - 1)}')
    return 0
    
def part2(lines):
    tot = 0
    for line in lines:
        tot += findLargestJoltageArb(line, 12)
    print(tot)

def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()
    part1(lines)
    part2(lines)
    

if __name__ == '__main__':
    main()