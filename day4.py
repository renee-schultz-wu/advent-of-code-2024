test = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]


with open("input.txt", "r") as file:
    alist = [line.strip() for line in file]

def count_helper(s):
    index = 0
    res = 0
    while index < len(s):
        index = s.find("XMAS", index)
        if index == -1:
            break
        res += 1
        index += 1
    return res

def diagonal_helper(grid):
    m, n = len(grid), len(grid[0])
    res = []
    for i in range(n):
        rl, rr = [], []
        l, r = 0, 0
        for j in range(m):
            if i - l >= 0:
                rl.append(grid[j][i-l])
                l += 1
            if i + r < n:
                rr.append(grid[j][i+r])
                r += 1
        res.append(rr)
        res.append(rl)
    for j in range(1, m):
        l = []
        r = 0
        for i in range(n):
            if j + r < m:
                l.append(grid[j + r][i])
                r += 1
        res.append(l)
    for j in range(1, m):
        l = []
        r = 0
        for i in range(n-1, -1, -1):
            if j + r < m:
                l.append(grid[j + r][i])
                r += 1
        res.append(l)
    return res

def p1():
    res = 0
    for a in alist:
        res += count_helper(a)
        res += count_helper(a[::-1])

    for a in zip(*alist):
        res += count_helper("".join(a))
        res += count_helper("".join(a[::-1]))

    for a in diagonal_helper(alist):
        res += count_helper("".join(a))
        res += count_helper("".join(a[::-1]))
    
    return res

def helper2(grid):
    if grid[1][1] == "A" and grid[0][0] == "M" and grid[0][2] == "M" and grid[2][0] == "S" and grid[2][2] == "S":
        return True
    if grid[1][1] == "A" and grid[0][0] == "M" and grid[2][0] == "M" and grid[0][2] == "S" and grid[2][2] == "S":
        return True
    if grid[1][1] == "A" and grid[2][0] == "M" and grid[2][2] == "M" and grid[0][0] == "S" and grid[0][2] == "S":
        return True
    if grid[1][1] == "A" and grid[0][2] == "M" and grid[2][2] == "M" and grid[0][0] == "S" and grid[2][0] == "S":
        return True
    return False

def grid(arr, y, x):
    res = []
    for j in range(3):
        row = []
        for i in range(3):
            row.append(arr[y+j][x+i])
        res.append(row)
    return res

def p2():
    m, n = len(alist), len(alist[0])
    res = 0
    for j in range(m-2):
        for i in range(n-2):
            if helper2(grid(alist,j,i)):
                res += 1
    return res

print("answer to part 1 is: ", p1())
print("answer to part 2 is: ", p2())