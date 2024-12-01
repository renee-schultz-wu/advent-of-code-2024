from collections import Counter 

with open("input.txt", "r") as file:
    alist = [line.strip() for line in file]

l = [x.split("   ") for x in alist]
a = [int(x[0]) for x in l]
b = [int(x[1]) for x in l]

a.sort()
b.sort()

p1 = sum([abs(x-y) for x, y in zip(a,b)])
print(p1)

    
c = Counter(b)
p2 = 0
for num in a:
    p2 += c.get(num, 0) * num

print(p2)