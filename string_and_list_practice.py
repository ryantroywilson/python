
words = "It\'s thanksgiving day. It\'s my birthday,too!"
words.find("day");
print words.find("day");
words.replace("day","month");
print words.replace("day","month")

#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

x = [2,54,-2,7,12,98];
print min(x)
print max(x)

"""
Print the first and last values in a list like this one:
x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only
the first and last values in the original list. Your code should work for
any list.
"""
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]
y = [x[0],x[-1]]
print y

"""
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6].
Sort your list first. Then, split your list in half. Push the list created
from the first half to position 0 of the list created from the second half.
The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick
with it, this one is tough!
"""
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[:len(x)/2]
z = x[len(x)/2:]
print y
print z
x = [y]
x.extend(z)
print x
