# Problem 5: Autocomplete with Tries

In this problem, we need to perform a full search of all the nodes children in order to find all the suffixes, this means the time complexity is O(n), where n is the number of children of a specific node.

To collect the suffixes we use recursion, where it will recurse until it finds a word. once it does, it appends the specific suffix to a list.

## Time complexity

The time complexity can be divided into the modules:
##### suffixes method: 
Recursively find the suffixes at any point in the tree means we have to visit every single child in the subtree. The complexity will then be **O(k)** where k is the number of child nodes.

##### insert method:
The insert method will mean that we will have to travel down the tree at most l times where l is the length of the word. So the complexity is **O(l)**

##### exists method:
The exists method worst case scenario is when the word to find is a prefix of an already existing word. We will need to traverse the trie for the length of the word, which will make it **O(l)** where l is the length of the word.

##### find method:
The find method is similar to exists method, but it returns the node even if its not a word. The complexity will be at most **O(l)** where l is the length of the prefix given.

- Overall, the time complexity will be `O(k) + 3O(l)`, which we can simplify to **O(k)**, since when the trie increases in size, it will be the most time consuming.


## Space Complexity

##### Trie
Saving the tree in memory means we need to hold n nodes in memory. The space complexity in this case is **O(n)** where n is the number of nodes in the Trie. It is not trivial to find the exact complexity based on number of characters, since different words can have the same nodes as prefixes.

##### Suffixes
The space complexity of finding suffixes is **O(m)**, where m is the number of suffixes found, since we retur an array with it. The worst case scenario is when we get the suffixes of root node, which will be the whole tree of **O(k)**, where k will be the amount of words existing in the trie.

- The overall space complexity is then `O(n) + O(k)` which simplifies to **O(n)** since is the most dominant one.