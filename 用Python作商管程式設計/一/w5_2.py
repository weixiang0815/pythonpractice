from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


n, p, d = map(int, input().split())  # 城鎮總數，預計選擇城鎮個數，基地台有效距離
town = [i for i in range(n)]
x, y, people = [], [], []  # x 座標，y 座標，城鎮人口數
for i in range(n):
    xi, yi, people_i = map(int, input().split())
    x.append(xi)
    y.append(yi)
    people.append(people_i)

best_town = []
people_covered_total = 0
for i in range(p):
    best_town_current = town[0]
    people_covered_most = 0
    best_town_covered = []
    for j in town:
        people_covered = people[j]
        town_covered = [j]
        for k in town:
            if k == j:
                continue
            if distance(x[j], y[j], x[k], y[k]) <= d:
                people_covered += people[k]
                town_covered += [k]
        if people_covered > people_covered_most:
            best_town_covered = town_covered
            people_covered_most = people_covered
            best_town_current = j
    best_town.append(best_town_current + 1)
    people_covered_total += people_covered_most
    for j in best_town_covered:
        town.remove(j)

for i in best_town:
    print(i, end=" ")
print(people_covered_total, end="")
