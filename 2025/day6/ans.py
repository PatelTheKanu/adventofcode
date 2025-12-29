
from string import digits


def part1():
    numbers = []
    f = open('input.txt')
    lines = f.readlines()
    for i in range(len(lines) - 1):
        line = lines[i] 
        numbers.append([])
        for num in line.split(' '):
            if num and num != '\n':
                numbers[i].append(int(num))
    ops = []
    results = []
    for op in lines[-1].split(' '):
        if op and  op != '' and op != '\n':
            ops.append(op)
            results.append('')

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            op = ops[j]
            num = numbers[i][j]
            if results[j] == '':
                results[j] = num
                continue
            if op == '*':
                results[j] *= num
            elif op  == '+':
                results[j] += num
    print(results)
    print(sum(results))

def part2():
    f = open('input.txt')
    lines = f.readlines()

    digits = []
    for i in range(len(lines) - 1):
        digits.append([])
        line = lines[i]
        for c in line:
            digits[i].append(c)
    ops = []
    results = []
    num_operands = []

    ops = []
    results = []
    for op in lines[-1].split(' '):
        if op and  op != '' and op != '\n':
            ops.append(op)
            results.append([])

    curr_equation = 0
    for col in range(len(lines[0])):
        is_empty_col = True
        results[curr_equation].append('')
        for row in range(len(lines) - 1):
            d = digits[row][col]
            if d != ' ' and d != '' and d != '\n':
                print(d)
                results[curr_equation][-1] += d
                is_empty_col = False
        if is_empty_col:
            results[curr_equation] = results[curr_equation][:-1]
            curr_equation += 1
    print(results)
    print(ops)
    fin_results = ['' for i in range(len(results))]
    for i in range(len(ops)):
        op = ops[i]
        print(op)
        for j in range(len(results[i])):
            num = results[i][j]
            print(num)
            if op == '*':
                if fin_results[i] == '':
                    fin_results[i] = 1
                fin_results[i] *= int(num)
            elif op  == '+':
                if fin_results[i] == '':
                    fin_results[i] = 0
                fin_results[i] += int(num)
    print(fin_results)
    print(sum(fin_results))

def main():
    part2()

if __name__ == '__main__':
    main()