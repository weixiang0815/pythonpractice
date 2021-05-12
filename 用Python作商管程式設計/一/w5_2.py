def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


n, p, d = map(int, input().split())  # 城鎮總數，預計選擇城鎮個數，基地台有效距離
x, y, population = [0] * n, [0] * n, [0] * n  # x 座標， y 座標，城鎮人口數
for i in range(n):
    x[i], y[i], population[i] = map(int, input().split())
