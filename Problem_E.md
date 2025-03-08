# E. Count the Numbers

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  

You are given a **sorted array** `a` of **n** elements, and some queries. In each query, you are given a pair **[x, y]**, and you have to count how many numbers **aᵢ** satisfy the condition **x ≤ aᵢ ≤ y**.  

For example, if the array is **[10, 20, 20, 45, 79]** and you are given a query **[20, 50]**, then the answer will be **3**, because there are **3 numbers** in total that have values between **20** and **50**.

## Input
- The first line of the input contains two integers **n** (1 ≤ n ≤ 10⁵) and **q** (1 ≤ q ≤ 10⁵), denoting the **array size** and the **number of queries**, respectively.  
- The next line contains **n** space-separated integers representing the sorted array **a** (1 ≤ aᵢ ≤ 10⁹) where **i = 0, 1, 2, ..., n−1**.  
- Each of the next **q** lines contains a pair **[x, y]** (1 ≤ x ≤ y ≤ 10⁹).  

📌 **Notes:**  
1. It is **guaranteed** that the given array is **sorted in non-decreasing order**.  
2. It is also **guaranteed** that the queries are **valid**, meaning for each query **[x, y]**, the condition **x ≤ y** always holds.

## Output
For each query **[x, y]**, print a single integer **P** denoting the number of elements in the array **a** such that **x ≤ aᵢ ≤ y**.


## Example

**Input**  
5 3  
10 20 20 45 79  
20 50  
5 45  
1 100

**Output**  
3  
4  
5