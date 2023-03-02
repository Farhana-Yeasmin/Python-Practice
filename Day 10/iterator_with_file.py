import itertools

"""
Here using iterator is usefull because without loading the entire contents of that file into memory we can work like this
"""
with open('/home/farhana/Desktop/All Python/Python-Practice/demo.txt','r') as f:
    header = itertools.islice(f,3)

    print(header)
    for line in header:
        print(line, end='')