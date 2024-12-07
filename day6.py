#import numpy as np

with open("input.txt", "r") as file:
    alist = [line.strip() for line in file]

test = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

def parse(alist):
    m, n = len(alist), len(alist[0])
    obs = [[False for _ in range(n)] for _ in range(m)]

    for j in range(m):
        for i in range(n):
            if alist[j][i] == ".":
                continue
            elif alist[j][i] == "#":
                obs[j][i] = True
            else:
                position = (j, i)
    return m, n, position, obs

m, n, position, obs = parse(alist)
direction = [(-1,0), (0, 1), (1, 0), (0, -1)]

def p1():
    visit = set()
    dirIndex = 0 
    y, x = position
    while y != 0 and y != m-1 and x != 0 and x != n-1:
        newY, newX = (y + direction[dirIndex][0], x + direction[dirIndex][1])
        if not obs[newY][newX]:
            y, x = newY, newX
            visit.add((y, x))
        else:
            dirIndex = (dirIndex+1)%4
            
    return len(visit)

def helper(visitDict, y, x, dirIndex):
    if (y, x) in visitDict and (dirIndex + 1) % 4 in visitDict[(y, x)]:
        return True
    dirIndex = (dirIndex+1)%4
    while y != 0 and y != m-1 and x != 0 and x != n-1:
        y, x = (y + direction[dirIndex][0], x + direction[dirIndex][1])
        if (y, x) in visitDict and dirIndex in visitDict[(y, x)]:
            return True
    return False

def loopHelper(startPosition, obs, dirIndex, visitDict):
    y, x = startPosition
    while y != 0 and y != m-1 and x != 0 and x != n-1:
        newY, newX = (y + direction[dirIndex][0], x + direction[dirIndex][1])
        if not obs[newY][newX]:
            if (newY, newX) in visitDict and dirIndex in visitDict[(newY, newX)]:
                return True
            y, x = newY, newX
            visitDict[(y, x)] = visitDict.get((y,x), []) + [dirIndex]
        else:
            dirIndex = (dirIndex+1)%4      
    return False

def p2():
    visit = set()
    visitDict = {}
    dirIndex = 0 
    y, x = position 
    visitDict[(y, x)] = [dirIndex]
    res = 0
    while y != 0 and y != m-1 and x != 0 and x != n-1:
        newObs = obs[:]
        newObs[y][x] = True
        if loopHelper((y, x), newObs, dirIndex, visitDict):
            res += 1
        newY, newX = (y + direction[dirIndex][0], x + direction[dirIndex][1])
        if obs[newY][newX]:
            dirIndex = (dirIndex+1)%4
        else:
            y, x = newY, newX
            visit.add((y, x))
            visitDict[(y, x)] = visitDict.get((y, x), []) + [dirIndex]
    return res

print("The answer to part 1 is ",p1())
print("The answer to part 2 is ",p2())
            
            


