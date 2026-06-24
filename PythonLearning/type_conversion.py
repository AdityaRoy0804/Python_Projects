
# length = len("Aditya Roy")
# #print("Your name has "+length+" characters ")           #shows type error since integer cannot be added with strings 
# print("Your name has "+str(length)+" characters")        # integer being converted to string
# print(type(length))
# new_legth = str(length)
# print(type(new_legth))


# print("10" + "10")          
# print(10 + 10)           #direct integer addition
# print(int("10") + int("10"))             #string converted to integer and added
# print(10 + int("Aditya"))                     #shows value error 


# a = input("enter value for a:")          #return tpyr of input is string 
# b = input("enter value for b:")
# sum = a+b                                #string concatenation
# print(sum)
# sum = int(a) + int(b)                    #type conversion to int and then addition2

# print(sum)


#sum of the digits of the number

a = input("enter a tow digits number:")
sum = int(a[0]) + int(a[1])
print(sum)