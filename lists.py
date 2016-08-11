list_1=[]
list_2=list()

print(list_1)
print(list_2)

print(list_1==list_2)

even=[2,4,6,8]
even.sort(reverse=True)
print(even)

num=list("2583 6852 352")
print(num)

even=[2,4,6,8]
odd=[1,3,5,7,9]

numbers=[even,odd]
print(numbers)
numbers.sort()
print(numbers)
for x in numbers:
    print(x)
    for y in x:
        print(y)


l=[1,2,3,4]
print(l)
l.append(5)
l.append([5])
l.append([5,6])
print(l)