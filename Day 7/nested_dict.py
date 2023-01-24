# A dictionary can contain dictionaries, this is called nested dictionaries.
#  Here are 3 dict create in a single dict()

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# x=child1 , y = {"name": "emil","year","2004"}
# Acess nested dict with indexing
for x , y in myfamily.items():
    for val in y:
        print(y[val])

# Another way to access nested dic():
for x , y in myfamily.items():
    for key,val in y.items():
        print(key, " ", val)        
    # print(x, " ")


# print(myfamily["child1"]["name"])


# for i in myfamily.items():