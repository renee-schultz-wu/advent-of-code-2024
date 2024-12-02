with open("input.txt", "r") as file:
    alist = [line.strip() for line in file]

def p1_helper(nums):
    if len(nums) == 1: return True

    if int(nums[1]) > int(nums[0]): lb, rb = 1, 3
    else: lb, rb = -3, -1

    prev = int(nums[0])
    for num in nums[1:]:
        num = int(num)
        if lb <= num - prev <= rb:
            prev = num
        else:
            return False
    return True

def p1(nums):
    res = 0
    for l in nums:
        if p1_helper(l.split(" ")): res += 1
    return res

def p2_helper(nums):
    for i in range(len(nums)):
        newnums = nums[:]
        newnums.pop(i)
        if p1_helper(newnums): 
            return True
    return False

def p2(nums):
    res = 0
    for l in nums:
        if p2_helper(l.split(" ")): res += 1
    return res

test = [
"7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"
]

print("answer to part 1 is: ",p1(alist))
print("answer to part 2 is: ",p2(alist))
