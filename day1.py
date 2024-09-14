# Advent of code 2023
#---Day 1: Trebuchet?! ---

total = 0
with open("advent1.txt","r") as file:
    for line in file:
        line = line.strip()
        list = [int(i) for i in line if i.isnumeric()]
        calibration = list[0]*10 +list[-1]
        total += calibration 
    