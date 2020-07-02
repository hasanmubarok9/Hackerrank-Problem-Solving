# Given an array of equal-length strings, 
# you'd like to know if it's possible to rearrange 
# the order of the elements in such a way that 
# each consecutive pair of strings differ by exactly 
# one character. Return true if it's possible, and false if not.


# For inputArray = ["aba", "bbb", "bab"], the output should be
# stringsRearrangement(inputArray) = false.
# There are 6 possible arrangements for these strings:

# ["aba", "bbb", "bab"]
# ["aba", "bab", "bbb"]
# ["bbb", "aba", "bab"]
# ["bbb", "bab", "aba"]
# ["bab", "bbb", "aba"]
# ["bab", "aba", "bbb"]
# None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

# For inputArray = ["ab", "bb", "aa"], the output should be
# stringsRearrangement(inputArray) = true.

# It's possible to arrange these strings in a way that 
# each consecutive pair of strings differ by 1 character 
# (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def stringsRearrangement(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False
