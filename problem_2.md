# Problem 2: Search in a Rotated Sorted Array

Since in this case we do not have a normal sorted array and we need to have O(log n), we need to perform a modified binary search which is O(log n) since the normal binary search is only for fully sorted arrays.

The way this works is that similarly to the binary search, it splits the array in the middle, and then checks which subarray is sorted. If an subarray is sorted, it means we can directly tell if the number can be there by comparing which first and last elements. We can do this to all cases. It's possible that the mid will be the pivot value and both subarrays will be sorted. In this case it will check where the number could be in (left or right) and performs the same modified binary search on it.

Since the only change from the normal binary search is one additional a few additional comparisons to check if sorted and if number could be in sorted, the time complexity is still O(log n).

The space complexity will be O(1) since we only store temporary variables needed for comparisons and the space is not dependent on the iterations.