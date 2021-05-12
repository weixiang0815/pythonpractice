cost = int(input())  # 單位進貨成本
retailPrice = int(input())  # 單位零售價格
NumberOfDemand = int(input())  # 需求的可能個數
quantityOfOrder = int(input())  # 訂貨量
probability = [0.0] * (NumberOfDemand + 1)  # 賣出零份、一份直到 N 份報紙的機率分布
for i in range(NumberOfDemand + 1):
    probability[i] = float(input())

expectedProfit = 0  # 預期利潤
leftProbabilitySum = 1  # 剩餘機率分布加總
for i in range(quantityOfOrder + 1):
    expectedRevenue = i * retailPrice - quantityOfOrder * cost  # 期望收入 = 需求個數*零售價 - 訂貨量*單位成本
    if i != quantityOfOrder:
        expectedProfit += expectedRevenue * probability[i]  # 期望利潤 = 期望收入*賣出該i份報紙的機率
        leftProbabilitySum -= probability[i]
    else:
        expectedProfit += expectedRevenue * leftProbabilitySum

print(int(expectedProfit))
