import numpy as np

input = open("Day 1/input.txt", "r")
elfCount = 0
calories = np.zeros(1, dtype=int)
for line in input:
    if line.rstrip() == "":
        calories = np.append(calories, 0)
        elfCount += 1
    else:
        calories[elfCount] += int(line.rstrip())
input.close()

sortedCalories = np.sort(calories)[::-1]

print(f"Number of elves: {elfCount-1}")
print(f"Top calories 1: {sortedCalories[0]}")
print(f"Top calories 2: {sortedCalories[1]}")
print(f"Top calories 3: {sortedCalories[2]}")
print(f"Sum of top 3: {sortedCalories[0:3].sum()}")
