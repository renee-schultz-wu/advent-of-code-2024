import re

with open("input.txt", "r") as file:
    alist = [line.strip() for line in file]

txt = ""
for a in alist: txt += a

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def helper(i):
    temp = re.findall(r'[0-9]{1,3}', i)
    return int(temp[0]) * int(temp[1])


def p1(txt):
    x = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', txt)
    res = 0
    for i in x:
        res += helper(i)
    print("answer to p1",res)

p1(txt)

test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def p2(txt):
    ind = True
    res = 0
    for x in re.finditer(r'mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\)', txt):
        if x.group() == "don't()":
            ind = False
        elif x.group() == "do()":
            ind = True
        elif ind:
            res += helper(x.group())
        else:
            pass

    print("answer to p2",res)

p2(txt)

    
