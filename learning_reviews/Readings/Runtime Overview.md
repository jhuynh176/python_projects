# **Runtime Overview**

If we are given hints on the runtime requirement of a problem during interviews, we can roughly deduce the algorithm as follows. The important thing about runtime complexity is that we usually do not consider constants when analyzing the time complexity. We usually want to find the "family" of functions that most closely the growth in computational time. 

For instance, `O(2n)`, `O(5n)` can be loosely said to belong the family of functions `O(n)`. Therefore, if a solution runs in precisely `O(2n)` time, it is common convention to simply consider it an `O(n)` function and discard the constant. 

It is however important to be careful of constants, sometimes a sufficiently bad constant can increase runtime substantially. 

- In some specific cases one may want to consider optimizing algorithms to have a better constant. 
- In most cases however this is not necessary and basic runtime analysis can give a good indication of how efficient a solution is and whether or not it will pass.


## **`O(1)`**

Constant time complexity. Could be

- Hashmap lookup
- Finding and applying math formula
  
  
## **`O(log(N))`**

`log(N)` grows VERY slowly. `log(1,000,000)` is only about 20. In fact, lookup by primary key in a relational database is `log(N)` (many mainstream relational databases such as `postgres` use B-trees for indexing by default, and search in B-tree is `log(N)`).

In coding interviews, `log(N)` typically means

- `Binary search` or variant
- Balanced binary search tree lookup
  

## **`O(N)`**

Linear time normally means looping through a linear data structure a constant number of times. Most commonly this means

- Going through array/linked list
- `Two pointers`
- Some types of greedy
- Tree/graph traversal
- Stack/Queue
  

## **`O(K log(N))`**

- Heap push/pop K times. When you encounter problems that look for the "top K elements", you can usually solve them with pushing and popping to a heap, K times, resulting in `O(K log(N))` runtime. e.g., `K closest points`, `merge K sorted lists`.
- Binary search K times.


## **`O(N log(N))`**

- Sorting. The default sorting algorithm's expected runtime in all mainstream languages is N log(N). For example, java uses a variant of merge sort for object sorting and a variant of quick sort for primitive type sorting.
- Divide and conquer with a linear time merge operation. Divide is normally log(N), and if merge is `O(N)` then the overall runtime is `O(N log(N))`. An example problem is smaller numbers to the right.


## **`O(N^2)`**

Also called quadratic time.

- Nested loops, e.g., visiting each matrix entry
Many brute force solutions
For small N < 1000, this is actually not that bad for modern computers. In fact, you can probably pass most Leetcode tests with quadratic time for small Ns. However, in an interview, your solution usually has to do better than quadratic time to impress the interviewer if there is a better solution.


## **`O(2^N)`**

Grows very rapidly. Often requires memoization to avoid repeated computations and reduce complexity.

- Combinatorial problems, backtracking, e.g. subsets
  
  
## **`O(N!)`**

Grows insanely rapidly. Only solvable by computers for small N. Often requires memoization to avoid repeated computations and reduce complexity.

- Combinatorial problems, backtracking, e.g. permutations
