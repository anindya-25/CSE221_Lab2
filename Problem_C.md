# C. Longest Subarray Sum

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  

You are given an array of **N** integers and an integer **K**. Your task is to find the length of the **longest contiguous subarray** whose sum is **less than or equal to K**.

## Input
- The first line contains two integers **N** (1 ≤ N ≤ 10⁵) and **K** (1 ≤ K ≤ 10⁹) — the size of the array and the maximum allowed sum.  
- The second line contains **N** space-separated integers **a₁, a₂, a₃, ..., aₙ** (1 ≤ aᵢ ≤ 10⁶) — the elements of the array.

## Output
Print a single integer — the length of the **longest contiguous subarray** whose sum is **less than or equal to K**.

## Examples

**Input**
5 4
4 1 2 1 5

**Output**
3

**Input**
5 5
1 1 1 1 1

**Output**
5

**Input**
3 1
2 3 4

**Output**
0

**Input**
10 12
1 2 6 4 3 2 3 1 4 2

**Output**
5

**Note**
In the first example, possible subarrays with sum less than or equal to 4 are [4],[1],[2],[1],[1,2],[2,1],[1,2,1]. Among them, the longest size is 3.

In the second example, sum of the entire array is 5. Hence, we can take the whole array.

In the third example, no subarray has sum less than or equal to 1. Hence, the answer is 0.