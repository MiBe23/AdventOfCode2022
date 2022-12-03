from typing import Any, Dict
import polars as pl


def mapValues(s: pl.Series, mapping: Dict[Any, Any]) -> pl.Series:
    return s.apply(lambda x: mapping.get(x, None))


def determineResult(x):
    dictPoints = {
        0: 3,
        1: 6,
        2: 0,
    }

    result = (x["me"] - x["elf"]) % 3
    return dictPoints.get(result, None)


def determineChoice(x):
    dictChoice = {
        0: -1,
        3: 0,
        6: 1,
    }

    op = dictChoice.get(x["points"], None)
    return (x["elf"] - 1 + op) % 3 + 1


dictElf = {
    "A": 1,
    "B": 2,
    "C": 3,
}
dictMe1 = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
dictMe2 = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

data = pl.read_csv("Day 2/input.txt", has_header=False, sep=" ")
part1 = data.select(
    [
        pl.all(),
        pl.col("column_1").map(lambda s: mapValues(s, mapping=dictElf)).alias("elf"),
        pl.col("column_2").map(lambda s: mapValues(s, mapping=dictMe1)).alias("me"),
    ]
)
part1 = part1.select(
    [
        pl.all(),
        pl.struct(["elf", "me"]).apply(lambda x: determineResult(x)).alias("points"),
    ]
)

choicePoints1 = part1["me"].sum()
resultPoints1 = part1["points"].sum()

print(f"Part 1:")
print(f"=======")
print(f"Choice points: {choicePoints1}")
print(f"Result points: {resultPoints1}")
print(f"Total points: {choicePoints1 + resultPoints1}")


part2 = data.select(
    [
        pl.all(),
        pl.col("column_1").map(lambda s: mapValues(s, mapping=dictElf)).alias("elf"),
        pl.col("column_2").map(lambda s: mapValues(s, mapping=dictMe2)).alias("points"),
    ]
)
part2 = part2.select(
    [
        pl.all(),
        pl.struct(["elf", "points"]).apply(lambda x: determineChoice(x)).alias("me"),
    ]
)


choicePoints2 = part2["me"].sum()
resultPoints2 = part2["points"].sum()

print(f"=======")
print(f"Part 2:")
print(f"=======")
print(f"Choice points: {choicePoints2}")
print(f"Result points: {resultPoints2}")
print(f"Total points: {choicePoints2 + resultPoints2}")
