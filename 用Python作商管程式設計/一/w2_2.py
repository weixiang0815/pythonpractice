a = int(input())
ans = 1000 - a
x = ans // 500
y = (ans - x*500)//100
z = (ans - x*500 - y*100)//50
u = (ans - x*500 - y*100 - z*50)//10
v = (ans - x*500 - y*100 - z*50 - u*10)//5
n = ans % 5
print(x, y, z, u, v, n)
