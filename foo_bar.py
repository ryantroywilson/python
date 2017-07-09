"""
Optional Assignment: Foo and Bar
Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime 
number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar". 
Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you 
will have to figure out if it is a perfect square. It is, so print "Bar".

This assignment is extra challenging! Try pair programming and pulling up a white board.
"""	
for num in range(1,200+1):
    for i in range(2,201):
    	temp = i**2
        if (num % i!= 0):
			print "foo"
	if temp / i == i:
			print "bar!"



			