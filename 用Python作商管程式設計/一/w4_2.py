cost = int(input())  # 單位進貨成本
retailPrice = int(input())  # 單位零售價格
NumberOfDemand = int(input())  # 需求的可能個數
probability = [0.0] * (NumberOfDemand + 1)  # 賣出零份、一份直到 N 份報紙的機率分布
for i in range(NumberOfDemand + 1):
    probability[i] = float(input())

expectedProfit = [0.0] * (NumberOfDemand + 1)  # 賣j份報紙的預期利潤分布
bestquantityOfOrder = 0
for j in range(NumberOfDemand + 1):
    leftProbabilitySum = 1  # 剩餘機率分布加總
    quantityOfOrder = j  # 訂貨量
    bestquantityOfOrder = quantityOfOrder
    for i in range(quantityOfOrder + 1):
        expectedRevenue = i * retailPrice - quantityOfOrder * cost  # 期望收入 = 需求個數*零售價 - 訂貨量*單位成本
        if i != quantityOfOrder:
            expectedProfit[j] += expectedRevenue * probability[i]  # 期望利潤 = 期望收入*賣出該i份報紙的機率
            leftProbabilitySum -= probability[i]
        else:
            expectedProfit[j] += expectedRevenue * leftProbabilitySum

    if j > 0 and expectedProfit[j] < expectedProfit[j - 1]:
        bestquantityOfOrder -= 1
        break

print(bestquantityOfOrder, int(expectedProfit[bestquantityOfOrder]))
