def getValue(s: str):
    if s.isupper():
        return ord(s) - ord("A") + 27
    else:
        return ord(s) - ord("a") + 1


priority1 = 0
priority2 = 0
lineCount = 0
groupString = ["", "", ""]
input = open("data/day3.txt", "r")
for line in input:
    n = len(line)
    s1 = line[0 : n // 2]
    s2 = line[n // 2 :]
    res = "".join(set(s1).intersection(s2))
    priority1 += getValue(res)

    groupString[lineCount] = line.rstrip()
    if lineCount == 2:
        badge = "".join(
            set(groupString[0])
            .intersection(groupString[1])
            .intersection(groupString[2])
        )
        priority2 += getValue(badge)
        lineCount = 0
    else:
        lineCount += 1
input.close()


print(f"Part 1:")
print(f"=======")
print(f"Total priority: {priority1}")

print(f"Part 2:")
print(f"=======")
print(f"Total priority: {priority2}")
