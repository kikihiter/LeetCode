# LeetCode
Some codes of mine on the leetcode.
Here will be a description of some questions.
## tag=easy
### 001. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:<br>
Given nums = [2, 7, 11, 15], target = 9,<br>

Because nums[0] + nums[1] = 2 + 7 = 9,<br>
return [0, 1].<br>

### 007. Reverse Integer
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
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.<br>

### 009. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.<br>

### 013. Roman to Integer
Given a roman numeral, convert it to an integer.<br>
Input is guaranteed to be within the range from 1 to 3999.<br>

Hit 1:<br>
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000<br>

Hit 2:<br>
Rules:<br>
* If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9<br>
* If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90<br>
* If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900<br>
 
### 014. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.<br>
 
### 020. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.<br>

### 021. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.<br>

Example:<br>
Input: 1->2->4, 1->3->4<br>
Output: 1->1->2->3->4->4<br>

### 026. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.<br>
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.<br>

Example 1:<br>
Given nums = [1,1,2],<br>
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.<br>
It doesn't matter what you leave beyond the returned length.<br>

Example 2:<br>
Given nums = [0,0,1,1,1,2,2,3,3,4],<br>
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.<br>
It doesn't matter what values are set beyond the returned length.<br>

Clarification:<br>
Confused why the returned value is an integer but your answer is an array?<br>
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.<br>

Internally you can think of this:<br>
// nums is passed in by reference. (i.e., without making a copy)<br>
int len = removeDuplicates(nums);<br>
// any modification to nums in your function would be known by the caller.<br>
// using the length returned by your function, it prints the first len elements.<br>
for (int i = 0; i < len; i++) {<br>
    print(nums[i]);<br>
}<br>

### 027. Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.<br>
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.<br>
The order of elements can be changed. It doesn't matter what you leave beyond the new length.<br>

Example 1:<br>
Given nums = [3,2,2,3], val = 3,<br>
Your function should return length = 2, with the first two elements of nums being 2.<br>
It doesn't matter what you leave beyond the returned length.<br>

Example 2:<br>
Given nums = [0,1,2,2,3,0,4,2], val = 2,<br>
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.<br>
Note that the order of those five elements can be arbitrary.<br>
It doesn't matter what values are set beyond the returned length.<br>

Clarification:<br>
Confused why the returned value is an integer but your answer is an array?<br>
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.<br>
Internally you can think of this:<br>
// nums is passed in by reference. (i.e., without making a copy)<br>
int len = removeElement(nums, val);<br>
// any modification to nums in your function would be known by the caller.<br>
// using the length returned by your function, it prints the first len elements.<br>
for (int i = 0; i < len; i++) {<br>
    print(nums[i]);<br>
}<br>

### 028. Implement strStr()
Implement strStr().<br>
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.<br>

Example 1:<br>
Input: haystack = "hello", needle = "ll"<br>
Output: 2<br>

Example 2:<br>
Input: haystack = "aaaaa", needle = "bba"<br>
Output: -1<br>

Clarification:<br>
What should we return when needle is an empty string? This is a great question to ask during an interview.<br>
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().<br>

### 035. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.<br>
You may assume no duplicates in the array.<br>

Example 1:<br>
Input: [1,3,5,6], 5<br>
Output: 2<br>

Example 2:<br>
Input: [1,3,5,6], 2<br>
Output: 1<br>

Example 3:<br>
Input: [1,3,5,6], 7<br>
Output: 4<br>

Example 4:<br>
Input: [1,3,5,6], 0<br>
Output: 0<br>

### 038. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:<br>
1.     1<br>
2.     11<br>
3.     21<br>
4.     1211<br>
5.     111221<br>
1 is read off as "one 1" or 11.<br>
11 is read off as "two 1s" or 21.<br>
21 is read off as "one 2, then one 1" or 1211.<br>
Given an integer n, generate the nth term of the count-and-say sequence.<br>
Note: Each term of the sequence of integers will be represented as a string.<br>

Example 1:<br>
Input: 1<br>
Output: "1"<br>

Example 2:<br>
Input: 4<br>
Output: "1211"<br>
