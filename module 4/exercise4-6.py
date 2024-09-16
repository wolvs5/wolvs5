#Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0).
# Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square.
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle
# A correlates with the fraction of the area of circle
# A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi:
# Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points.
# Each point inside the square is tested for whether it resides inside circle A.
# Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A
# by testing if it fulfills the inequation x^2+y^2<1.).
from random import uniform

#main
i = n = 0
point = int(input("please enter the number of random points: "))
while i < point:
    x = y = uniform( -1,1)

    if x*x + y*y < 1:
        n+=1
    i+=1
print("Approximation of pi calculated by", point,"random points is:", n*4/point)