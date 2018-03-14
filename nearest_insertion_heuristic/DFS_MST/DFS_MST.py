# Program:              DFS_MST.py
# Author:               Jessica Calnan [OSU CS325-400-W2018 Project Group 26]
# Description:          TSP algorithm implementation that finds the minimum 
#						spanning tree using Kruskal's algorithm, then does a
#                       depth first search on the MST to find the tour.
# Commands:             1) cd into the directory containing all files.
#						2) At the command line type:
#                       	python DFSofMST.py inputFileName.txt

import math
import sys
import os
import timing

#start_time = time.time()
# -----------------------------------------------------------------------------	
def dist(city1, city2):
	d_x = city1['x'] - city2['x']
	d_y = city1['y'] - city2['y']
	sq_dx = math.pow(d_x, 2)
	sq_dy = math.pow(d_y, 2)
	return int(round(math.sqrt(sq_dx + sq_dy)))

# -----------------------------------------------------------------------------	
def pop_min(prqu):
	min_u = prqu[0]
	prqu.remove(prqu[0])
	return min_u

# -----------------------------------------------------------------------------	
def dec_key(prqu, cost):
	for i in range(len(prqu)):
		for j in range(len(prqu)):
			if cost[prqu[i]] < cost[prqu[j]]:
				prqu[i] = prqu[i] + prqu[j]
				prqu[j] = prqu[i] - prqu[j]
				prqu[i] = prqu[i] - prqu[j]

# -----------------------------------------------------------------------------	
class edge:
	u = None # 1st vertex
	v = None # 2nd vertex
	d = 0 # distance from 1st vertext to 2nd vertex
	def __init__(self, u, v, d):
		self.u = u
		self.v = v
		self.d = d

def kruskal_alg(adj_mtrx):
	edges = []
	for i in range(0, len(adj_mtrx) - 1):
		for j in range(i + 1, len(adj_mtrx)):
			e = edge(i, j, adj_mtrx[i][j])
			edges.append(e)		
	edges.sort(key = lambda x: x.d)
	
	previous = [None for x in range(len(adj_mtrx))]
	visited = []
	for e in edges:
#		print (str(e.d) + "," + str(e.u) + "," + str(e.v))
		if (not(e.v in visited)):
			visited.append(e.v)
#			print (visited)
			previous[e.v] = e.u
#			print (previous)
	return previous

# -----------------------------------------------------------------------------	
def prim_alg(adj_mtrx):
	cost = [sys.maxsize for x in range(len(adj_mtrx))]
	previous = [None for x in range(len(adj_mtrx))]
	prqu = [x for x in range(len(adj_mtrx))]

	cost[0] = 0
	dec_key(prqu, cost)

	while len(prqu) > 0:
		u = pop_min(prqu)

		for v in [v for v in range(len(adj_mtrx)) if adj_mtrx[u][v] > 0 and u != v]:
			dist = adj_mtrx[u][v]
			if v in prqu and dist < cost[v]:
				previous[v] = u
				cost[v] = dist
				dec_key(prqu, cost)

	return previous

# -----------------------------------------------------------------------------	
def adj_list_MST(adj_mtrx, MST):
	adj_list = {}
	for i in range(0, len(adj_mtrx)):
		adj_v = {}
		for j in range(0, len(MST)):
			if i == MST[j]:
				adj_v[j] = adj_mtrx[i][j]
		adj_list[i] = adj_v
	return adj_list

# -----------------------------------------------------------------------------	
def DFS(adj_list):
	visited = []
	stack = []
	stack.append(0)
#	print (stack)

	while(len(stack) > 0):
		u = stack[len(stack) - 1]
		stack.remove(stack[len(stack) - 1])
		if not (u in visited):
			visited.append(u)
			aux_stack = []
			for eachAdj in sorted(adj_list[u].items(), key=lambda x: x[1], reverse=True):
				v = eachAdj[0]
				if not (v in visited):
					aux_stack.append(v)
			while len(aux_stack) > 0:
				v = aux_stack[0]
				stack.append(v)
				aux_stack.remove(v)
#			print (stack)

	return visited

# -----------------------------------------------------------------------------	
def main():
	# get input file from user input
	if (len(sys.argv) != 2):
		print ('ERROR: Expected one argument only.  See instructions.\n')
		quit()
	else:
		in_file = sys.argv[1]
		if not(os.path.isfile(in_file)):
			print ('ERROR: File \'' + str(in_file) + '\' not found.\n')
			quit()

	# open in , out files
	base = os.path.basename(in_file)
	in_file = open(base, 'r')
	out_file = open(base + '.tour', 'w') #add .tour to end of out files

	# get cities from in_file, store in list
	cities = []
	for eachLine in in_file:
		city_iter = eachLine.split()
		curr_city = {'id':int(city_iter[0]), 'x':int(city_iter[1]), 'y':int(city_iter[2])}
		cities.append(curr_city)
#		print(curr_city)

	# initialize adj_mtrx for Graph (each city connected to all other cities)
	adj_mtrx = [[0 for x in range(len(cities))] for y in range(len(cities))]
	for i in range(0, len(cities)):
		for j in range(i + 1, len(cities)):
			ij = dist(cities[i], cities[j])
			adj_mtrx[i][j] = ij
			adj_mtrx[j][i] = ij
#		print (adj_mtrx[i])
	
	# generate MST using Prim or Kruskal alg
#	MST = primsAlg(adj_mtrx)
#	print (MST)
	MST = kruskal_alg(adj_mtrx)
#	print (MST)

	# turn MST into adj_list
	adj_list = adj_list_MST(adj_mtrx, MST)
#	print (adj_list)

	# find DFS discovery order
	discovery = DFS(adj_list)
#	print (discovery)	

	# find total distance from node (city) 0 to 1, to 2, to n-1, to n, to 0
	total_dist = 0
	cities_iter = iter(discovery)
	prev_city = cities[discovery[0]]
	next(cities_iter) # skip first city
	for eachItem in cities_iter:
		city_iter = cities[eachItem]
		# find distance to city_iter from the prev_city
#		print (city_iter)
#		print (prev_city)
		dist_add = dist(city_iter, prev_city)
		total_dist = total_dist + dist_add 
#		print ("%s: %s" % (dist_add, total_dist))
		prev_city = city_iter
	# find distance from final city in tour back to first city
	dist_add = dist(prev_city, cities[discovery[0]])
	total_dist = total_dist + dist_add 
#	print ("%s: %s" % (dist_add, total_dist))

	# write to out_file
	out_file.write(str(total_dist) + '\n')
	cities_iter = iter(discovery)
	for city_iter in cities_iter:
		out_file.write(str(city_iter) + '\n')

	in_file.close()
	out_file.close()
#print("--- %s Seconds ---" % (time.time() - start_time))

# -----------------------------------------------------------------------------	
if __name__ == "__main__":
	main()
