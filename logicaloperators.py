# and or not

percentage = int(input("Enter percentage: "))
if percentage >= 30 and percentage <= 40:
    print("Third Division")
elif percentage > 40 and percentage <= 60:
    print("Second Division")
elif percentage > 60 and percentage <= 100:
    print("First Division")
elif percentage < 30 or percentage <= 0:
    print("Failed")
elif not percentage < 100:
    print("Enter valid value between 0 and 100")
else:
    print("Undetermined")


