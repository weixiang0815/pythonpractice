from matplotlib import pyplot as plt
import random

fig = plt.figure(figsize=(7, 5))

names = ["Henry", "Will", "John", "Mary"]
scores = [0, 0, 0, 0]
scores2 = [0, 0, 0, 0]
positions = [0, 1, 2, 3]
positions2 = [0, 0, 0, 0]
positions3 = [0, 0, 0, 0]
rd = random.Random()
for x in range(4):
    i = rd.randint(0, 100)
    scores[x] = i
    i = rd.randint(0, 100)
    scores2[x] = i
    positions2[x] = positions[x]+0.25
    positions3[x] = (positions[x]+positions2[x])/2

plt.bar(positions, scores, width=0.25, color="r")
plt.bar(positions2, scores2, width=0.25, color="b")
plt.xticks(positions3, names)

plt.title("Exam Scores")
plt.show()
