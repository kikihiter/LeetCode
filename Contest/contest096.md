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
