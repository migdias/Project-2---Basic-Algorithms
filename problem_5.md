# Problem 5: Autocomplete with Tries

In this problem, we need to perform a full search of all the nodes children in order to find all the suffixes, this means the time complexity is O(n), where n is the number of children of a specific node.

To collect the suffixes we use recursion, where it will recurse until it finds a word. once it does, it appends the specific suffix to a list.

The space complexity of finding suffixes is O(m), where m is the number of suffixes found, since we retur an array with it.