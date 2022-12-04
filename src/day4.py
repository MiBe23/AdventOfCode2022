import polars as pl


def determineFullOverlap(x):
    s1 = int(x["elf1"][0])
    s2 = int(x["elf1"][1])
    s3 = int(x["elf2"][0])
    s4 = int(x["elf2"][1])

    if (s1 >= s3) & (s2 <= s4):
        return 1
    elif (s1 <= s3) & (s2 >= s4):
        return 1
    else:
        return 0


def determinePartialOverlap(x):
    s1 = range(int(x["elf1"][0]), int(x["elf1"][1]) + 1)
    s2 = range(int(x["elf2"][0]), int(x["elf2"][1]) + 1)

    if set(s1).intersection(set(s2)):
        return 1
    else:
        return 0


data = pl.read_csv("data/day4.txt", has_header=False)
data = data.select(
    [
        pl.col(["column_1"]).str.split("-").alias("elf1"),
        pl.col(["column_2"]).str.split("-").alias("elf2"),
    ]
)
data = data.select(
    [
        pl.all(),
        pl.struct(["elf1", "elf2"])
        .apply(lambda x: determineFullOverlap(x))
        .alias("fullOverlaps"),
        pl.struct(["elf1", "elf2"])
        .apply(lambda x: determinePartialOverlap(x))
        .alias("partialOverlaps"),
    ]
)

fullOverlapCount = data["fullOverlaps"].sum()
partialOverlapCount = data["partialOverlaps"].sum()

print(f"Part 1:")
print(f"=======")
print(f"Full overlaps: {fullOverlapCount}")
print(f"=======")
print(f"Part 2:")
print(f"=======")
print(f"Partial overlaps: {partialOverlapCount}")
