# Problem 3: Rearrange Array Digits

For this problem since an O(nlog n) was the expected complexity, the mergesort was used. The original merged sort from class was used without change because the resulting sorted array could be technically processed to get the two numbers.

The idea is that after the array is sorted, to start building the numbers from the end of the array (largest numbers). The sum of two numbers will be as large as possible when the first digits in the numbers are as large as possible. Therefore, we start building both numbers from the end of the sorted list with a step of two (backwards). This will allow both numbers to be as bigger as they can be.

###### Example: Sorted Array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
- Number 1: start on last index and fills with step -2 -> [9] -> [9, 7] -> [9, 7, 5] -> ... -> to_string() -> 97531
- Number 2: start on second to last index and fills with step -2 -> [8] -> [8, 6] -> ... -> to_string() -> 86420

The complexity of this solution is dominated by the merge sort which is O(n log n) + processing of the sorted array O(n/2) + O(n/2), which is still O(n log n)

Since when sorting we create a merged array to store the sorted elements during merging process, the space complexity is O(n) where n is the original length of the array. In the case of the mergesort, its recursively splitting the input array at each level, and therefore will be a max slices of O(log n). Furthermore, for each recursion we need to hold left and right slices which will be complexity of O(n). Putting it all together we have O(n) + O(n log n) -> O(n).