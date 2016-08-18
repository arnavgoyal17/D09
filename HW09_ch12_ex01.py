#!/usr/bin/env python
# HW09_ch12_ex01
# (1) Write a function called most_frequent that takes a string and prints the
#     chars in decreasing order of frequency. (compare and print in lowercase)
# Ex. >>> most_frequent("aaAbcc")
#     a
#     c
#     b
###############################################################################
# Imports


# Body
def most_frequent(s):
    
    # convert the string to lowercase
    s = s.lower()

    # define a dict that will hold the counts
    dictCounts = {}

    sList = s.split()
    for items in sList:
      for chars in items:
        dictCounts[chars] = dictCounts.get(chars, 0) + 1

    output = sorted(sorted(dictCounts), key=dictCounts.__getitem__, reverse=True)
    for values in output:
      print(values)


###############################################################################
def main():   # DO NOT CHANGE BELOW
    print("Example 1:")
    most_frequent("abcdefghijklmnopqrstuvwxyz")
    print("\nExample 2:")
    most_frequent("The quick brown fox jumps over the lazy dog")
    print("\nExample 3:")
    most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                  "sed do eiusmod tempor incididunt ut labore et dolore magna "
                  "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                  "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
                  "uis aute irure dolor in reprehenderit in voluptate velit "
                  "esse cillum dolore eu fugiat nulla pariatur. Excepteur "
                  "sint occaecat cupidatat non proident, sunt in culpa qui "
                  "officia deserunt mollit anim id est laborum.")
    print("\nExample 4:")
    most_frequent("Squdgy fez, blank jimp crwth vox!")

if __name__ == '__main__':
    main()
