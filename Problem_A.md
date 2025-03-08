# A. Two Sum Trouble

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  

Your little brother, Bob, loves playing with integers. One day, his teacher gave him a sorted list of N integers in **non-decreasing** order. Now, your brother wants to play a game with you.  

Bob will give you an integer **S**. You have to find if it is possible to find two values from the list (at distinct positions) whose sum is equal to **S**.  

Since you are feeling very tired, you decide to write a program that can quickly answer Bob's query.

## Input
The first line contains two integers **N** (1 ≤ N ≤ 10⁶) and **S** (1 ≤ S ≤ 10⁹), denoting the length of the list and the target sum.  

In the next line, there will be **N** integers **a₁, a₂, a₃, ..., aₙ** (1 ≤ aᵢ ≤ 10⁹) in **non-decreasing** order, separated by spaces.

## Output
Print two distinct **1-based** indices **i** and **j** such that **aᵢ + aⱼ = S** where **i < j**. If no such pair exists, then print **-1**.  
If multiple solutions exist, you may print any one of the valid answers.

## Examples

**Input**  
4 10  
1 3 5 7

**Output**  
2 4

**Input**  
6 18  
1 5 8 9 9 10

**Output**  
3 6

**Input**  
4 7  
2 4 6 8

**Output**  
-1

**Input**  
4 10  
1 5 6 8

**Output**  
-1

**Note**  
In the second sample input, 4 5 is also a valid output.