import copy
import re

input = open("data/day5.txt", "r")
stacks = [[], [], [], [], [], [], [], [], []]
stacks1 = []
stacks2 = []
lineCounter = 0
for line in input:

    if lineCounter < 8:
        for i in range(len(stacks)):
            value = line[(i + 1) * 4 - 3]
            if value != " ":
                stacks[i].append(value)

    if lineCounter == 8:
        for stack in stacks:
            stack.reverse()
        stacks1 = copy.deepcopy(stacks)
        stacks2 = copy.deepcopy(stacks)

    if lineCounter > 9:
        numbers = re.findall("[0-9]+", line)
        amount = int(numbers[0])
        fromStack = int(numbers[1]) - 1
        toStack = int(numbers[2]) - 1

        stacks2[toStack].extend(stacks2[fromStack][-amount:])
        del stacks2[fromStack][-amount:]

        while amount > 0:
            stacks1[toStack].append(stacks1[fromStack][-1])
            stacks1[fromStack].pop()
            amount -= 1

    lineCounter += 1
input.close()

part1 = ""
for stack in stacks1:
    part1 += stack[-1]

part2 = ""
for stack in stacks2:
    part2 += stack[-1]

print(f"Part 1:")
print(f"=======")
print(f"Top crates: {part1}")

print(f"=======")
print(f"Part 2:")
print(f"=======")
print(f"Top crates: {part2}")
