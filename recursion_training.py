houses = ["Majd's house","Charlie's house","Issa's house","Micho's house","Joseph's house","Amanda's house"]

def deliver_present(houses):

    if len(houses) == 0 :
        return 0

    else:
        half = len(houses)//2

        first_elve = houses[:half]
        first_elve.pop()
        second_half = houses[half:]
        second_half.pop()

        return deliver_present(first_elve) + deliver_present(second_half)
        
deliver_present(houses)

        
def hi_recursion(remaining):
    #base case
    if remaining == 0:
        return True
    
    print('hi')

    hi_recursion(remaining - 1)

#hi_recursion(5)

def print_five_hellos(counter):

    if counter == 0:
        return False
    
    else:
        print('hello')
        return print_five_hellos(counter - 1)



def get_sum(nums):
    #nums = list

    if len(nums) == 0:
        return 0
    else:
        poped_number = nums.pop()
        return poped_number + get_sum(nums)
        
def handout_presents(presents):
    
    if len(presents) == 0:
        return 0

    else:
        presents.pop()
        return handout_presents(presents)



def marking_tests(tests):

    if len(tests) == 0:
        return 0
    
    tests.pop()
    return 1 + marking_tests(tests)


def coins_change(coins, n)

    if n <= 0:
        return 0

    if 
    else:
        return n + coins_change(coins)
