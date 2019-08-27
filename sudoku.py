import random
#Drawing sudoko board

s = {}
ct = 0
l = []
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
    
    random_number = random.randint(1,9)
    
    random_x = random.randint(1,9)
    random_y = random.randint(0,8)
    
    
    
    column = [s[i][random_y] for i in range(1,10)]

    num = '.'+str(random_number)
    cell = []

    if random_x <= 3 :
        if random_y <= 2:

            cell.append(s[1][0])
            cell.append(s[1][1])
            cell.append(s[1][2])
            cell.append(s[2][0])
            cell.append(s[2][1])
            cell.append(s[2][2])
            cell.append(s[3][0])
            cell.append(s[3][1])
            cell.append(s[3][2])

        elif random_y >= 3 and random_y <= 5:
            cell.append(s[1][3])
            cell.append(s[1][4])
            cell.append(s[1][5])
            cell.append(s[2][3])
            cell.append(s[2][4])
            cell.append(s[2][5])
            cell.append(s[3][3])
            cell.append(s[3][4])
            cell.append(s[3][5])

            

        elif random_y > 5:
            cell.append(s[1][6])
            cell.append(s[1][7])
            cell.append(s[1][8])
            cell.append(s[2][6])
            cell.append(s[2][7])
            cell.append(s[2][8])
            cell.append(s[3][6])
            cell.append(s[3][7])
            cell.append(s[3][8])
    
    elif random_x >= 4 and random_x <= 6:
        if random_y <= 2:
            cell.append(s[4][0])
            cell.append(s[4][1])
            cell.append(s[4][2])
            cell.append(s[5][0])
            cell.append(s[5][1])
            cell.append(s[5][2])
            cell.append(s[6][0])
            cell.append(s[6][1])
            cell.append(s[6][2])
            

        elif random_y >= 3 and random_y <= 5:
            cell.append(s[4][3])
            cell.append(s[4][4])
            cell.append(s[4][5])
            cell.append(s[5][3])
            cell.append(s[5][4])
            cell.append(s[5][5])
            cell.append(s[6][3])
            cell.append(s[6][4])
            cell.append(s[6][5])
            

        elif random_y > 5:
            
            cell.append(s[4][6])
            cell.append(s[4][7])
            cell.append(s[4][8])
            cell.append(s[5][6])
            cell.append(s[5][7])
            cell.append(s[5][8])
            cell.append(s[6][6])
            cell.append(s[6][7])
            cell.append(s[6][8])
    
    elif random_x >= 7:

        if random_y <= 2:
            
            cell.append(s[7][0])
            cell.append(s[7][1])
            cell.append(s[7][2])
            cell.append(s[8][0])
            cell.append(s[8][1])
            cell.append(s[8][2])
            cell.append(s[9][0])
            cell.append(s[9][1])
            cell.append(s[9][2])

        elif random_y >= 3 and random_y <= 5:
            
            cell.append(s[7][3])
            cell.append(s[7][4])
            cell.append(s[7][5])
            cell.append(s[8][3])
            cell.append(s[8][4])
            cell.append(s[8][5])
            cell.append(s[9][3])
            cell.append(s[9][4])
            cell.append(s[9][5])

        elif random_y > 5:
            
            cell.append(s[7][6])
            cell.append(s[7][7])
            cell.append(s[7][8])
            cell.append(s[8][6])
            cell.append(s[8][7])
            cell.append(s[8][8])
            cell.append(s[9][6])
            cell.append(s[9][7])
            cell.append(s[9][8])

    
    if '.'+str(random_number) not in s[random_x] and '.'+str(random_number) not in column and '.'+str(random_number) not in cell:
        s[random_x][random_y] = '.'+str(random_number)
       

    else:
        #elif '.'+str(random_number) in s[random_x] and '.'+str(random_number) in column and '.'+str(random_number) in cell:
        
        generate_random_numbers()
        

print_sudoku_board()

while ct <= 90:

    generate_random_numbers()

    ct += 1


print_sudoku_board()
