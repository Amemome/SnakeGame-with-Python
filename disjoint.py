from collections import deque

a = deque()


a.append(list(tuple([0,0])))
a.append(list(tuple([1,0])))
a.append(list(tuple([2,0])))

if list([0,0]) in a: print("wow")