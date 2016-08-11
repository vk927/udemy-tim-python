list=["hi","hello","good","morning","bye","welcome"]

my_itr= iter(list)

for i in range(len(list)):
    print(next(my_itr))

print("================================")
for i in list:
    print(i)