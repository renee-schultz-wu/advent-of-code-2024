import math

with open("input.txt", "r") as file:
    alist = [line.strip() for line in file]

d = {}
for i in range(alist.index("")):
    temp = alist[i].split("|")
    d[(int(temp[0]))] = d.get((int(temp[0])), [])
    d[(int(temp[0]))].append(int(temp[1]))

def helper(arr):    
    impossible = []
    for a in arr[::-1]:
        if a in impossible:
            return 0
        impossible.extend(d[a])
    return arr[math.ceil(len(arr)//2)]

def p1():
    res = 0
    for l in range(alist.index("")+1,len(alist)):
        temp = alist[l].split(",")
        arr = [int(a) for a in temp]
        res += helper(arr)
    return res

def helper2(arr):    
    impossible = []
    for a in arr[::-1]:
        if a in impossible:
            return False
        impossible.extend(d[a])
    return True

def helper3(arr):
    for a in arr:
        temp = [l for l in d[a] if l in arr]
        if len(temp) == len(arr)//2:
            return a
    return 0

def p2():
    res = 0
    for l in range(alist.index("")+1,len(alist)):
        temp = alist[l].split(",")
        arr = [int(a) for a in temp]
        if not helper2(arr):
            res += helper3(arr)
    return res

print("answer to part 1 is: ", p1())
print("answer to part 2 is: ", p2())

