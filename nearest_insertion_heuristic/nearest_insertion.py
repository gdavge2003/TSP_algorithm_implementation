from nearest_insertion_heuristic.helper_functions import *


# nearest insertion for TSP
# input: list of points formatted as tuples: (identifier, x, y)
# output: list of points in tour order, with last element as total distance
def nearest_insertion_tsp(points):
    # setup initial subtour (convex hull)
    tour = construct_convex_hull(points)
    # print(tour)

    for i in tour:
        points.remove(i)

    # nearest insertion
    while len(points) > 0:
        insert_point = points.pop()
        distance_list = []

        # iterate through current tour to find minimum insert point
        for i in range(0, len(tour)):
            j = i+1
            if i == len(tour)-1:
                j = 0

            current_distance = distance_calculate(tour[i], tour[j])
            insertion_distance = distance_calculate(tour[i], insert_point) + distance_calculate(tour[j], insert_point)
            distance_list.append((i, insertion_distance - current_distance))

        insertion_index = min(distance_list, key=lambda t: t[1])[0] + 1
        tour.insert(insertion_index, insert_point)

        # print(tour)

    # calculate length of tour
    distance = 0
    for i in range(0, len(tour)):
        j = i + 1
        if i == len(tour) - 1:
            j = 0

        distance = distance + distance_calculate(tour[i], tour[j])

    tour.append(distance)

    return tour


# arr = [(0, 100, 0),
#        (1, 0, 100),
#        (2, 100, 100),
#        (3, 0, 0),
#        (4, 50, 50)]
#
# print(nearest_insertion_tsp(arr))
