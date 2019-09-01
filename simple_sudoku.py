
#this is a partially filled sudoku board that will be solved by the user after
#the program solves it and erase some cells randomly
sudoku_board = {0:[7,8,'  ',4,'  ','  ',1,2,'  '],
    1:[6,'  ','  ','  ',7,5,'  ','  ',9],
    2:['  ','  ','  ',6,'  ',1,'  ',7,8],
    3:['  ','  ',7,'  ',4,'  ',2,6,'  '],
    4:['  ','  ',1,'  ',5,'  ',9,3,'  '],
    5:[9,'  ',4,'  ',6,'  ','  ','  ',5],
    6:['  ',7,'  ',3,'  ','  ','  ',1,2],
    7:[1,2,'  ','  ','  ',7,4,'  ','  '],
    8:['  ',4,9,2,'  ',6,'  ','  ',7]
}

               
                
def print_sudoku_board(s):
    """This function prints out the sudoku board with all vertical and horizantal lines
    
    Arguments:
        s {dict} -- [key = row , value = column]
    """
    counter = 0
    #change the numbers in the dictionary to fixed values by adding '.' to every number
    for item in range(9):
        for x in range(9):
            if s[item][x] != '  ':
                s[item][x] = '.'+str(s[item][x])
    #print the upper line
    print(('-' * 34))
    #print all the rows with the values 
    for i in range(9):
        counter += 1
        print('| '+s[i][0],s[i][1],s[i][2],'|',s[i][3],s[i][4],s[i][5],'|',s[i][6],s[i][7],s[i][8],'|')
        #print separator line after every 3 rows
        if counter % 3 == 0:
            print('-'*34)
            
def validity(coordinates, number, sudoku_board):
    """This function returns false if the number is in the row , column or box
    
    Arguments:
        coordinates {tuple} -- position of the empty cell
        number {int} 
        sudoku_board {dict} 
    
    Returns:
        [bool] -- False if the number is either in the row or the column or the block
    """

    #check if number exists in the row
    for x in range(9):
        if sudoku_board[coordinates[0]][x] == number:
            return False
    #check if number exists in the column 
    for y in range(9):
        if sudoku_board[y][coordinates[1]] == number:
            return False

    cube_x = coordinates[0] // 3
    cube_y = coordinates[1] // 3

    for x in range(cube_x * 3, cube_x * 3 + 3):
        for y in range(cube_y * 3, cube_y * 3 + 3):
            if sudoku_board[x][y] == number:
                return False
    
    return True


def empty_cells(sudoku_board):

    for x in range (0,len(sudoku_board)):
        for y in range (9):
            
            if sudoku_board[x][y] == '  ':
                return(x, y)

    return None
def solve_sudoku_board(sudoku_board):

    empty = empty_cells(sudoku_board)

    if not empty:
        return True
    else:
        row, column = empty

    for i in range(1,10):
        if validity((row,column), i, sudoku_board):
            sudoku_board[row][column] = i
            
            
            if solve_sudoku_board(sudoku_board):
                return True

            sudoku_board[row][column] = '  '
            

    return False


            

    





solve_sudoku_board(sudoku_board)
print_sudoku_board(sudoku_board)
