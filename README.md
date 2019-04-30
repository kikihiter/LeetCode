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
1.     1
2.     11
3.     21
4.     1211
5.     111221
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

### 053. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.<br>

Example:<br>
Input: [-2,1,-3,4,-1,2,1,-5,4],<br>
Output: 6<br>
Explanation: [4,-1,2,1] has the largest sum = 6.<br>
Follow up:<br>
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.<br>

### 058. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.<br>
If the last word does not exist, return 0.<br>
Note: A word is defined as a character sequence consists of non-space characters only.<br>

Example:<br>
Input: "Hello World"<br>
Output: 5<br>

### 066. Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.<br>
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.<br>
You may assume the integer does not contain any leading zero, except the number 0 itself.<br>

Example 1:<br>
Input: [1,2,3]<br>
Output: [1,2,4]<br>
Explanation: The array represents the integer 123.<br>

Example 2:<br>
Input: [4,3,2,1]<br>
Output: [4,3,2,2]<br>
Explanation: The array represents the integer 4321.<br>

### 067. Add Binary
Given two binary strings, return their sum (also a binary string).<br>
The input strings are both non-empty and contains only characters 1 or 0.<br>

Example 1:<br>
Input: a = "11", b = "1"<br>
Output: "100"<br>

Example 2:<br>
Input: a = "1010", b = "1011"<br>
Output: "10101"<br>

### 069. Sqrt(x)
Implement int sqrt(int x).<br>
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.<br>
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.<br>

Example 1:<br>
Input: 4
Output: 2<br>

Example 2:<br>
Input: 8
Output: 2<br>

Explanation: The square root of 8 is 2.82842..., and since <br>
             the decimal part is truncated, 2 is returned.<br>
             
### 070. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.<br>
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?<br>
Note: Given n will be a positive integer.<br>

Example 1:<br>
Input: 2
Output: 2<br>
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step<br>
2. 2 steps<br>

Example 2:<br>
Input: 3
Output: 3<br>
Explanation: There are three ways to climb to the top.<br>
1. 1 step + 1 step + 1 step<br>
2. 1 step + 2 steps<br>
3. 2 steps + 1 step<br>

### 083. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.<br>

Example 1:<br>
Input: 1->1->2
Output: 1->2<br>

Example 2:<br>
Input: 1->1->2->3->3
Output: 1->2->3<br>

### 088. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.<br>

Note:<br>
The number of elements initialized in nums1 and nums2 are m and n respectively.<br>
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.<br>

Example:<br>
Input:<br>
nums1 = [1,2,3,0,0,0], m = 3<br>
nums2 = [2,5,6],       n = 3<br>
Output: [1,2,2,3,5,6]<br>

### 100. Same Tree
Given two binary trees, write a function to check if they are the same or not.<br>
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.<br>

Example 1:<br>

Input:     1         1<br>
          / \       / \
         2   3     2   3<br>

        [1,2,3],   [1,2,3]<br>
Output: true<br>

Example 2:<br>

Input:     1         1<br>
          /           \
         2             2<br>

        [1,2],     [1,null,2]<br>
Output: false<br>

Example 3:<br>

Input:     1         1<br>
          / \       / \
         2   1     1   2<br>

        [1,2,1],   [1,1,2]<br>
Output: false<br>

### 104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.<br>
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.<br>
Note: A leaf is a node with no children.<br>
Example:<br>
Given binary tree [3,9,20,null,null,15,7],<br>
    3<br>
   / \<br>
  9  20<br>
    /  \<br>
   15   7<br>
return its depth = 3.<br>
