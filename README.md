# LeetCode
Some codes of mine on the leetcode.
Here will be a description of some questions.
## tag=easy
### 1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:<br>
Given nums = [2, 7, 11, 15], target = 9,<br>

Because nums[0] + nums[1] = 2 + 7 = 9,<br>
return [0, 1].<br>
<br> 
### 7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:<br>
Input: 123
Output:  321
<br>
Example 2:<br>
Input: -123
Output: -321
<br>
Example 3:<br>
Input: 120
Output: 21
<br>
Note:<br>
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
<br>
### 9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
<br>
### 13. Roman to Integer
Given a roman numeral, convert it to an integer.<br>
Input is guaranteed to be within the range from 1 to 3999.<br>
<br>
Hit 1:
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000
<br>
Hit 2:<br>
Rules:<br>
* If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9<br>
* If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90<br>
* If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900<br>
<br>
