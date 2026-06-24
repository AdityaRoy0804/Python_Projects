# manipulating sets
# set1 = {10,56,89,90,"Aditya",True}
# print(set1)

#union of sets 
set1 = {"ram","shyam","jenny"}
set2 = {"jenny","jiya","akash"}
set3 = {"ankur","pradeep"}
# print(set1.union(set2))                 #using union()
# print(set1|set2|set3)                   #using | operator
# print(set1.union(set2,set3))            #it can take multiple arguments as well
# print(set1.union(('Mohan','Jenny')))    #it can tupple as an argument
# print(set1.union(['Mohan','Jenny']))    #it can take list as an argument

#updating the sets
# set1.update(set2)
# print(set1)              # updates the elements in set1 with the elements of set2
# print(set2)
# set1|=set2
# print(set1)              # updating using operators
# set1.update(['Jenny','Mohan'])         #update can take list as well as tupple as an argument
# print(set1)

#intersection of sets
# print(set1.intersection(set2))
# print(set1.intersection(set2,set3))            #empty set
# print(set1&set2)                               # using & operator

# intersection_update()
# set1.intersection_update(set2)
# print(set1)                             # updates the element of the sets with its intersection with anothee sets

#difference of the sets 
# print(set1.difference(set2))
# print(set1-set2)                 #using operator -

#difference_update()
# set1.difference_update(set2)
# print(set1)


   
