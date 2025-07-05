x = input("x = ")
# y = x + 1 # this will give error because can only concatenate str (not "int") to str
# uncomment above and run and try , user input is string and concat is being tried with int ("1" + 1)

# below are built in functions
# int(x)
# float(x)
# bool(x)
# str(x)

print(type(x))  #checks type of a variable value

print(int(x) + 1)

# boolean false = 0, None, "" rest all are true
print(bool("")) # boolean False
print(bool(0)) # boolean False
print(bool(None)) # boolean False
print(bool(1)) # boolean True
print(bool(-1)) # boolean True
print(bool(5)) # boolean True


