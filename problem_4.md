# Problem 4: Dutch National Flag Problem

In this case, we know that zeroes should always go to the beginning of the list and twos should go to the end. We dont really need to care about the ones because they would be sorted automatically.

We keep track of the positions where we can put the next zero and next 2.

Basically for every element, we check if its zero or two. If it is zero, we exchange the zero value with the next available position after the last zero ( in the beginning of the list). The same logic applies for the two, but the next available position will be backwards. 

Since we only traverse the list once, the time complexity is O(n).

The space complexity is O(1) since we exchange the values in place.