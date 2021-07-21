n = []
while True:
    key = input()
    n+=[int(key)]
    if key == '9999':
        break
n.sort()
print(n[0])