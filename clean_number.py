number="123,456,890"
newNum=""
for i in number:
    if i in "01234567890":
        newNum=newNum+i

print("the cleaned number is",int(newNum))
