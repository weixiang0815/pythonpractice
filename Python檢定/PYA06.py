sum = 0
for x in range(5):
    key = input()
    if key == 'J':
        key = '11'
    elif key == 'Q':
        key = '12'
    elif key == 'K':
        key = '13'
    elif key == 'A':
        key = '1'
    sum += int(key)
print(sum)