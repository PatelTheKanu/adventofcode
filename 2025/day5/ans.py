
def isFresh(fresh_ranges, id):
    for fresh_range in fresh_ranges:
        if id >= fresh_range[0] and id <= fresh_range[1]:
            return True
    return False

def main():
    f = open('input.txt')
    fresh_ranges = []
    availble_ids = set()

    # TODO make cmd line arg
    part1 = False
    line = f.readline()
    while line and line != '\n':
        frange = line.split('-')
        fresh_ranges.append((int(frange[0]), int(frange[1][:-1])))
        line = f.readline()
    if part1:
        line = f.readline()
        while line:
            availble_ids.add(int(line))
            line = f.readline()
    
        numFresh = 0
        for id in availble_ids:
            numFresh += isFresh(fresh_ranges, id)
        print(numFresh)
    else:
        mins = sorted([f[0] for f in fresh_ranges])
        maxes = sorted([f[1] for f in fresh_ranges])
        total_fresh_ids = maxes[-1] - mins[0] + 1
        mins.pop(0)
        maxes.pop()
        while maxes and mins:
            if maxes[0] < mins[0]:
                total_fresh_ids -= (mins[0] - maxes[0] - 1)
            maxes.pop(0)
            mins.pop(0)

        #for id in range(min(mins), max(maxes)+1):
        #seen = set()
        #for f in fresh_ranges:
        #    if f[0] not in seen and f[1] + 1 not in seen:
        #        total_fresh_ids += f[1] - f[0] + 1
        #        seen.update(range(f[0], f[1] + 1))
        #    else:
        #        mid = f[0]
        #        last_mid = mid
        #        while mid in seen:
        #            last_mid = mid
        #            mid = f[1] + mid//2   

        #        for id in range(last_mid, f[1] + 1):
        #            if id not in seen:
        #                total_fresh_ids += 1
        #                seen.add(id)
        print(total_fresh_ids)


if __name__ == '__main__':
    main()