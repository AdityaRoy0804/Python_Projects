height = input("Enter everyones height(in metre) separated by commas(,):")
height_list = height.split(",")
count = 0
for height in height_list :
    count = count + 1
for i in range(count) :
    height_list[i] = int(height_list[i])
total = 0
for i in height_list:
    total = total + i
avg = round(total/count)
print("The average height is :",avg)
    