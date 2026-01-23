# Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi using the method explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

# Ask user how many random points to generate. random. Uniform()
number_of_points = int(input("How many random points do you want to generate? "))

# Counters for the points
points_circle = 0 # n
points_total = 0 # N

import random

while points_total < number_of_points:
    # Generating a point (assigning x and y)
    x = random.uniform(-1,  1)
    y = random.uniform(-1,  1)

    # Check if point is inside the circle
    if x ** 2 + y ** 2 < 1:
        points_circle = points_circle + 1 # points_circle += 1

    points_total = points_total + 1 # points_total += 1

# pi approx = 4 * n / N
# Finally print out the approximation of pi to the user.
pi_approximation = 4 * points_circle / points_total
print(f"Pi is approximately: {pi_approximation}")