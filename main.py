"""
Problem 5: Merge Two Lists (25 marks)
Write a Python function “merge_lists(lst1, lst2)” that takes two lists as input
and returns a new list that contains all elements from both lists, sorted in ascending order.

Example:
print(merge_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_lists([10, 20, 30], [15, 25, 35]))  # [10, 15, 20, 25, 30, 35]
"""


def MergeList(lst1, lst2):
    # write code here
    return sorted(lst1 + lst2)


if __name__ == '__main__':
    l1 = [2, 4, 6, 8, 10]
    l2 = [1, 3, 5, 7, 9]
    result = MergeList(l1, l2)
    print(result)
