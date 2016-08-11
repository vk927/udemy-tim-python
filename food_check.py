food=["egg","chicken","lamb","beef","shrimp"]

reaction=''
for i in food:
    if i=="beef":
        reaction="no"
        break
#here also we can keep else, this else is for whole for loop, if for loop enters atleast once if group
# then else won't execute
#else:
#    print("I can eat")
if reaction=="no":
    print("Sorry! I can't eat")
else:
    print("I can eat")