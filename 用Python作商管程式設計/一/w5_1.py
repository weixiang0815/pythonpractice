c = int(input())  # 單位進貨成本
r = int(input())  # 單位零售價格
N = int(input())  # 需求的可能個數
s = int(input())  # 殘值
probability = [0.0] * (N + 1)  # 賣出零份、一份直到 N 份報紙的機率分布
for i in range(N + 1):
    probability[i] = float(input())

expProfit = [0.0] * (N + 1)  # 賣出 i 份報紙的預期利潤分布
bestExpProfit = 0
for i in range(N + 1):
    q = i  # 訂貨量
    leftProbabilitySum = 1  # 剩餘機率分布加總
    expectedProfit = 0
    for j in range(q + 1):
        # 預期收益 = 賣出 j 份 * 零售價 - 訂貨量 * 單位進貨成本 + 賣剩份數 * 殘值
        revenue = j * r - q * c + (q - j) * s
        if j == q:
            expectedProfit += revenue * leftProbabilitySum
        else:
            expectedProfit += revenue * probability[j]
            leftProbabilitySum -= probability[j]
    expProfit[i] = expectedProfit
    if i > 0 and expProfit[i] < expProfit[i-1]:
        bestExpProfit = expProfit[i-1]
        break

print(expProfit.index(bestExpProfit), int(bestExpProfit))
