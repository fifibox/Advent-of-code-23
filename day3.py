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

##part 2 placeholder
def convert_num(digits): # [3,2,1] returns 123
    total = 0
    for i in range(len(digits)):
        total += digits[i]*10**i
    return total

data = []
rowsFound = [] # store row number which contains *

with open('input.txt','r') as file:
    for line in file:
        if '*' in line:
            rowsFound.append(len(data))
        data.append(list(line.strip()))


for row in rowsFound:
    line = data[row]
    digit = []
    count = 0
    numbers = []
    position = line.index('*')
    while line[position-1].isnumeric():
        digit.append(int(line[position-1]))
        position -= 1
    if len(digit) >0:
        count += 1
        numbers.append(convert_num(digit))
    
    position = line.index('*')
    digit = []
    while line[position+1].isnumeric():
        digit.append(int(line[position+1]))
        position += 1
    
    # check line above 
    if row>0:
        line = data[row-1]
        digit = []
        
    print(count,numbers)
        




        
                      
