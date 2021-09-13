idstr = input("請輸入身份證字號：").upper()
code1 = ord(idstr[0])
cmap = [10, 11, 12, 13, 14, 15, 16, 17,
        34, 18, 19, 20, 21, 22, 35, 23, 24,
        25, 26, 27, 28, 29, 32, 30, 31, 33]
num1 = cmap[code1 - 65]
newid = str(num1) + idstr[1:]
print("重新編碼後的身分證字號為：", newid)

weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
checksum = 0
for i in range(11):
    checksum += weight[i] * int(newid[i])
remainder = checksum % 10
print("依據checksum rule，餘數為", remainder)
if remainder == 0:
    print("此為合法身分證字號")
else:
    print("此為非法身分證字號")
