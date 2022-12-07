def findFirstUniqueString(data, length):
    window = []
    charCount = 0
    for c in data:
        window.append(c)
        if charCount > (length - 1):
            del window[0]
        if charCount > (length - 2):
            if len(set(window)) == length:
                break
        charCount += 1
    return window, charCount + 1


input = open("data/day6.txt", "r")
data = input.readline()
input.close()

[marker1, startOfPacket] = findFirstUniqueString(data, 4)
[marker2, startOfMessage] = findFirstUniqueString(data, 14)

print(f"Part 1:")
print(f"=======")
print(f"Marker: {marker1}")
print(f"Position: {startOfPacket}")

print(f"=======")
print(f"Part 2:")
print(f"=======")
print(f"Marker: {marker2}")
print(f"Position: {startOfMessage}")
