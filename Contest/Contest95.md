# Contest 95
### 876. Middle of the Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.</br>
If there are two middle nodes, return the second middle node.</br>

Example 1:</br>
Input: [1,2,3,4,5]</br>
Output: Node 3 from this list (Serialization: [3,4,5])</br>
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).</br>
Note that we returned a ListNode object ans, such that:</br>
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.</br>

Example 2:</br>
Input: [1,2,3,4,5,6]</br>
Output: Node 4 from this list (Serialization: [4,5,6])</br>
Since the list has two middle nodes with values 3 and 4, we return the second one.</br>

Note:</br>
The number of nodes in the given list will be between 1 and 100.</br>

### 877. Stone Game
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].</br>
The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.</br>
Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.</br>
Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.</br>

Example 1:</br>
Input: [5,3,4,5]</br>
Output: true</br>
Explanation: </br></br>
Alex starts first, and can only take the first 5 or the last 5.</br>
Say he takes the first 5, so that the row becomes [3, 4, 5].</br>
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.</br>
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.</br>
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.</br>
 
Note:</br>
2 <= piles.length <= 500</br>
piles.length is even.</br>
1 <= piles[i] <= 500</br>
sum(piles) is odd.</br>

### 878. Nth Magical Number
A positive integer is magical if it is divisible by either A or B.</br>
Return the N-th magical number. Since the answer may be very large, return it modulo 10^9 + 7.</br>

Example 1:</br>
Input: N = 1, A = 2, B = 3</br>
Output: 2</br>

Example 2:</br>
Input: N = 4, A = 2, B = 3</br>
Output: 6</br>

Example 3:</br>
Input: N = 5, A = 2, B = 4</br>
Output: 10</br>

Example 4:</br>
Input: N = 3, A = 6, B = 4</br>
Output: 8</br>
 
Note:</br>
1 <= N <= 10^9</br>
2 <= A <= 40000</br>
2 <= B <= 40000</br>
