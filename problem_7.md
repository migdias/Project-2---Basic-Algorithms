# Problem 7: Request Routing in a Web Server with a Trie

In this problem, the complexity is all about adding paths to the Trie, and looking them up. Splitting the path also requires checking the whole path. 

- Insertion is O(n) with n as the number of elements since we have to go through each part of the path. 
- Lookup is also O(n) since we need to grab the element to check if there is a handler. We have to go in worst case to the nth element.
- Splitting the path is again O(n) where n is the number of parts in the path.

In terms of space complexity, the space required in total is the space to:

- Store TrieNodes which is O(k) where k is the number of nodes
- Store the path for split operation (which is temporary).

In summary, the Time Complexity is O(n) and the Space Complexity is O(k).

