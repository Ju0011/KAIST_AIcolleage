import elice_utils
import csv
lines = list()
with open("./tpmon.txt", "r") as f:
    for line in f:
        lines.append(line.strip().split(","))

print(lines)
f.close()