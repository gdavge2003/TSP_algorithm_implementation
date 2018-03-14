import sys
sys.path.append('../')
from nearest_insertion_heuristic.nearest_insertion import *
import time



# Main function for the "Nearest Insertion" heuristic
# Parameter should be the text file that has the TSP problem in correct format
# Outputs answer in new text file "<input_file_name>.tour"
# Outputs to terminal the runtime
def main(input_file):
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


# main("tsp_problems/tsp_example_1.txt")
# main("tsp_problems/tsp_example_2.txt")
# main("tsp_problems/tsp_example_3.txt")
# main("tsp_problems/test-input-1.txt")
# main("tsp_problems/test-input-2.txt")
# main("tsp_problems/test-input-3.txt")
# main("tsp_problems/test-input-4.txt")
# main("tsp_problems/test-input-5.txt")
# main("tsp_problems/test-input-6.txt")
# main("tsp_problems/test-input-7.txt")
main(str(sys.argv[1]))