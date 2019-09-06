import itertools
import random

counter = 0
##Q1
#section a : all numbers 1 - 1000 divisible by 7
def divisible_by_7():
    print( [i for i in range(1,1000) if i%7 == 0] )

#section b : all numbers 1 - 1000 that have number 3
def numbers_have_three():
    print([i for i in range(1,1000) if '3' in str(i)])

#section c : remove all vowels in a string
def remove_vowels(s):
    print (''.join([letter for letter in s if letter not in 'aeoui']))

#section d : find all words in a string that are less than 4 chars
def find_words(s):
    print([word for word in s.split() if len(word) < 4 ])

#section e : find all number 1-1000 divisible by any digit
def numbers_divisible_by_any():
    # there are two way
    # 1- we could use the 'or' operator and check for all number 2-9 
    # 2- we could use another loop inside the list comprehension to loop over a list of divisible numbers

    print(set([i for i in range(1,1000) for j in [2,3,4,5,6,7,8,9] if i%j == 0]))

#Dictionary comprehension: a
def get_words_counts(s):
    print({word:len(word) for word in s.split()})

###----------------------------------------------------->
#Q2 Random operation
def random_operation(a, b):
    #picking random operation and apply it on the two numbers a and b
   operator = random.choice("+%/*")

   return eval(str(a) + operator + str(b))

#Q3 fibonacci using recursion
def fibonacci_recursion():

    def fibonacci(n):
        if(n <= 1):
            return n
        else:
            return(fibonacci(n-1) + fibonacci(n-2))
    
    for i in range(7):
        print (fibonacci(i))




