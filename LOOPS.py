"""
For Loop
We use the for loop when we know how many times we have to repeat our code.
You will mostly be using for loops in your programs, particularly in Python.
A for loop looks like this:
"""

for count in range (0,5):
    print "looping -", count
#output =
"""
looping - 0
looping - 1
looping - 2
looping - 3
looping - 4
"""
#Looping through a list

#create a new list
#remember lists can hold many data-types, even lists!
my_list = [4, 'dog', 99, ['list','inside','another','list'], 'hello world!']
for element in my_list:
    print element
#output =
"""
4
dog
99
['list', 'inside', 'another', 'list']
hello world!
"""


#While Loops !!!
"""While loops are often used when we don't know how many times we have to
repeat a block of code but we know we have to do it until a certain condition
is met.
"""
# same example as above but instead of for loop we will use while loops
count = 0
while count < 5:
    print 'looping - ', count
    count +=1
#output =
"""
looping -  0
looping -  1
looping -  2
looping -  3
looping -  4
"""

"""The break statement exits the current loop prematurely, resuming
execution at the first post-loop statement, just like the traditional break
found in C or JavaScript.

The most common use for the break is when some external condition is triggered,
requiring a hasty exit from a loop. The break statement can be used in both
while and for loop. When loops are nested, a break will only exit from the
innermost loop.
"""

for val in "string":
    if val == "i":
        break
    print val
#output =
#s
#t
#r

"""
The continue statement returns the control to the beginning of the loop.
The continue statement rejects -- or skips -- all the remaining statements in
the current iteration of the loop, and continues normal execution at the top of
the loop. The continue statement is very useful when you want to skip one or
more loop iterations, but keep looping to the end.
"""

for val in "string":
    if val == "i":
        countinue
    print val
#output  =
#s
#t
#r
#n
#g

# more examples of else statements in loops
x = 3
y = x
while y > 0:
    print y
    y = y - 1
else:
    print "Final else statement"
"""
output =
3
2
1
Final else statement
"""

x = 3
y = x
while y > 0:
    print y
    y = y - 1
    if y == 0:
        break
else:
    print "Final else statement"

"""
output =
3
2
1
""" 
