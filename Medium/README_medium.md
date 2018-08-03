# LeetCode
Some codes of mine on the leetcode.
Here will be a description of some questions.
## tag=medium
### 002. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</br>
You may assume the two numbers do not contain any leading zero, except the number 0 itself.</br>

Example</br>
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)</br>
Output: 7 -> 0 -> 8</br>
Explanation: 342 + 465 = 807.</br>

### 003. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.</br>

Examples:</br>
Given "abcabcbb", the answer is "abc", which the length is 3.</br>
Given "bbbbb", the answer is "b", with the length of 1.</br>
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.</br>

### 005. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:</br>
Input: "babad"</br>
Output: "bab"</br>
Note: "aba" is also a valid answer.</br>

Example 2:</br>
Input: "cbbd"</br>
Output: "bb"</br>

### 006. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</br>

P   A   H   N</br>
A P L S I I G</br>
Y   I   R</br>
And then read line by line: "PAHNAPLSIIGYIR"</br>
Write the code that will take a string and make this conversion given a number of rows:</br>
string convert(string s, int numRows);</br>

Example 1:</br>
Input: s = "PAYPALISHIRING", numRows = 3</br>
Output: "PAHNAPLSIIGYIR"</br>

Example 2:</br>
Input: s = "PAYPALISHIRING", numRows = 4</br>
Output: "PINALSIGYAHRPI"</br>
Explanation:</br>
P     I    N</br>
A   L S  I G</br>
Y A   H R</br>
P     I</br>

### 008. String to Integer (atoi)
Implement atoi which converts a string to an integer.</br>
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.</br>
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.</br>
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.</br>
If no valid conversion could be performed, a zero value is returned.</br>

Note:</br>
Only the space character ' ' is considered as whitespace character.</br>
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.</br>

Example 1:</br>
Input: "42"</br>
Output: 42</br>

Example 2:</br>
Input: "   -42"</br>
Output: -42</br>
Explanation: The first non-whitespace character is '-', which is the minus sign.</br>
             Then take as many numerical digits as possible, which gets 42.</br>

Example 3:</br>
Input: "4193 with words"</br>
Output: 4193</br>
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.</br>

Example 4:</br>
Input: "words and 987"</br>
Output: 0</br>
Explanation: The first non-whitespace character is 'w', which is not a numerical </br>
             digit or a +/- sign. Therefore no valid conversion could be performed.</br>

Example 5:</br>
Input: "-91283472332"</br>
Output: -2147483648</br>
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.</br>
             Thefore INT_MIN (−231) is returned.</br>
             
### 012. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.</br>
Symbol       Value</br>
I             1</br>
V             5</br>
X             10</br>
L             50</br>
C             100</br>
D             500</br>
M             1000</br>
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.</br>
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:</br>

I can be placed before V (5) and X (10) to make 4 and 9. </br>
X can be placed before L (50) and C (100) to make 40 and 90. </br>
C can be placed before D (500) and M (1000) to make 400 and 900.</br>
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.</br>

Example 1:</br>
Input: 3</br>
Output: "III"</br>

Example 2:</br>
Input: 4</br>
Output: "IV"</br>

Example 3:</br>
Input: 9</br>
Output: "IX"</br>

Example 4:</br>
Input: 58</br>
Output: "LVIII"</br>
Explanation: C = 100, L = 50, XXX = 30 and III = 3.</br>

Example 5:</br>
Input: 1994</br>
Output: "MCMXCIV"</br>
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.</br>

### 017. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.</br>
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</br>

Example:</br>
Input: "23"</br>
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].</br>

Note:</br>
Although the above answer is in lexicographical order, your answer could be in any order you want.</br>

### 019. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.</br>

Example:</br>
Given linked list: 1->2->3->4->5, and n = 2.</br>
After removing the second node from the end, the linked list becomes 1->2->3->5.</br>

Note:</br>
Given n will always be valid.</br>

Follow up:</br>
Could you do this in one pass?</br>

### 022. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.</br>
For example, given n = 3, a solution set is:</br>
[</br>
  "((()))",</br>
  "(()())",</br>
  "(())()",</br>
  "()(())",</br>
  "()()()"</br>
]</br>

### 024. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.</br>

Example:</br>
Given 1->2->3->4, you should return the list as 2->1->4->3.</br>
Note:</br>
Your algorithm should use only constant extra space.</br>
You may not modify the values in the list's nodes, only nodes itself may be changed.</br>

### 029. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.</br>
Return the quotient after dividing dividend by divisor.</br>
The integer division should truncate toward zero.</br>

Example 1:</br>
Input: dividend = 10, divisor = 3</br>
Output: 3</br>

Example 2:</br>
Input: dividend = 7, divisor = -3</br>
Output: -2</br>

Note:</br>
Both dividend and divisor will be 32-bit signed integers.</br>
The divisor will never be 0.</br>
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.</br>

### 031. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.</br>
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).</br>
The replacement must be in-place and use only constant extra memory.</br>
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.</br>

1,2,3 → 1,3,2</br>
3,2,1 → 1,2,3</br>
1,1,5 → 1,5,1</br>

### 033. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</br>
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).</br>
You are given a target value to search. If found in the array return its index, otherwise return -1.</br>
You may assume no duplicate exists in the array.</br>
Your algorithm's runtime complexity must be in the order of O(log n).</br>

Example 1:</br>
Input: nums = [4,5,6,7,0,1,2], target = 0</br>
Output: 4</br>

Example 2:</br>
Input: nums = [4,5,6,7,0,1,2], target = 3</br>
Output: -1</br>

### 034. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.</br>
Your algorithm's runtime complexity must be in the order of O(log n).</br>
If the target is not found in the array, return [-1, -1].</br>

Example 1:</br>
Input: nums = [5,7,7,8,8,10], target = 8</br>
Output: [3,4]</br>

Example 2:</br>
Input: nums = [5,7,7,8,8,10], target = 6</br>
Output: [-1,-1]</br>

