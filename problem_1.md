# Problem 1: Square Root of an Integer

Is is given that we only need to calculate the floor of the square root of a number `n`. Since a*a = b, where a is the perfect square root of the b, we only need to find the where `floor(a) * floor(a) <= b and floor(a+1) * floor(a+1) >= b`. Therefore the algorithm, in order of be complexity log(n) need to cut by 2, each iteration and so, given a number `b`, we "cut" on the middle by a = b // 2, depending whether the result of a * a is bigger or smaller than b, we go to either size as a kind of binary search.

By keeping track of the start and end intervals we can achieve a complexity of O(log(n)), since it is dominated by the binary search where the search space reduced by half on each iteration.

The space complexity of this O(1) since we do not store anything in array format. We store temporary variables that are overwritten as iterations go.