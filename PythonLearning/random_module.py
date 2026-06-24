import random
names = input("enter everyone's name separated by comma:")
name_list = names.split(",")
i = random.randint(0,len(name_list))
print(f"{name_list[i]} will pay the bill.")