list=["milk","pasta","spam","eggs","bread","rice"]
for i in list:
    if i=="spam":
        print("Don't buy this ",i)
        continue
    print("Buy this item",i)