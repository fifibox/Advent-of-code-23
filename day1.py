# Advent of code 2023
#---Day 1: Trebuchet?! ---

total = 0

with open("advent1.txt","r") as file:
    for line in file:
        line = line.strip()
        list = [int(i) for i in line if i.isnumeric()]
        calibration = list[0]*10 +list[-1]
        total += calibration 

print(total)

#--part 2--

total = 0
num = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

with open("advent1.txt","r") as file:
    for line in file:
        line = line.strip()
        for key,value in num.items():
            if key in line:
                line = line.replace(key,key[0] + value + key[-1])
        list = [int(i) for i in line if i.isnumeric()]
        calibration = list[0]*10 +list[-1]
        total += calibration
        
print(total)
