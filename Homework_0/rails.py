'''
This python file contains the solutions for most of the exercises as functions,
and every function has it's own Docstring. 

written by: Majd Hafiri

'''

import random
import os
import sys

#Exercise 1
def print_all_numbers():
    """
    This function prints the numbers 0-5, with an interval of 0.1 between them.
    and without a decimal point.
    """
    #The counter is 0-9 and will be added next to numbers 0-5
    counter = 0
    
    for i in range (0,5):
        #add 0.1 next to every number without the decimal point
        while counter < 10:
            #when counter is zero , the integer number 0-5 will be printed
            if counter == 0:
                print (i)
            else:
                print(i, counter)

            counter += 1
        #reassign the counter to zero after every integer number 0-5
        counter = 0

#Example 2
def fibonacci():
    """
    This function prints out all the numbers in the Fibonacci sequence which are smaller than 10000
    """
    #x,y are the starting values for the secquence
    x = 0
    y = 1
    #temp variable is used to store the old value of x before assigning x = y in the while loop
    temp = y

    while x < 10000: 
        print(x)
        temp = x
        x = y
        y = temp + y


#Example 3
def divisible_by_seven():
    """
    This function prints out all the numbers between 0-100 divisible by 7
    """
    for i in range(0,101):
        #print the number 'i' if the remainder is equal to zero
        if i % 7 == 0:
            print(i)
#Example 4
def slicing():
    """
    This function prints out different sections of the string ("Hello, my name is Inigo Montoya")
    using slicing
    """

    s = "Hello, my name is Inigo Montoya"

    print(s[0:5]) # prints 'Hello'
    print(s[7:14]) # prints 'my name'
    print(s[::2])  #prints 'Hlo ynm sIioMnoa'
    print(s[2:19:2]) # prints 'lo ynm sI'

#Example 6
def five_digit_number():
    """
    This function receives a 5 digit number from the user and prints out:
    1. The number itself
    2. The digits, divided by commas (but not after the last digit)
    3. The sum of the digits

    """
    #newString is used to store the five numbers seperated by commas as a string
    newString = ''
    #sum variable used to store the sum of the 5-digit number 
    sum = 0
    #receive the user input and store it in number
    number = str(input("Please enter a 5 digit number\n"))
    #Iterate over the 5-digit number string 
    for num in number:
        newString += num+','
        sum += int(num)

    print('You entered the number: ', number)
    
    print('The digits of this number are: ', newString[:-1])

    print('The sum of the digits is: ', sum)

    
#Exercise 8.1
def multiplication(a, b):
    """This function will return the result of a * b
    
    Arguments:
        a  = integer or float 
        b  = integer or float
    
    Return:
    a * b
    """
    return a * b


# Exercise 8.2
def division(a, b):
    """This function returns the result of a / b and return illegal if b is 0
    
    Arguments:
        a = integer or float
        b = integer or float
    
    """
    if b == 0:
        return 'illegal'

    return a / b



# Exercise9
def random_list():
    """prints out a list of randomly selected numbers from 0-15 with interval of 2 

    """
    list1 = []
    index = []
    
    for i in range(15):
        list1.append(random.randint(0,15))
    print (list1[::2])

# Exercise 11    
def write_to_file(file1, file2):
    """
    This function will be called when exercise11_main() is executed.
    It will write the content of file1 to file2
    
    Arguments:
        file1 {string} -- The name of the file contains the text that will be copied to another file
        file2 {string} -- The name of the file where the text will be copied from file1
    """
    
    text_file_1 = open(file1,'r')
    text_file_2 = open(file2,'w')
    #read every line in file1 and write it to file2 
    for line in text_file_1:
        text_file_2.write(line)
    
    text_file_1.close()
    text_file_2.close()

#Exercise 12
def display_content(name):
    """This function will be called when exercise12_main() is executed.
    It prints out the content of a file
    
    Arguments:
        name {string} -- File name
    """
    text_file = open(name, 'r')
    print (text_file.read())
    text_file.close()

##exercise 13
def math_operations(homework_file, solutions_file):
    """This function will be called when exercise13_main() is executed.
    It writes the result of every math equation in homework_file to solutions_file.
    Every line in homework_file is a basic math equation (+,-,*,/)
    
    Arguments:
        homework_file {string} -- homework file name
        solutions_file {string} -- solutions file name
    """
    
    with open(homework_file, 'r') as h:
        with open(solutions_file, 'w') as s:
            #iterate over the lines in homework file and split every line to get the operands and the operator
            for line in h:
                items = line.split()
                #Check what the operator is and do the operation.
                # items[0] is the first operand
                # item[2] is the second operand
                # item[1] is the operator
                if items[1] == '+':
                    res = int(items[0]) + int(items[2])
                elif items[1] == '-':
                    res = int(items[0]) - int(items[2])
                elif items[1] == '/':
                    res = int(items[0]) / int(items[2])
                elif items[1] == '*':
                    res = int(items[0]) * int(items[2])
                #writing the result to solutions file 
                s.write(str(res))
                s.write("\n")
            s.close()
        h.close()


