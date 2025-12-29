
def dfs(lines, linenumber, index, seen):
    if linenumber >= len(lines) or index >= len(lines[linenumber]):
        return 0
    
    if lines[linenumber][index] == '^':
        output = 1
        if (linenumber + 1, index + 1) not in seen:
            seen.add((linenumber + 1, index + 1))
            output += dfs(lines, linenumber + 1, index + 1, seen)
        if (linenumber + 1, index - 1) not in seen:
            seen.add((linenumber + 1, index - 1))
            output += dfs(lines, linenumber + 1, index - 1, seen)
        return output  
    if (linenumber + 1, index) not in seen:
        seen.add((linenumber + 1, index))
        return dfs(lines, linenumber + 1, index, seen)
    return 0

def timelines(lines, linenumber, index):
    if linenumber >= len(lines) or index >= len(lines[linenumber]):
        return 0
    
    if lines[linenumber][index] == '^':
        return 1 + timelines(lines, linenumber + 1, index + 1) + timelines(lines, linenumber + 1, index - 1)

    return timelines(lines, linenumber + 1, index)

def main():
    f = open('input.txt')
    lines = f.readlines()
    index = 0
    for c in lines[0]:
        if c == 'S':
            break
        index += 1
    #seen = set()
    #print(dfs(lines, 1, index, seen))
    print(1 + timelines(lines, 1, index))

if __name__ == '__main__':
    main()