import re


class dir:
    def __init__(self, name, parentDir=NotImplemented):
        self.fileSize = 0
        self.dirSize = 0
        self.dirList = []
        self.name = name
        self.parentDir = parentDir

    def addFile(self, fileSize):
        self.fileSize += fileSize

    def addDir(self, dir):
        self.dirList.append(dir)

    def setDirSizes(self):
        if self.dirList:
            for dir in self.dirList:
                self.dirSize += dir.setDirSizes()
        self.dirSize += self.fileSize
        return self.dirSize


dirDict = {"/": dir("/")}
curDir = dirDict["/"]
input = open("data/day7.txt", "r")
for line in input:
    if "$ cd" in line.rstrip():
        arg = line.rstrip().split(" ")[-1]
        if arg == "..":
            curDir = curDir.parentDir
        elif arg == "/":
            curDir = dirDict[arg]
        else:
            curDir = dirDict[curDir.name + "/" + arg]
    elif "$ ls" in line.rstrip():
        continue
    elif "dir " in line.rstrip():
        arg = line.rstrip().rsplit(" ")[-1]
        newDirName = curDir.name + "/" + arg
        dirDict.update({newDirName: dir(newDirName, parentDir=curDir)})
        curDir.dirList.append(dirDict[newDirName])
    else:
        curDir.addFile(int(re.findall("[0-9]+", line)[0]))
input.close()

dirDict["/"].setDirSizes()

totalSpace = 70000000
neededSpace = 30000000
usedSpace = dirDict["/"].dirSize
spaceToDelete = neededSpace - (totalSpace - usedSpace)

part1 = 0
part2 = usedSpace
for x in dirDict:
    xSize = dirDict[x].dirSize
    if xSize <= 100000:
        part1 += xSize
    if (xSize >= spaceToDelete) & (xSize <= part2):
        part2 = xSize


print(f"Part 1:")
print(f"=======")
print(f"Total sum: {part1}")

print(f"=======")
print(f"Part 2:")
print(f"=======")
print(f"To delete: {part2}")
