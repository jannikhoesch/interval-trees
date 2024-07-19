# Experimental Analysis of Interval Trees

This repository contains a university project that I created for the course Advanced Data Structures at the Universitat Politècnica de Catalunya. The goal is to implement an Interval Tree in order to solve the linear stabbing problem and to demonstrate the effectiveness of this data structure under various configurations and query loads.

## Introduction
The linear stabbing problem is a fundamental problem in computational geometry, where the goal is to efficiently determine which of a set of intervals contain a given query point. 

![image](https://github.com/user-attachments/assets/055ecafc-ade5-414c-b956-04726224c8b1)

An Interval Tree is an advanced data structure designed to solve such problems by organizing intervals in a way that allows for fast querying. At its core, the Interval Tree is a binary search tree where each node stores an interval and potentially additional data structures to manage overlapping intervals efficiently. The tree partitions the space such that queries about which intervals overlap with any given point or another interval can be answered quickly.
![image](https://github.com/user-attachments/assets/0fb20418-d0c3-462d-bc0b-2b03dc1e9c8f)


## Implementation
The Interval Tree implemented in this project is designed to efficiently solve the linear stabbing problem, which involves identifying all intervals that contain a given query point. This section provides a brief description of the structure and functionality of my Interval Tree.
Each node in the Interval Tree contains a median value, computed from the start- and endpoints of the intervals. This median serves to categorize the intervals into three distinct groups: left intervals, which lie entirely to the left of the median; right intervals, entirely to the right; and crossing intervals, which span the median. To facilitate efficient queries, crossing intervals at each node are sorted into two lists: ’Crossing Left’, sorted by the starting points of the intervals, and ’Crossing Right’, sorted by the ending points in reverse order.
The query mechanism determines whether a point falls within any of the stored intervals by traversing the tree. If the query point is less than the node’s median, the function checks against the ’Crossing Left’ list; if greater, it checks against ’Crossing Right’. In cases where the point matches the median, all crossing intervals are returned. The tree traversal continues recursively as needed into either the left or right subtree. This process benefits from the sorted order of crossing intervals, enabling early termination of the search when it is clear no further intervals in the list can contain the point.

## Experiments
The experiments are designed to evaluate the performance of the Interval Tree and compare it to a naive interval querying method. For different numbers of intervals I measured the build time and memory usage of the Interval Tree and calculated the average time per query.
The data set consists of randomly generated intervals with endpoints within the range 1 to 1000. The number of intervals tested ranges up to 100000, incremented by 1000 intervals per experiment iteration. For each interval set an Interval Tree is built and the building time and memory usage measured. Then, 100 random point queries are executed that are solved both by the Interval Tree method and a naive method, that checks every interval linearly if it contains the query point. The taken time for each query is recorded and averaged in the end.

## Results
The results obtained from my experiment illustrate the performance characteristics of the Interval Tree in terms of memory usage, build time, and query efficiency.
Each interval is stored twice within the tree structure - in the sorted ’Crossing Left’ and ’Crossing Right’ lists of one node. The observed linear increase in memory consumption as the number of intervals increases as shown in Figure 1 aligns well with this theoretical assumption of a storage complexity of O(n).

![memory_usage](https://github.com/user-attachments/assets/72e23152-d1b1-472b-91f9-4a6665cd7916)

The build time of the Interval Tree (Figure 2) showed an increasing trend, consistent with the preprocessing complexity of O(nlogn). This complexity arises from the need to sort interval endpoints and to determine medians, which are necessary steps in constructing the tree’s nodes optimally. The graph indicates that the practical performance follows this expected complexity, with slight fluctuations possibly due to variations in the data distribution or the overhead of recursive tree construction.
The query time comparison between the Interval Tree and the naive method highlights the efficiency of the Interval Tree (Figure 3). The naive method’s performance degrades linearly as the number of intervals increases, which is expected given its O(n) complexity per query. In contrast, the Interval Tree maintains a much lower increase in query time, adhering to the O(log n + K) complexity, where K is the number of intervals in the query result. If all intervals contain the query point the query time is equal to the naive method, because all intervals are checked. The bigger the number of non-overlapping intervals the lower the query time of the tree method, as this enables the efficient usage of the data structure.

![build_time](https://github.com/user-attachments/assets/6c4d272e-e273-4477-9064-2c10a80ef3a8)

![query_time](https://github.com/user-attachments/assets/3eddfe61-7911-4530-8329-165538cf62dd)

## Conclusion
This project validated the effectiveness of the Interval Tree for solving the linear stabbing problem, demonstrating significant improvements in query efficiency over a naive approach. With build and query time complexities of O(n log n)) and O(log n + K) respectively, the Interval Tree efficiently balances build time, memory usage, and query speed, confirming its theoretical advantages. The results underscore the Interval Tree’s suitability for applications that demand fast and frequent interval data queries.




