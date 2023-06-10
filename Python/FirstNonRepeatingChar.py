# Write a function named first_non_repeating_letter that takes a string input,
# and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character,
# but the function should return the correct case for the initial letter. For example,
# the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

# SOLUTION:

def first_non_repeating_letter(s):
    sl = s.lower()
    for i in range(len(sl)):
        if sl.count(sl[i]) == 1:
            return s[i]
    return ''


def first_non_repeating_letter_alt(s):  # My first solution
    slist = list(s.lower())
    i = 0
    while i < len(slist):
        j = 0
        flag = True
        while j < len(slist) and flag:
            if slist[i] == slist[j] and not i == j:
                flag = False
            j += 1
        if flag:
            return s[i]
        i += 1
    return ''
