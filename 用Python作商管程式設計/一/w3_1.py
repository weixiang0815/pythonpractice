x1 = int(input())
x2 = int(input())
y = int(input())
if x1 < y:
    x2 += x1
    x1 = 0
else:
    x1 -= y
    x2 += y
print(x1, x2)
