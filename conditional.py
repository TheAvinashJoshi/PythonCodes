count = 25
if count > 10:  # colon is terminator used in ifs, below will come indent that tells compiler something under the scope of if
    print("it is more than 10")
    print("make a coffee")
# when you remove indentation it will ask compiler to close if scope
print("out of if1")

if count > 30:
    print("more than 30")
elif count > 20:
    print("more than 20")
else:
    print(F"count is {count}")

print("out of if else ladder")

# ternary
age = 20
print("Eligible" if age > 18 else "Not Eligible")