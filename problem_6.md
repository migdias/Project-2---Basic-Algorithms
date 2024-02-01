# Problem 6: Unsorted Integer Array

In this specific problem, sorting is not really necessary and it only increases the time complexity.

We can very easily solve this problem in O(n) (linear time), by going through each element on the list of integers and keeping the minimum and maximum at each iteration.
Since we only need to traverse the list one, the time complexity is always O(n). If we had a sorted array, it would be O(1).

The space complexity is O(1) because we are not storing any big variables at each iteration. Each iteration we check if the new element is bigger or smaller than the current min and max and change them if necessary.