##exercise 17
def guessing_game():
    """
    This function will ask the user to guess the random selected number 0-9

    """
    random_number = random.randint(0,9)
    user_input = 11
    #This loop will keep running until the user enters the same number as the auto-generated one
    while user_input != random_number:

        user_input = input('Guess the auto-generated number 0-9: ')
        #check if the user enters a number or a character
        if user_input.isdigit() == False:
            #if the user enters 'exit' the loop will break
            if user_input.lower() == 'exit':
                print('You exited the game!')
                break
            else:
                print('Enter a number 0-9')
                continue
        #if the user guesses the number, it will print a message and breaks the while loop
        elif int(user_input) == random_number:
            print("You've guessed it!")
            break
        # if the user didn't guess the number , it will print a message
        else:
            print('try again!')


# Exercise 18      
def generate_password():
    """
    This function will generate a random (weak , strong) password based on the user_input

    """
    generated_password = ""
    #weak_pass_keys is used to generate weak passwords and they are all small letters
    weak_pass_keys = "qwertyuiopasdfghjklzxcvbnm"
    #strong_pass_keys is used to generate strong passwords which includes small letters, capital letters
    #and symbols
    strong_pass_keys = "1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP\{\}ASDFGHJKL:'ZXCVBNM<>?~`"
    
    
    user_input = str(input('Do you want to generate a "weak" or "strong" password: '))
    
    #if the user chooses weak , 10 randomly characters will be selected from weak_pass_keys
    if user_input.lower() == 'weak':

        for i in range(10):
            generated_password += random.choice(weak_pass_keys)

    #if the user chooses strong , 15 randomly characters will be selected from strong_pass_keys
    elif user_input.lower() == 'strong':

        for i in range(15):
            generated_password += random.choice(strong_pass_keys)
    #print a message if the user enters any word other than 'weak' or 'strong'
    else:
        print('Please enter the word "weak" or "strong" next time :)')

    


# Exercise 19
def all_numbers_below(num):
    """This function returns a list of all numbers less than 'num' and divisible by 3
    
    Arguments:
        num {integer} 
    
    """
    return [i for i in range(num,0,-1) if i%3 == 0] 


# Exercise 20
def diff_avg(list1,list2):
    """This function returns the average difference between list1 and list2
    
    Arguments:
        list1 { list }
        list2 { list }
    
    """
    return abs(sum(list1)/len(list1) - sum(list2)/len(list2))


#exercise11_main()  
def exercise11_main():
    """
    This function calls write_to_file()
    The script requires the user to pass the arguments (first_file, second_file) when running rails.py.
    To test exercise 11, call this function inside if __name__ == '__main__':

    """
    #if number of arguments is not 3 , it prints a message
    if len(sys.argv) != 3:
        print ('usage: ./rails.py file1.txt file2.txt')
        sys.exit(1)
    #Two arguments (text file1, text file2)
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    #if the two files were found , write_to_file() will be called 
    if filename1 == 'file1.txt' and filename2 == 'file2.txt':
        write_to_file(filename1, filename2)
    #print a message if one of the files is not found
    else:
        print ('unknown filenames!')
        sys.exit(1)

#exercise 12 main()
def exercise12_main():
    """
    This function calls display_content()
    The script requires the user to pass the argument (filename) when running rails.py.
    To test exercise 12, call this function inside if __name__ == '__main__':
    """
    #if number of arguments is not 2 , it prints a message
    if len(sys.argv) != 2:
        print ('usage: ./rails.py filename')
        sys.exit(1)
    #filename passed through the command line 
    filename = sys.argv[1]
    
    #throws a message if the file is not found
    try:
        if filename:
            display_content(filename)
    except:
        print ('file does not exist!')
        sys.exit(1)

#exercise 13 main()
def exercise13_main():
    """
    This function calls math_operations()
    The script requires the user to pass the arguments (homework filename, solutions filname) when running rails.py.
    To test exercise 13, call this function inside if __name__ == '__main__':
    """
    #if the number of arguments is not 3 it will print a message and ends the process
    if len(sys.argv) != 3:
        print ('usage: ./rails.py homework.txt solutions.txt')
        sys.exit(1)
    #Two files names 
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    #if both files exist, it calls math_operation() otherwise it prints a message and stops the process
    if filename1 == 'homework.txt' and filename2 == 'solutions.txt':
        math_operations(filename1, filename2)
    else:
        print ('unknown filenames!')
        sys.exit(1)



if __name__ == '__main__':
   random_list()


        