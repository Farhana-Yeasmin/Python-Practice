"""
OrderedDict is dictionary subclass which remembers the order in which the entries were done
"""

import collections

d = collections.OrderedDict()
d[1] = 'F'
d[2] = 'a'
d[3] = 'r'
d[4] = 'h'

d[1]='b'
print(d)