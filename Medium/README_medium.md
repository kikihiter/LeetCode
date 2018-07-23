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

