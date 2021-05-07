key = input()
sum = 0
for x in range(len(key)):
    print('ASCII code for {} is {}'.format(key[x],ord(key[x])))
    sum += ord(key[x])
print(sum)