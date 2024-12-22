x = int(input("Please enter a integer: "))
if x < 0:
    x = "0"
    print("Negative changed to zero. x =", x)
# Use elif whenever you want to have more than one if
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
