def test_range():
    n= int(input("Enter the number: "))
    if n in range(4,11):
        return "Morning"
    elif n in range(11,16):
        return "Noon"
    elif n in range(16, 20):
        return "Evening"
    elif n in range(20,24):
        return "Night"
    elif n in range(0,4):
        return "Past midnight"
    else:
        return "You have entered the number out of the range"
print(test_range())