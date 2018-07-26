# LeetCode
Some codes of mine on the leetcode.
Here will be a description of some questions.
## tag=easy
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
