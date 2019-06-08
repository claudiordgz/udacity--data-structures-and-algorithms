# Active Directory

Searching in a list of lists has the worst complexity of `O(n^2)`. Let's break down groups into `g` and users into `u`, searching in all groups is unavoidable, that means we need `O(g)`, but we can optimize searching for a specific user. 

We could improve this by using Binary Search. Binary Search is useful for searching take `O(log(n))` elements in the worst case. The challenge is that sorted items are necessary to achieve this, sorting first would be `O((n)log(n))` worst case complexity versus a linear search of `O(n)`. 

To improve this, we can insert in order by using a Binary Search Tree, which still has `O(n)`. 

We would need to figure out what are our requirements. For a large company with a large number of users, fast lookup might be necessary, but for a small company in the tens with or a medium company with high turnover, quick insertion and deletion might more important.
