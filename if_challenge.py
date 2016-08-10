
def tour_check(age):
    if 18<=age<=30:
        print("Welcome to Holiday Tour")
    elif age<18:
        print("Please come back after",18-age,"years! you should be 18 years old for eligibility")
    else:
        print("Sorry you might have tried ",age-30,"years back! we are not eligible for holiday tour anymore")


name=input("Enter your name ...")
age=int(input(name +"  enter your age ..."))

tour_check(age)


