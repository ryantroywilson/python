"""

Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use
the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples
of 5 from 5 to 1,000,000.

Sum List
Create a program that prints the sum of all the values in
the list: a = [1, 2, 5, 10, 255, 3]

Average List
Create a program that prints the average of the values in
the list: a = [1, 2, 5, 10, 255, 3]

"""

#PART ONE: PRINT ALL ODD NUMBERS FROM 1 - 1000 (for loop) no lists

count = range(0,1000)
for i in count:
    if i%2!=0:
        print i

# PART TWO: prints all the multiples of 5 from 5 to 1,000,000.

count = range(0,1000000)
for i in count:
    if i%5==0:
        print i

# SUM LIST: print sum of all the values in list: a = [1, 2, 5, 10, 255, 3]
x = [1, 2, 5, 10, 255, 3]
y = sum(x)
print y

#Average List Create a program that prints the average of the values in
a = [1, 2, 5, 10, 255, 3]
b = sum(a)/len(a)
print b
