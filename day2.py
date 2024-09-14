# Advent of code 2023
#--- Day 2: Cube Conundrum ---

total = 0
game_id = 0

bag = {'red':12,'green':13,'blue':14}

with open("input.txt","r") as file:
    for game in file:
        
        game_id += 1
        flag = False
        
        # convert each game to a list of 3 sets
        game = game.split(':')[1].strip().split(';')
        
        
        for set in game:
            
            # convert each set to a list of cube number and color  
            set = set.split(',')
            set = [i.lstrip().split() for i in set]
            
            # check the number of each colour against dictionary 
            for cube in set:
                if int(cube[0]) > bag.get(cube[1]):
                    flag = True
                    break
            
        # add game ID if flag = Flase 
        if flag is False:
            total += game_id
                
print(total)

#---part 2 placeholder
        
                    


       
        
        
        


