"""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""

# Get character fromGet the characters from position 2 to position 5 (not included):
b = "Hello, World"
print(b[2:5])


# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):
print(b[:5])

# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

print(b[-5:-2])



