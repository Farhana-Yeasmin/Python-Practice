#SORT LIST ALPHANUMERICALLY 
"""
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() 
thislist.sort(reverse=True) #decending sort
print(thislist)

#Case Insensitive Sort:
"""
By default the sort() method is case sensitive, resulting in all capital letters being sorter before lower case letters.
"""
#Case sensitive sorting give you an unexpected result so using str.lower function for case insensitive function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort( key= str.lower)
print("newlist:")
thislist.reverse()
print(thislist)
