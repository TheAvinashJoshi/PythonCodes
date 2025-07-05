def printMyName():
    print("Avinash Joshi")

printMyName()

# lastName="joshi" is default param that says if you dont pass then it will take joshi
def printMyNameCustom(firstName, lastName="joshi"):
    return f"name is {firstName} {lastName}"

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
# print(printMyNameCustom(firstName, lastName))

# by default python methods return None

# specify argument name while passing
# print(printMyNameCustom(firstName=firstName, lastName=lastName))
print(printMyNameCustom(firstName)) # not passed takes Joshi
print(printMyNameCustom(firstName, lastName)) # takes whatever passed

# optional params should come after required

# xargs
def show(*numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number) 
show(1,2,3,4,5) # iterable list it will make


