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

