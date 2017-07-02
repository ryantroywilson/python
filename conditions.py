"""Conditional statements or expressions in Python can be done
using if (and else) just like in other programming languages. We use these
conditional statements with logic operators to control the flow of
our programs.
"""
# if statement:
if <condition>:
  # do something
# if-else statement:
elif <condition>:
  # do something
else:
  # do this instead
"""
If there is construction
{
     use detour
}
else
{
     take the normal route
}
"""


#EXAMPLES!

age = 15
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'

  #OR

 if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!'


Operator	/      Description	Example
==	Checks if the value of two operands are equal or not, if yes then condition
becomes true.
(1 == 2) is not true.
(1 == 1) is true.

!=	Checks if the value of two operands are equal or not, if values are not
equal then condition becomes true.
(1 != 2) is true.

<>	Checks if the value of two operands are equal or not, if values are not
 equal then condition becomes true.
 (1 <> 2) is true. This is similar to != operator.*

>Checks if the value of left operand is greater than the value of right
operand, if yes then condition becomes true.
(1 > 2) is not true.

< Checks if the value of left operand is less than the value of right
 operand, if yes then condition becomes true.
 (1 < 2) is true.

>=	Checks if the value of left operand is greater than or equal to the value
of right operand, if yes then condition becomes true.
(1 >= 2) is not true.

<=	Checks if the value of left operand is less than or equal to the value of
right operand, if yes then condition becomes true.
(1 <= 2) is true.

and Checks each expression on the left and right. If both are true then this
evaluates true. If either or both expressions are false then
this is false
(1 <= 2 and 2 <= 3) is true.
(1 <= 2 and 2 >= 3) is false.
(1 >= 2 and 2 >= 3) is false.

or Checks each expression on the left and right. If either of the expressions
are true then this evaluates true. If both expressions are
false then this is false.
(1 <= 2 or 2 >= 3) is true.
(1 <= 2 or 2 <= 3) is true.
(1 >= 2 or 2 >= 3) is false.

not Reverses the true-false value of the operand	not(true) is false. 
not(false) is true.
not(1 >= 2) is true.
not(1 =< 2) is false.
not(1 <= 2 and 2 =< 3) is false.
not(1 >= 2 or 2 >= 3) is true.
