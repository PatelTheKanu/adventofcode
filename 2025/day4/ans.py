

from copy import deepcopy


NUM_ALLOWED_ROLLS_IN_ADJ_POS = 3
ROLL_CHAR = '@'

def getAdjList(grid, row, col):
    rightEdge = len(grid[row].replace('\n', '')) - 1
    bottomEdge = len(grid) - 1
    adjList = []
    if row != 0:
        adjList += [(row - 1, col)]
    if col != 0:
        adjList += [(row, col - 1)]
    if row != 0 and col != 0:
        adjList += [(row - 1, col - 1)]
    if row != 0 and col != rightEdge:
        adjList += [(row - 1, col + 1)]
    if row != bottomEdge and col != 0:
        adjList += [(row + 1, col - 1)]
    if row != bottomEdge:
        adjList += [(row + 1, col)]
    if col != rightEdge:
        adjList += [(row, col + 1)]
    if row != bottomEdge and col != rightEdge:
        adjList += [(row + 1, col + 1)]
    return adjList


def isRoll(grid, row, col):
    try:
        return grid[row][col] == ROLL_CHAR
    except IndexError as e:
        print(f'On row {row} and col {col}')
        raise e

def getNumRollsInAdjPos(grid, row, col):
    adjList = getAdjList(grid, row, col)
    rolls = 0
    for adjRow, adjCol in adjList:
        if isRoll(grid, adjRow, adjCol):
            rolls += 1
    return rolls

    
def getNumAccessibleRolls(grid):
    numAccessibleRolls = 0
    rows = range(len(grid))
    for row in rows:
        cols = range(len(grid[row].replace('\n', '')))
        for col in cols:
            if isRoll(grid, row, col) and getNumRollsInAdjPos(grid, row, col) <= NUM_ALLOWED_ROLLS_IN_ADJ_POS:
                numAccessibleRolls += 1

    return numAccessibleRolls


def main():
    f = open('input.txt')
    origGrid = f.readlines()
    numAccessibleRolls = getNumAccessibleRolls(origGrid)
    print(f'accessbileRolls: {numAccessibleRolls}')



if __name__ == '__main__':
    main()