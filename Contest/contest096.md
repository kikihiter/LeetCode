# Contest96
### 887. Projection Area of 3D Shapes
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.</br>
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).</br>
Now we view the projection of these cubes onto the xy, yz, and zx planes.</br>
A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. </br>
Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.</br>
Return the total area of all three projections.</br>

Example 1:</br>
Input: [[2]]</br>
Output: 5</br>

Example 2:</br>
Input: [[1,2],[3,4]]</br>
Output: 17</br>
Explanation: </br>
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.</br>

Example 3:</br>
Input: [[1,0],[0,2]]</br>
Output: 8</br>

Example 4:</br>
Input: [[1,1,1],[1,0,1],[1,1,1]]</br>
Output: 14</br>

Example 5:</br>
Input: [[2,2,2],[2,1,2],[2,2,2]]</br>
Output: 21</br>

Note:</br>
1 <= grid.length = grid[0].length <= 50</br>
0 <= grid[i][j] <= 50</br>

### 885. Boats to Save People
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.</br>
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.</br>
Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)</br>

Example 1:</br>
Input: people = [1,2], limit = 3</br>
Output: 1</br>
Explanation: 1 boat (1, 2)</br>

Example 2:</br>
Input: people = [3,2,2,1], limit = 3</br>
Output: 3</br>
Explanation: 3 boats (1, 2), (2) and (3)</br>

Example 3:</br>
Input: people = [3,5,3,4], limit = 5</br>
Output: 4</br>
Explanation: 4 boats (3), (3), (4), (5)</br>

Note:</br>
1 <= people.length <= 50000</br>
1 <= people[i] <= limit <= 30000</br>

### 884. Decoded String at Index
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:</br>
If the character read is a letter, that letter is written onto the tape.</br>
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.</br>
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.</br>

Example 1:</br>
Input: S = "leet2code3", K = 10</br>
Output: "o"</br>
Explanation: </br>
The decoded string is "leetleetcodeleetleetcodeleetleetcode".</br>
The 10th letter in the string is "o".</br>

Example 2:</br>
Input: S = "ha22", K = 5</br>
Output: "h"</br>
Explanation: </br>
The decoded string is "hahahaha".  The 5th letter is "h".</br>

Example 3:</br>
Input: S = "a2345678999999999999999", K = 1</br>
Output: "a"</br>
Explanation: </br>
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".</br>
 
Note:</br>
2 <= S.length <= 100</br>
S will only contain lowercase letters and digits 2 through 9.</br>
S starts with a letter.</br>
1 <= K <= 10^9</br>
The decoded string is guaranteed to have less than 2^63 letters.</br>
