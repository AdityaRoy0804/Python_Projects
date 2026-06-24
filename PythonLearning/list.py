# list = [1,2,3,4,5]
# print(list)
# print(list[2])                 #positive indexing
# print(list[-4])                #negative indexing

# #list slicing
# print(list[1:3])
# print(list[:])                  #default values 

# # sorting  and  reversing the list
# list = [5,2,3,1,4]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# print(min(list))                  # returns the smallest value of element in the list
# print(max(list))                  # returns the largest value of element is list

# #mutating the element is the list
# list = [1,2,3,4,5]
# list[1] = 7                   #individual element
# list[2:5] = [8,8,8]
# # list[2:5] = []             #removes the element from index 2 to range 5
# print(list)

# # remove and pop
# list = [1,2,3,4,1]
# list.remove(1)                    # removes the element at their firdt appearance 
# print(list)
# list.pop(2)                       # removes the element from the given index no
# print(list)
# list.pop()                        # default argument is size - 1
# print(list)

# nested list 
num = [1,10,15,[20,10,-15],17,0]
print(len(num))
print(num[3])
print(num[3][1])               #accessing the elemnts of nested list 
print(num[3][0:2])
print(num[3][0:2:2])
