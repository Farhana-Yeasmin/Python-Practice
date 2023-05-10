import re

"""
Compiling the pattern can help improve performance if you need to use the same pattern multiple times.
"""
pattern = re.compile("^[A-Z]+$")

"""
NOTE:
=> re.search() : This function returns a match object if it finds the first occurence of the pattern in the string. 
=> re.findall() : This function returns a list of non overlaping mathces of the pattern in the string
"""
# print(pattern.search("HELLLO"))

Nameage = '''
Janice is 22 and Theon is 25
Gabriel is 44 and Joey is 56
'''

ages = re.findall('\d{1,3}',Nameage)
# print(ages)


"""
NOTE:
=> finditer() : This function return the index of all matches of a pattern
=> span(): Only return the index of first occurence from a string 
"""
# Findind index
str = "we need to inform him with the latest information"

for i in re.finditer("inform", str):
    loctup = i.span()
    # print(loctup)

# here SPAN() return the index of first occurence
s = re.search("inform",str)
if s:
    loctup = s.span()
    # print(loctup)

str = "Sat, hat, mat, pat"
matcherRegex = "[Shmp]at"
allstr = re.findall(matcherRegex,str)

# print(allstr)

"""
NOTE:
Syntax of sub(): re.sub(pattern, repl, string, count=0, flags=0)
=> pattern -> A string representing the regular expression pattern to search for
=> repl -> representing the replacement for each matched 
=> string -> input string
/*
input_str = "I have an apple, he has an apple, she has an apple, we all have apples."
output_str = re.sub("apple", "orange", input_str)
*/
"""

#  SUB(): Replace a perticular matcher string
food = 'hat rat mat pat'
matcherRegex = "[r]at"
regex = re.compile(matcherRegex)

food = regex.sub("food",food)

print(food)

