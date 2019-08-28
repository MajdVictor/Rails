import random
import sys

#Drawing sudoko board

s = {}
ct = 0
l = []
cell = []

counter_x = 1
counter_y = 0
random_numbers_list = [1,2,3,4,5,6,7,8,9]

def print_sudoku_board():
    
    global s
    
    if not s:
        
        s = {i+1:['  ' for i in range(1,10)] for i in range(9)}
        s[1][0] = '.3'
        s[1][2] = '.6'
        s[1][3] = '.5'
        s[1][5] = '.8'
        s[1][6] = '.4'
        s[2][0] = '.5'
        s[2][1] = '.2'
        s[3][1] = '.8'
        s[3][2] = '.7'
        s[3][7] = '.3'
        s[3][8] = '.1'
        #############
        s[4][2] = '.3'
        s[4][4] = '.1'
        s[4][7] = '.8'
        s[5][0] = '.9'
        s[5][3] = '.8'
        s[5][4] = '.6'
        s[5][5] = '.3'
        s[5][8] = '.5'
        s[6][1] = '.5'
        s[6][4] = '.9'
        s[6][6] = '.6'
        ##############
        s[7][0] = '.1'
        s[7][1] = '.3'
        s[7][6] = '.2'
        s[7][7] = '.5'
        s[8][7] = '.7'
        s[8][8] = '.4'
        s[9][2] = '.5'
        s[9][3] = '.2'
        s[9][5] = '.6'
        s[9][6] = '.3'

    counter = 0
    print(('-' * 34))
    
    for i in range(1,10):
        counter += 1
        print('| '+s[i][0],s[i][1],s[i][2],'|',s[i][3],s[i][4],s[i][5],'|',s[i][6],s[i][7],s[i][8],'|')
        if counter % 3 == 0:
            print('-'*34)
    
    return s
    
    
def get_cell(counter_x,counter_y):
    global cell
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

def generate_random_numbers():
    
    global s
    global ct
    global random_list
    global counter_x
    global counter_y
    global random_numbers_list
    global cell
    
    
    
    while counter_y != 9:
           
        random_number = [1,2,3,4,5,6,7,8,9]
        

        for z in range(9):
            get_cell(counter_x,z)
            if s[counter_x][z] == '  ':

                for h in range(9):
                    column = [s[i][z] for i in range(1,10)]
                    num = '.'+str(random_number[h])

                    if num not in s[counter_x] and num not in column and num not in cell :
                        s[counter_x][z] = num
                    
                        break
                    else:
                        pass
            counter_y += 1
                        

                            


print_sudoku_board()

for i in range(9):
    
    generate_random_numbers()
    counter_y = 0
    counter_x += 1
    random_numbers_list = [1,2,3,4,5,6,7,8,9]
    print_sudoku_board()
    
#print_sudoku_board()
print_sudoku_board()
