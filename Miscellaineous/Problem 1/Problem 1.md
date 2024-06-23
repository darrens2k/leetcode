Given an array, you have to select some elements from it such that the sum of the selected elements should be the minimum possible. You have to select p subarrays of size 1, q subarrays of size 2, and r subarrays of size 3. All these selected subarrays should be disjoint. Return the minimum sum of the selected elements.

Example
```
For arr = [3, 1, 0, 5, 1, 6, 5, -1, -100], p = 1, q = 1, r = 1, the output should be solution(arr, p, q, r) = -96. 

Sum of elements will be minimum when these subarrays are selected: [1], [-1, -100] and [3, 1, 0], sum = 1 + (-1) + (-100) + 3 + 1 + 0 = -96.
```
Here if we select any other element, resultant sum will be more than -96. For eg, if we select [3], [1, 0], [5, 1, 6], resultant sum will be 3 + 1 + 0 + 5 + 1 + 6 = 16 which is more than -96.

Guaranteed constraints:
* 1 ≤ arr.length ≤ 100,
* -10^5 ≤ arr[i] ≤ 10^5.
* 0 ≤ p, q, r ≤ 30,
* p + 2q + 3r ≤ arr.length