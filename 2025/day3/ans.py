from heapq import heappush, heappop, heapify

def findLargestJoltage(line):
    print(f'line is {line[:-1]}')
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
        print('SWAP')
        out = int(f'{abs(second[0])}{abs(first[0])}')
        if first[1] > 1:
            out =  max(out, findLargestJoltage(line[first[1]:]))

    print(out)
    return out

def part1(lines):
    tot = 0
    for line in lines:
        tot += findLargestJoltage(line)
    print(tot)

def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()
    part1(lines)
    

if __name__ == '__main__':
    main()