import random
import sys

#Drawing sudoko board

s = {}
ct = 0
l = []
coordinates = [(x,y) for x in range(1,10) for y in range(0,9)]
counter_x = 1
counter_y = 0
random_numbers_list = [1,2,3,4,5,6,7,8,9]
def print_sudoku_board():
    
    global s
    

    if not s:
        
        s = {i+1:['  ' for i in range(1,10)] for i in range(9)}


    counter = 0
    print(('-' * 34))
    
    for i in range(1,10):
        counter += 1
        print('| '+s[i][0],s[i][1],s[i][2],'|',s[i][3],s[i][4],s[i][5],'|',s[i][6],s[i][7],s[i][8],'|')
        if counter % 3 == 0:
            print('-'*34)
    
    return s
    
    
    

def generate_random_numbers():
    
    global s
    global ct
    global random_list
    global counter_x
    global counter_y
    global random_numbers_list

    
    
    
    
    cell = []
    

    while counter_y != 9:
        
        
        random_number = random.choice(random_numbers_list)
        num = '.'+str(random_number)

        column = [s[i][counter_y] for i in range(1,10)]
        if counter_x <= 3 :
            if counter_y <= 2:
                cell = []
                for i in range (1,4):
                    for x in range(3):
                        cell.append(s[i][x])

            elif counter_y >= 3 and counter_y <= 5:
                cell = []
                for i in range (1,4):
                    for x in range(3,6):
                        cell.append(s[i][x])

                

            elif counter_y > 5:
                cell = []
                for i in range (1,4):
                    for x in range(6,9):
                        cell.append(s[i][x])
        
        elif counter_x >= 4 and counter_x <= 6:
            if counter_y <= 2:
                cell = []
                for i in range (4,7):
                    for x in range(3):
                        cell.append(s[i][x])
                

            elif counter_y >= 3 and counter_y <= 5:
                cell = []
                for i in range (4,7):
                    for x in range(3,6):
                        cell.append(s[i][x])
                

            elif counter_y > 5:
                cell = []
                for i in range (4,7):
                    for x in range(6,9):
                        cell.append(s[i][x])
        
        elif counter_x >= 7:

            if counter_y <= 2:
                cell = []
                for i in range (7,10):
                    for x in range(3):
                        cell.append(s[i][x])

            elif counter_y >= 3 and counter_y <= 5:
                cell = []
                for i in range (7,10):
                    for x in range(3,6):
                        cell.append(s[i][x])

            elif counter_y > 5:
                cell = []
                for i in range (7,10):
                    for x in range(6,9):
                        cell.append(s[i][x])
            

    
        if num not in s[counter_x] and num not in column and num not in cell :
            s[counter_x][counter_y] = num
            
            counter_y += 1
            random_numbers_list.remove(random_number)
        else:
            print_sudoku_board()
            generate_random_numbers()
            

        
        
    


#while '  ' in s[1] or '  ' in s[2] or '  ' in s[3] or '  ' in s[4] or '  ' in s[5] or '  ' in s[6] or '  ' in s[7] or '  ' in s[8] or '  ' in s[9]:
    ##create_filled_board()


print_sudoku_board()
for i in range(3):
    
    generate_random_numbers()
    counter_y = 0
    counter_x += 1
    random_numbers_list = [1,2,3,4,5,6,7,8,9]
    print_sudoku_board()
    
#print_sudoku_board()
print_sudoku_board()
