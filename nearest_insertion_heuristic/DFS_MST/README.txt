Jessica Calnan
OSU CS 325-400-W2018
TSP Project Group 26
3/14/18
DFS over MST Algorithm

Compile and Run DFS_MST.py:

At command line type:
	python DFS_MST.py <input file>
	example:  python DFS_MST.py tsp_example_1.txt

		*You should see a statement upon running DFS_MST on a file that looks like:
		"0:00:00.010 - Start Program" this indicates that the program has started and
		a timer is timing execution time.  When the execution is done you will see:
		"0:00:00.000 - End Program
		Elapsed time: 0:00:00.000" this indicates the time the program finished execting
		and how much time has passed during the execution = run time. Actual data below.
		Runtime Format [d:hh:mm:ss.ssss] 
		
Results:

Example Cases:
Prim's Algorithm on DFS_MST:
  Time				Input File			Output File					 Distance		Verified
0:00:00:00.9900		tsp_example_1.txt	tsp_example_1.txt.tour		   139725  		   Yes
0:00:01:21.3700		tsp_example_2.txt	tsp_example_2.txt.tour		     3819		   Yes
DNF

Kruskal's Algorithm on DFS_MST:
  Time				Input File			Output File					 Distance		Verified
0:00:00:00.0500		tsp_example_1.txt	tsp_example_1.txt.tour		   141813		   Yes
0:00:00:00.5700		tsp_example_2.txt	tsp_example_2.txt.tour			 3890		   Yes
0:11:46:52.8194		tsp_example_3.txt	tsp_example_3.txt.tour		  2955932		   Yes	


Competition Test Cases:
Prim's Algorithm on DFS_MST:
   Time				Input File			Output File					 Distance		Verified
0:00:00.190 		test-input-1.txt	test-input-1.txt.tour		   6914			   Yes
0:00:02.239  		test-input-2.txt	test-input-2.txt.tour		  10055			   Yes
0:00:49.090			test-input-3.txt	test-input-3.txt.tour		  15965			   Yes
0:08:03.800 		test-input-4.txt	test-input-4.txt.tour	      22346			   Yes
DNF 				test-input-5.txt	
DNF 				test-input-6.txt	
DNF		 			test-input-7.txt	

Kruskal's Algorithm on DFS_MST:
  Time				Input File			Output File					 Distance		Verified
0:00:00:00.0100     test-input-1.txt	test-input-1.txt.tour		    8397		   Yes
0:00:00:00.0800		test-input-2.txt	test-input-2.txt.tour		   12681		   Yes
0:00:00:00.5100		test-input-3.txt	test-input-3.txt.tour		   21611		   Yes
0:00:00:02.2600		test-input-4.txt	test-input-4.txt.tour		   31268		   Yes
0:00:00:15.2300		test-input-5.txt	test-input-5.txt.tour		   44272		   Yes
0:00:01:33.5800		test-input-6.txt	test-input-6.txt.tour		   61610		   Yes
(Exceeded 3 min.	test-input-7.txt	test-input-7.txt.tour		   Not Found in time
time limit)

Analysis:

Because there were two options for MST functions in the DFS algorithm that I chose to implement, I ran both
functions, (Prim and Kruskal,)  in order to find out which would be more efficient. Based on the results above,
I found that Kruskal's approach for finding the MST in the DFS algorithm was faster than Prim's.  After trying 
4 of the competition test cases and all of the example cases with Prim's approach, it was clear that Kruskal's
function would produce faster results. Therefore, after waiting an hour, I aborted the execution of DFS_MST using
Prim's approach and focused soley on Kruskal's approach. I included only these results in the report file.  
Although the algorithm using Kruskal's approach runs fairly quickly for relatively small input file sizes, 
it is still not efficient for larger input files.  The solutions are also not what I would expect to see and 
are not considered optimal.  Therefore, if I were to choose an algorithm to solve the TSP I would not choose a 
depth first search over a minimum spanning tree. 

Resources:

https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution/1557906#1557906
https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
https://www.ics.uci.edu/~eppstein/161/960206.html
https://cs.stackexchange.com/questions/6749/depth-first-search-to-find-minimum-spanning-tree
https://stackoverflow.com/questions/1195872/kruskal-vs-prim
https://stackoverflow.com/questions/29464252/adjacency-matrix-in-python
