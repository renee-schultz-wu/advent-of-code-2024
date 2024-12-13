
with open("input.txt", "r") as file:
    alist = [line.strip() for line in file]

test = [
    'RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE'
]

m, n = len(alist), len(alist[0])

visited = set()

def helper(y, x, l):
    if (y, x) in visited:
        return 0, 0
    if y >= m or x >= n or x < 0 or y < 0:
        return 0, 0
    border = 4
    area = 1
    visited.add((y, x))
    if y > 0 and alist[y - 1][x] == l:
        tempb, tempa = helper(y-1, x, l)
        border += tempb - 1
        area += tempa
    if x > 0 and alist[y][x - 1] == l:
        tempb, tempa = helper(y, x - 1, l)
        border += tempb - 1
        area += tempa
    if y < m - 1 and alist[y + 1][x] == l:
        tempb, tempa = helper(y + 1, x, l)
        border += tempb - 1
        area += tempa
    if x < n - 1 and alist[y][x + 1] == l:
        tempb, tempa = helper(y, x + 1, l)
        border += tempb - 1
        area += tempa
    return border, area

res = 0
for j in range(m):
    for i in range(n):
        b, a = helper(j, i, alist[j][i])
        res += b * a
print("result to part 1 is ", res)