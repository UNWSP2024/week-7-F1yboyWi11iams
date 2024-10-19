# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
x1 = float(input("Enter a number for X: "))
y1 = float(input("Enter a number for Y: "))
z1 = float(input("Enter a number for Z: "))
x2 = float(input("Enter a number for X: "))
y2 = float(input("Enter a number for Y: "))
z2 = float(input("Enter a number for Z: ")
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
answer = sqrt ((x2 - x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
print(answer)
