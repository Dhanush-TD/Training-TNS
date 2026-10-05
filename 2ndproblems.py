

# 1. Two Sum – Hashing
# Given an integer array and a target value, find the indices of two elements whose sum equals the target.
# Example: [2, 7, 11, 15], target = 9 → [0, 1]

# 2. Longest Substring Without Repeating Characters – Sliding Window
# Given a string, find the length of the longest substring containing no duplicate characters.
# Example: "abcabcbb" → 3

# 3. Maximum Subarray Sum – Kadane's Algorithm
# Find the contiguous subarray having the maximum possible sum.
# Example: [-2,1,-3,4,-1,2,1,-5,4] → 6

# 4. Merge Overlapping Intervals – Sorting
# Given a collection of intervals, merge all overlapping intervals.
# Example: [[1,3],[2,6],[8,10],[9,12]] → [[1,6],[8,12]]

# 5. Detect a Cycle in a Linked List – Fast & Slow Pointers
# Determine whether a singly linked list contains a cycle. Try solving it with O(1) extra space.

# 6. Valid Parentheses – Stack
# Given a string containing (), {}, and [], determine whether the brackets are properly balanced.
# Example: "({[]})" → true

# 7. Binary Tree Level Order Traversal – BFS
# Given the root of a binary tree, return its nodes level by level.
# Example:

#     3
#    / \
#   9  20
#      / \
#     15  7
# Output: [[3], [9,20], [15,7]]

# 8. Lowest Common Ancestor of a Binary Tree
# Given a binary tree and two nodes p and q, find their lowest common ancestor.
# 9. Number of Islands – Graph/BFS/DFS
# Given a grid containing '1' (land) and '0' (water), count the number of distinct islands.
# Example:

# 1 1 0 0
# 1 0 0 1
# 0 0 1 1

# Output: 2

# 10.Longest Consecutive Sequence – Hashing
# Given an unsorted array, find the length of the longest sequence of consecutive integers. Try to solve it in O(n) time.
# Example: [100,4,200,1,3,2] → 4 (1,2,3,4)

# Please work on these codes and keep them in your laptop

# ================================
# Data Structure Questions in Python
# ================================

# 1. Two Sum – Hashing
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# 2. Longest Substring Without Repeating Characters – Sliding Window
def length_of_longest_substring(s):
    seen, left, max_len = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# 3. Maximum Subarray Sum – Kadane's Algorithm
def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# 4. Merge Overlapping Intervals – Sorting
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

# 5. Detect a Cycle in a Linked List – Fast & Slow Pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False

# 6. Valid Parentheses – Stack
def is_valid(s):
    stack, mapping = [], {')':'(', '}':'{', ']':'['}
    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack

# 7. Binary Tree Level Order Traversal – BFS
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def level_order(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

# 8. Lowest Common Ancestor of a Binary Tree
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right

# 9. Number of Islands – Graph/BFS/DFS
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r,c)
                count += 1
    return count

# 10. Longest Consecutive Sequence – Hashing
def longest_consecutive(nums):
    num_set, longest = set(nums), 0
    for num in num_set:
        if num-1 not in num_set:  # start of sequence
            length = 1
            while num+length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


print("1. Two Sum:", two_sum([2,7,11,15], 9))
print("2. Longest Substring:", length_of_longest_substring("abcabcbb"))
print("3. Max Subarray:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print("4. Merge Intervals:", merge([[1,3],[2,6],[8,10],[9,12]]))
print("6. Valid Parentheses:", is_valid("({[]})"))
grid = [["1","1","0","0"],["1","0","0","1"],["0","0","1","1"]]
print("9. Number of Islands:", num_islands(grid))
print("10. Longest Consecutive:", longest_consecutive([100,4,200,1,3,2]))