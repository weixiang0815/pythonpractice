a, b = int(input()), int(input())
if not a % 2 == 0:
    a += 1
sum = a
while a<b:
    sum+=a+2
    a+=2
print(sum)