"""
Write the following functions.
Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
When a string is passed, instead of displaying *, display the first letter of the string according to the example below. 
You may use the .lower() string method for this part.
For example:

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
Copy
draw_stars(x) should print the following in the terminal:

****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj
"""

def stars(arr):
    for x in arr:
        print "*" * x


nums = [1,2,3,4,5,6,7,8,9,1,5,3,2,7,3,9,19]
stars(nums)

def stars_part_two(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x = [12, "Ryan", 20, "Troy", 19, 20, "Wilson"]
stars_part_two(x)



