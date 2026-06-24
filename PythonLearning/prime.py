num = int(input("enter a number:"))
count = 0
if num < 0:
    count+=1
elif num == 0:
    count+=1
else:
    if num == 1:
        count+=1
    else:
        for i in range(2,num):
            if num%i==0:
                count+=1
if count == 0:
    print("prime number")
else:
    print("not a prime number")