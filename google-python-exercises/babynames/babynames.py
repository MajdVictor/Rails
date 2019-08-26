#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):

  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006'def print_to_summary_file(names_list):, 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  year = ''
  final_list = []
  
  ##getting the year from the file name
  for i in filename:
    if i.isdigit():
      year += i
  ##add the year to the list as it's the first element
  final_list.append(year)
  #reading the text from the file
  with open(filename, 'r') as f:
    all_text = f.read()
  #finding the rank and the two names and store them as tuples in a list
  text = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', all_text)
  #unpacking tuples and add the rank with the associated name
  for rank, male, female in text:
    final_list.append(male+' '+rank)
    final_list.append(female+' '+rank)
  #printing the sorted list
  return sorted(final_list)

def print_to_summary_file(filename, names_list):
  #this function writes the names_list to the summary file (filename)
  with open(filename, 'w') as f:
    for item in names_list:
        f.write(' %s\n' %item)

  f.close()

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  list1 = []
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  #if the first argument is --summaryfile then the loop below will iterate over the arguments that follow 
  #arg[1] which is the name of the summary file.
  
  if args[0] == '--summaryfile':
    #looping over the html file and extract the name,rank and the year and call print_to_summary_file to write
    #the result to a summary file
    if len(args) > 2:
      for arg in args[2:]:
        list1 = extract_names(arg)
        print_to_summary_file(args[1], list1)
        print('Check your summary file!')
    else:
      print 'usage: [--summaryfile] file [file ...]'
      sys.exit(1)

  #If summaryfile option isn't specified then only one function will be called to print out the result
  #on the terminal
  elif args[0] != '--summaryfile':

    for arg in args:
      print(extract_names(arg))

  
if __name__ == '__main__':
  main()
