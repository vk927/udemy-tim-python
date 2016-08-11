num="1,2,3,3,4"
x=''
for c in num:
    if c in "0123456789":
        x=x+c

print("trimmed number is ", x)

for x in ['a','hi','hello','bye']:
    print (x)


# skipping 5 elements while looping through a set of elements
for i in range (0,100,5):
    print("i is ",i)

#multiplication tables from 1 to 10
for i in range (1,11):
    for j in range (1,11):
        print(i,"times",j,"=",i*j)
    print("=====================")