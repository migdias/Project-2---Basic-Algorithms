# Problem 7: Request Routing in a Web Server with a Trie

## Time complexity

##### Insert method
The insert method will mean that we will have to travel down the tree at most r times where r is the amount of routes of the path. So the complexity is **O(r)**

##### Find method
The find method has to go through the trie at most r times (worst case). The complexity will be at most **O(r)** where r is the amount of routes of the path given.

##### add_handler method
The add_handler just runs a **O(1)** operation to check if the path is valid, and then runs the insert method which is **O(r)**

##### lookup method
It calls the find method which is **O(r)**, and then if it exists, return. There is two other comparisons that simplify to **O(1)**. The overall time complexity of this method is then **O(r)**.

##### split_path method
The time complexity of this one is **O(r)** since it has to go through the whole string in search for the '/' and split it. There are two other pop operations and a comparison which are **O(1)**. This simplifies to **O(r)** 

- The overall time complexity is then `4O(r) -> O(r)`, where r is the amount of routes in the path. Note: The complexity is mainly dominated by the inser and  find operation. 

## Space Complexity

##### Trie Nodes
Storing the nodes of the trie is proportional to the total length of all routes in the trie, which is **O(k)** where k is the total amount of routes stored.

##### Route Strings
Storing the route strings is proportional to the total length of all routes in the trie, which is mainly **O(m)** where m the the total characters stored.

- The overall space complexity is then **O(m + k)**

