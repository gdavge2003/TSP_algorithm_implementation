import math


# Reads the TSP problem instance in input text file
# Input: text file with 3 numbers on each line: city identifier | x-coordinate | y-coordinate
# Output: list of (identifier, x, y) tuples.
def read_input_file(input_file):
    arr = []

    with open(input_file) as file:
        for line in file:
            line = line.split()
            line = [int(i) for i in line]
            arr.append(tuple(line))

    return arr


# Input: list of tuples in the format (identifier, x, y). Last element is total distance
# Should be answer to TSP problem.
# Output: text file with total distance, and cycle
def output_tour_file(tour, output_file):
    total_distance = tour.pop()

    with open(output_file, "w") as out:
        out.write("%s\n" % total_distance)

        for i in tour:
            identifier = i[0]
            out.write("%s\n" % identifier)


# build convex hull given points on a 2D euclidean space using monotone chain algorithm
# input: list with points in this tuple format: (identifier, x-coordinate, y-coordinate)
# output: list of points that is part of convex hull, in counter-clockwise order from left/bottom corner
def construct_convex_hull(arr):
    # remove duplicates and sort by increasing x, then y
    arr = sorted(set(arr), key=lambda x: (x[1], x[2]))

    # if empty or single point, return
    if len(arr) <= 1:
        return arr

    # cross product of OA and OB vectors. returns (+) if OAB makes counter-clockwise turn
    # returns negative for clockwise turn, and 0 for collinear
    def cross(o, a, b):
        return (a[1] - o[1]) * (b[2] - o[2]) - (a[2] - o[2]) * (b[1] - o[1])

    # lower hull
    lower = []
    for i in arr:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], i) <= 0:
            lower.pop()

        lower.append(i)

    # upper hull
    upper = []
    for i in reversed(arr):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], i) <= 0:
            upper.pop()

        upper.append(i)

    # construct upper and lower hulls together
    return lower[:-1] + upper[:-1]


# calculates the distance between two points
# input: tuples in the format (identifier, x, y)
# output: distance between them rounded to nearest integer
def distance_calculate(a, b):
    return int(round(math.sqrt((a[1]-b[1])**2 + (a[2]-b[2])**2)))