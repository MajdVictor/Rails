## Q1
def count_redundancy(s):
    """returns a dictionary of letters and their count from the string s
    
    Arguments:
        s {string} 
    
    Returns:
        [dict] 
    """
    ##creating a new list of all letters in s
    list_of_chars = list(s)
    #creating a new set of unique letter
    set_of_chars = set(list_of_chars)
    count_dict = {}
    #iterating over the set elements and count their redundancy, and adding letter : count 
    #as key : value
    for element in set_of_chars:
        count_dict[element] = list_of_chars.count(element)

    return count_dict

## Q2
def flat_list(l):
    """returns a flat list
    
    Arguments:
        l {list} -- nested list
    
    Returns:
        [list] -- flat list
    """
    given_list = l
    new_list = []

    def iterate_over_list(l):
        ##iterating over the nested list and append the items to a new list
        for i in l:

            if type(i) == list:
                #if i is a list , the iterate_over_list() is called again to iterate over the inner elements in that
                #list
                iterate_over_list(i)

            else:
                #append to the new list
                new_list.append(i)

        return new_list
    
    print(iterate_over_list(l))

## Q3
def parse_url(url):
    """This is a simple URL parser. It takes a full string of url and returns a dictionary
    that contains 3 values: scheme, netloc and path
    
    Arguments:
        url {string} -- [description]
    """
    new_dict = {}

    scheme_index = url.find('https')
    netloc_index = url.find('://')
    path_index = url.find('.com/')

    new_dict['scheme'] = url[:netloc_index]
    new_dict['netloc'] = url[netloc_index+3:path_index+4]
    new_dict['path'] = url[path_index+4:]

    return new_dict

def parsing(filename1, filename2):
    line1 = ''
    line2 = ''
    new_line = ''

    d = open(filename2,'w')

    with open(filename1, 'r') as f:

        lines = f.readlines()
        for i in range(len(lines)-1):
        
            if 'Day' in lines[i]:
                d.write(lines[i])
            elif not lines[i].strip():
                d.write('\n')
            else:
                if lines[i+1].strip():
                    
                    next_line = lines[i+1]
                    d.write(lines[i][0:5] +'-'+next_line[:5]+lines[i][5:])
                
    f.close()



            




if __name__ == "__main__":
    parsing('cw2_data.txt','cw2_data_parsed.txt')


