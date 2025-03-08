# D. Can you Iterate the Binary String?

**time limit per test:** 0.5 seconds  
**memory limit per test:** 256 megabytes  

You are given **T** test cases. Each test case contains a **binary string S** that follows a specific pattern:

- There will be **zero or more** `0`s in the **prefix** of **S**.  
- There will be **zero or more** `1`s in the **suffix** of **S**.  

For each string, find the **index of the first occurrence** of the character `1` in **1-based indexing**.  
Find the output of each query in **O(log |S|)**.

## Input
- The first line contains an integer **T** (1 ≤ T ≤ 10⁴) — the number of test cases.  
- Each of the next **T** lines contains a **binary string S** (1 ≤ |S| ≤ 4 × 10³), where **|S|** represents the length of the string.

## Output
For each test case, print a single integer:

- The **first occurrence** of the character `1` in the string **S** in **1-based indexing**.  
- If there is **no `1`** in the string, print **−1**.

## Example

**Input**  
15  
0000011111111  
00000111111111    
00000  
0000  
1111  
111  
0  
1  
01  
01111  
000000000000001  
0000000000000001  
0000000000000111111111111111111111  
00000001111111111111111  
0000000111111111111111111111111111

**Output**  
6  
6  
-1  
-1  
1  
1  
-1  
1  
2  
2  
15  
16  
14  
8  
8