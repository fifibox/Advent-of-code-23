# Advent of code 2023
#--- Day 3: Gear Ratios ---

valid_symbols = "!@#$%^&*()_-+={}[]/"
total = 0

# function to check if there is any symbol next to a number
def check_symbol(x,y):
    flag=False
    # check left side
    if y>0:
        if line[y-1] in valid_symbols:
            flag = True
        elif x>0 and file[x-1][y-1] in valid_symbols:
            flag = True
        elif x+1<len(file) and file[x+1][y-1] in valid_symbols:
            flag = True
            
    # check right side
    if y+1<len(line):
        if line[y+1] in valid_symbols:
            flag=True
        elif x>0 and file[x-1][y+1] in valid_symbols:
            flag = True
        elif x+1<len(file) and file[x+1][y+1] in valid_symbols:
            flag = True
        
    # check the line above
    if (x>0 and file[x-1][y] in valid_symbols ):
            flag=True
    # check the line below 
    if (x+1<len(file) and file[x+1][y] in valid_symbols):
            flag=True
    return flag


file = []   
with open("input1.txt","r") as file_handler:
    for line in file_handler:    
        file.append(list(line.strip()))
        
x = 0 # positon of line
for line in file:
    digits = [] # to store number
    flag = False
    for y in range (len(line)):
        if line[y].isnumeric():
            digits.append(int(line[y]))
            if check_symbol(x,y):
                flag = True
                
        if y==len(line)-1 or (y<len(line)-1 and not line[y].isnumeric()):
            if flag:
                digits.reverse()
                number = sum([digits[i]*(10**i) for i in range(len(digits))])
                flag = False
                print(number)
                total += number
  
            digits=[]
                
    x += 1
print(total)

##part 2 

grid = open('input.txt','r').read().splitlines()
total = 0

for r,row in enumerate(grid):
    for c,ch in enumerate(row):
        if ch != '*' :
            continue
        
        # co_ordinate set 
        cs = set()
        for current_row in [ r-1, r, r+1]:
            for current_column in [c-1 , c , c+1]:
                if current_row < 0 or current_row >= len(grid) or current_column < 0 or current_column >= len(grid[current_row]) or not grid[current_row][current_column].isdigit():
                    continue

                # if it is a digit, find the beginning coordinate of the number
                while current_column > 0 and grid[current_row][current_column-1].isdigit():
                    current_column -= 1
                cs.add((current_row,current_column))

        if len(cs) == 2:
            num_set = []
            for cr,cl in cs:
                s = ''
                while cl < len(grid[cr]) and grid[cr][cl].isdigit():
                    s += grid[cr][cl]
                    cl += 1
                num_set.append(int(s))
            gear = num_set[0] * num_set[1]
            total += gear
print(total)
