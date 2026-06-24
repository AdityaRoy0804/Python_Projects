# manipulating tuple
tuple1 = (12,6,-8,"Aditya",True)
# print(tuple1)
# print(tuple1[1])               #indexing
# print(tuple1[-2])              # negative indexing
# print(tuple1[1:])              # slicing
# print(tuple1[::2])

# nesting  and concatenation of tuple
tuple2 = (45,67,90)
tuple3 = (tuple1,tuple2)
print(tuple3)
tuple3 = tuple2 + tuple1
print(tuple3)



