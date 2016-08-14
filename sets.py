even=set()
ev={}
even.add("hi")
print(even)
#ev.add("hi")


#to stoop adding items to set use frozenset
fset=frozenset(even)

print("-----------------",fset)

fx=frozenset("rock")
print(fx)
print(sorted(fx))

lset=set("---------------hi hello")

print(lset)

pd=set(range(10))
print(pd)

od =set(range(0,10,2))
print(od)

od.remove(2)
#od.remove(20)
od.discard(20)

print(od)

if od.issubset(pd):
    print("hello")

if pd.issuperset(od):
    print("bye")


dc=set([1,22,3])
print(dc)

mar=set([1,4,5])
print(dc-mar)
print(mar-dc)
print(mar & dc) # print (mar.intersection(dc))
print(mar.union(dc))
print(dc.symmetric_difference(mar))

