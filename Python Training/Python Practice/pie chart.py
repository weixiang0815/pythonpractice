from matplotlib import pyplot as plt

plt.figure(figsize=(5, 5))

labels = ["Taiwan", "USA", "Japan", "Korea", "China"]
power = [59, 23, 50, 31, 20]
explode = [0.05, 0, 0, 0, 0]
color = ["c", "b", "y", "g", "r"]

plt.pie(power, labels=labels, autopct="%1.f%%", explode=explode, colors=color)

plt.show()
