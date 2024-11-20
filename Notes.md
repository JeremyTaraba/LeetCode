# Common ways to solve coding problems by data type

## Arrays and Strings
Could be solved by brute force. When you think of brute force you should think of recursion, dfs, and backtracking(very useful). Only use brute force when you need all possible solutions. In java and other programming languages you can't manipulate strings and will need to create a copy or using a string builder.

These can also be solved using a map/dictionary. 

Other common ways to solve array problems are to use two pointers (left and right pointers), binary search, sliding window, or even prefix sums (compute sum going left to right). 

Backtracking - used with arrays, especially if you need every combination. Different types like recursive (most common) or iterative using stacks or queues. Can also be used to eliminate unwanted results/paths. When it comes to arrays, you need to pass the index in as a parameter to the recursive call

Another way to solve array problems is a decision tree/trie:
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    

## Linked list 
These problems are commonly solved with recursion, recursion is usually the simplest but not the best. iteration also works although might be harder to code. Additionally, a lot of these problems can also be solved by using a runner and current pointer where the runner goes a set number of spaces ahead of current. 

Getting the size of the list can help but will take O(n) time. Can also use a slow/fast pointer to find the middle of the list without knowing the size. When the fast runner hits the end of the list the slow runner is in the middle.

## Stacks and Queues 
No common way of solving these problems just know when to use them such as using queue when you need to keep track and return oldest data or stack when you need to get most recent data.

## MinHeap and MaxHeap
Very useful for finding the minimum or maximum values in O(1) time. The storage of the heap will not be in order but the min will always be at the top. In Python there is no MaxHeap so will use a minHeap and make all values negative to make it work like a MaxHeap


## Trees and Graphs and Tries
Usually we use dfs for searching because bfs is harder to implement but bfs is good if we want to search for the closest connection to something else. Unlike dfs, bfs is better done not recursively and instead iteratively using a queue. Bidirectional search is used to find the shortest path from a source to destination. It is basically 2 bfs one on the source and another on the destination until they collide. 

For Graphs. Need to have a Visit set so you know which nodes you have already visited so you don't go in circles. May need to nested loop to call the dfs function.

## Backtracking
Used if need all combinations of something. Horrible runtime since computing every possibility. Use a dfs for these and go down different paths where you either choose or don't choose an option. Usually you append the answer into a list that is global or can also pass it in as a parameter. 
EX: 
answerList = []
    def backtracking(index, cur, total):  
        if total == target:
            answerList.append(cur.copy())
            return
        if index == len(candidates) or total > target:
            return

        cur.append(candidates[index])
        backtracking(index, cur, total+candidates[index])
        cur.pop()
        backtracking(index+1, cur, total)

    backtracking(0,[], 0)


## Dynamic Programming
Usually problems where you either choose to take a path or to not take a path, can sometimes be confused with combinations.
Commonly solved using a dp[] array that stores past results (memorization). Typically using a bottom up approach is easier to understand and implement but sometimes a top down approach is better. Sometimes you don't even need the whole array, you just need the last computed values so can just use 2 variables to keep track of this. Can also use a set or map instead of using an array if need be. Usually At least O(n^2) if not worse runtime.

## Additional Notes:
- Sum of first n natural numbers (1,2,...n) can be found by doing n*(n+1)/2
- For reversing strings, can use a stack for this since it already reverses it instead of trying to reverse it in place which doesn't work in Java or making a new string which is confusing
- Python has a built in TreeNode data type that gives you value, left, and right. Can set left and right to another TreeNode to create a tree


