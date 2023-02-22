 #LOOPING USING LIST COMPREHENSION:
#  List comprehension offers the shortest syntax for looping through list:
thislist = ["New","Year","Eve"]
[print(x) for x in thislist]


# remove fruits those have "a" in their name and added it into a new list
fruits = ["apple","abanana","cherry","kiwi"]
newList = []

for x in fruits.copy():
    if "a" in x:
        newList.append(x)
        fruits.remove(x)
print(fruits)        
print(newList)        

# remove vowels from a string
text = "whoops"
textlist = list(text)
for char in textlist[:]:     
    if char.lower() in 'aeiou':
        textlist.remove(char)

print(textlist)       