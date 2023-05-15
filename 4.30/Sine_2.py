import math

sin = math.sin
pi = math.pi

for i in range(41):
    x = float(i) / 40.0 * 2 * pi
    character_count_per_line = int(40*x)  # Change this line to print out sine curve correctly.

    output_str = '#' * character_count_per_line
    print(output_str)