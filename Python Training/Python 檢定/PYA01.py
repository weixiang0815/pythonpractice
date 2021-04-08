key = [0.0]*4
for x in range(4):
    key[x] = float(input())
print('|%7.2f%7.2f|' %(key[0], key[1]))
print('|%7.2f%7.2f|' %(key[2], key[3]))
print('|%-7.2f%-7.2f|' %(key[0], key[1]))
print('|%-7.2f%-7.2f|' %(key[2], key[3]))