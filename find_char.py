"""
Write a program that takes a list of strings and a string containing a single character, and prints a new list 
of all the strings containing that character.

Here's an example:

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
Copy
Hint: how many loops will you need to complete this task?
"""

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for i in word_list:
    for character in char:
        if character in i:
        	new_list.append(i)
        	break
print new_list

 	

            



