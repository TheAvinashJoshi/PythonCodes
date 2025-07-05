for number in range(10):
    print(number)

# prints stars
print("printing stars")
for number in range(10):
    print((number+1) * "*")

for number in range(1,11):
    print(number)

# in range first argument is from where to start iterator, second is to which it should iterate and thid is no of steps
for number in range(0,100, 10):
    print(number)

# lets say we need to break loop on certain condition
for number in range(0,10):
    print("In loop")
    if number == 5:
        print("reached to 5, breaking here")
        break

# else block of for will execute only of inner if never reached and iteration completed
for number in range(0,10):
    print("In loop", number)
    if number == 5:
        print(f"reached to {number}, breaking here")
        break
else:
    print("all set")

# nested loops
for x in range(5):
    for y in range(3):
        print(f"(x is {x}, y is {y})")


# type of range is always range called iterable (complex type)
# strings are also iterable

for str in "Python":
    print(str) 

# list is complex object like arrays

for num in [10,20,30]:
    print(num)


# while loops
# text = ""
# while text != "-1":
#     aNumber = input("Enter a text: ")

evenCount = 0
for even in range(2,10):
    if(even % 2 == 0):
        print(even)
        evenCount += 1
    even += 1
print(f"we have {evenCount} even numbers")


