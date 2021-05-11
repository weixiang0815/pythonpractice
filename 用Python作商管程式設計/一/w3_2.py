a = int(input())
ans = 1000 - a
x = ans // 500
y = (ans - x * 500) // 100
z = (ans - x * 500 - y * 100) // 50
u = (ans - x * 500 - y * 100 - z * 50) // 10
v = (ans - x * 500 - y * 100 - z * 50 - u * 10) // 5
n = ans % 5
value = [500, 100, 50, 10, 5, 1]
num = [x, y, z, u, v, n]
isValid = [False] * 6
for i in range(6):
    if num[i] != 0:
        isValid[i] = True
ans = []
m = 0
for i in range(6):
    if isValid[i] is True:
        ans += [str(value[i]) + ", " + str(num[i])]
        m += 1
answer = ""
for i in range(m):
    answer += ans[i]
    if i != m - 1:
        answer += "; "
print(answer)
