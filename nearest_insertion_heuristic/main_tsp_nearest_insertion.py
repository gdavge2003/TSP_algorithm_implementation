from nearest_insertion_heuristic.nearest_insertion_tsp import nearest_insertion_tsp
from nearest_insertion_heuristic.helper_file_functions import *
import time
import sys


# Main function for the "Nearest Insertion" heuristic
# Parameter should be the text file that has the TSP problem in correct format
# Outputs answer in new text file "<input_file_name>.tour"
# Outputs to terminal the runtime
def nearest_insertion_main(input_file):
    # setup data for TSP from input file
    points = read_input_file(input_file)

    # solve TSP; record time for it
    start_time = time.time()
    tour = nearest_insertion_tsp(points)
    r_time = time.time() - start_time

    # output solution
    file_name = input_file + ".tour"
    output_tour_file(tour, file_name)

    # output runtime in terminal
    print("TSP problem from " + input_file + " solved in:", r_time, "seconds.")


#nearest_insertion_main("tsp_example_1.txt")
nearest_insertion_main(str(sys.argv[1]))