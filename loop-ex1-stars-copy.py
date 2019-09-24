# Loops help us to do a particular task many times
# Example 1

# The range() function defaults to 0 as a starting value, however it is possible 
# to specify the starting value by adding a parameter: range(a, b, c) which means 
# values from 'a' to 'b' (but not including 'b') and increases by 3 each time

# Let's add all of the numbers from 1 to 10:

# total will keep track of the sum of the numbers as they are 
# added


# this for loop creates the top triangle
stars = ""
for x in range(1, 10, 1):
  stars = stars + "*" 
  print (stars)


# this for loop creates the bottom triangle
stars = ""
for x in range(1, 10, 1):
  stars = stars + "*" 
  print (stars)