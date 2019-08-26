import itertools


### Q1 because 0.1 + 0.2 = 0.30000000000000004 which is not equal to 0.3

### Q2
def connect_two_string(a, b):
    """This function takes two strings, and prints them interlaced in one another.
    
    Arguments:
        a {string} 
        b {string}
    
    Returns:
        string 
    """

    def combining_chars(length, s, a, b):
        #This inner function accepts 4 arguments:
        ##length = the length of the smallest string
        ##s = the largest string
        ## and the two string a ,b

        new_string = ''
        ## iterate with the minimum length and add every character in both strings to new_string
        for i in range(length):
            new_string += a[i] + b[i]

        ## add the rest of the chars that come after the maximum length
        if s == 'a':
            return new_string + a[len(b):]

        return new_string + b[len(a):]

    ##calling combinig_chars() inner function and pass 4 parameters based on the length of a and b 
    if len(a) >= len(b):
        
        print(combining_chars(len(b),'a', a, b))

    else:

        print(combining_chars(len(a),'b', a, b))




#### Q3
def using_split_and_upper(s):
    """This function prints out the result of split() and upper() applied on string s
    
    Arguments:
        s {string}
    """
       
    print('split() result: '+ s.split())
    print('upper() result: '+ s.upper()) 


####Q4
def biggerIsGreater(s):
    
    new_string = ''
    
    #use enumerate to find the items and their indexes and the loop will break once it returns
    #the smallest bigger value which is always at index 1 
    for index,item in enumerate(itertools.permutations(s)):
        if index == 1:
            #this loop is used to concatinate the tuple elements at index 1
            for i in item:
                new_string += i

            return "the word is " + new_string

#### Q5 - Hangman game
def hangman_game():
    """This function includes the Algorithm for the Hangman game

    """
    #This variable represents the user's lives 
    lives = 5
    #printing out a title
    print('Hangman game\nYou have 5 lives, be careful!')
    #user input for the secret word 
    word = input('Enter a word: ')

    #dashes_list is used to show (-) for hidden letter and it has the same word's length
    dashes_list = ['-'] * len(word)
    #splitting the word into characters and put them in a list
    letters_list = list(word.lower())
    
    #This loop will break once the user loses all the 5 lives
    while lives != 0:
        
        letter = input('Guess a letter! :')
        
        
        if letter.lower() in letters_list:

            letter_index = letters_list.index(letter.lower())
            letters_list[letter_index] = '-'
            dashes_list[letter_index] = letter.lower()

            print(''.join(dashes_list))

        else:

            lives -= 1
            print('You have ',lives, ' more. ' + 'Be careful your losing lives!\n')

        if '-' not in dashes_list:
            print("Congrats! you've guessed the word :" + ''.join(dashes_list))
            break
            

    if '-' in dashes_list:
        print("You've lost, try again!")


    
    



if __name__ == "__main__":
    
    pass