# Given two arrays of strings a1 and a2 return a sorted array r
# in lexicographical order of the strings of a1 which are substrings of strings of a2.
#
# Example 1:
# a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# Example 2:
# a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []
#
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.

# SOLUTION:

def in_array(array1, array2):
    array3 = []
    for i in array1:
        j = 0
        while j in range(len(array2)) and not i in array3:
            if i in array2[j]:
                array3.append(i)
            j += 1
    array3.sort()
    return array3
