n1 = ()
while True:
    key = int(input())
    if key == -9999:
        break
    n1 = n1 + (key, )
n2 = ()
while True:
    key = int(input())
    if key == -9999:
        break
    n2 = n2 + (key, )
n = n1[:] + n2[:]
print('Combined tuple before sorting: ', n)
a = list(n)
a.sort()
print('Combined list after sorting: ', a)
