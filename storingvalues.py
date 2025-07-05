# integers
intCount = 20
intCount2 = 10
print("intCount=", intCount, "and intCount2=", intCount2)
print("sum=", intCount + intCount2)
print("substraction=", intCount - intCount2)
print("multiplication=", intCount * intCount2)
print("division=", intCount / intCount2)
# print("testing devide by zero ", intCount / 0)

# floats
floatCount = 1.9
print("floatCount=", floatCount)

# boolean
isThisThree = (3 == 4)
print("boolean test", isThisThree)

# writing big strings and in good format
longString = """
  Hello Bob \n
  Hope you are well \n
  I got your email and I will get back to you soon\n
  Regards\n
  Avinash 
"""
print("longString=", longString)

# length of string
print("the longstring is", len(longString), "characters long")

# accessing inside string
stringVar = "Python Programming"
print("first letter of", stringVar, "is", stringVar[0])
print("last letter of", stringVar, "is", stringVar[len(stringVar)-1])
print("last letter of", stringVar, "is", stringVar[-1])
print("first 3 letters of", stringVar, "are", stringVar[0:3])
print("all letters of", stringVar, "are", stringVar[0:])
print("first 3 letters of", stringVar, "are", stringVar[:3])
print("copy of", stringVar, "is", stringVar[:])

# escape characters  \" \' \\ \n (for newline)
print('I am "Avinash"')
print("I am \"Avinash\"")

# formatting strings
firstName = "Avinash"
lastName = "Joshi"
fullName = firstName + " " + lastName
print("First name is", firstName, "Last name is", lastName, "Full name is", fullName)

# use formatter f or F (same thing)
print(F"First name is {firstName} and Last name is {lastName} and fullName is {firstName} {lastName}")
print(f"First name is {firstName} and Last name is {lastName} and fullName is {firstName} {lastName}")


# string functions stringVariable and press dot and see all
collegeName = "Aishwarya college"
print(f"length of {collegeName}is {len(collegeName)}")
print(f"lower case of {collegeName.upper()} is {collegeName.lower()}")
print(f"{collegeName} in tilecase {collegeName.title()}")
spacedCollegeName = "   Aishwarya college  "
print(f"{spacedCollegeName} removed whitespaces or trimmed {spacedCollegeName.strip()}")
print(f"{spacedCollegeName} removed left whitespaces or trimmed {spacedCollegeName.lstrip()}")
print(f"{spacedCollegeName} removed right whitespaces or trimmed {spacedCollegeName.rstrip()}")

# search in a string (case sensitive) -1 means not found
stringToSearch = "My world is beatiful world"
searchKey = "world"
# only first occurance will display
print(f"{searchKey} in {stringToSearch} is at {stringToSearch.find(searchKey)} index") 

# check if contains (TRUE or FALSE)
print(f"{searchKey} in {stringToSearch} EXISTS? {searchKey in stringToSearch }") 
print(f"Universe in {stringToSearch} EXISTS? {"Universe" in stringToSearch }") 

# replace
stringToReplaceIn = "My world is beatiful world"
print(f"Before {stringToReplaceIn}") 
print(f"After replacing world with universe {stringToReplaceIn.replace("world", "universe")}") 






