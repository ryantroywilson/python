"""
Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display
what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
The result should be like this:

import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
random_num = random.randint()

from random import randint
print(randint(0, 9))
"""
def score():
	import random
	x = random.randint(0,100) 
	print x
	if x >= 60 and x <=69:
		print "Score: 60 - 69; Grade - D"
	elif x >= 70 and x <= 79:
		print "Score: 70 - 79; Grade - C"
	elif x >= 80 and x <= 89:
		print "Score: 80 - 89; Grade - B"
	elif x >= 90 and x <= 100:			
		print "Score: 90 - 100; Grade - A"
	else:
		print "YOU FAILED!"

score()


