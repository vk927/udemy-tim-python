
menu=[]
menu.append(["egg","spam","bacon"])
menu.append(["egg","chicken","spam"])
menu.append(["fish","shrimp","veg"])
menu.append(["potato","chips","ranch"])
menu.append(["lamb","tomato","spam"])
menu.append(["green","chicken","beans"])

#print(menu)

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)