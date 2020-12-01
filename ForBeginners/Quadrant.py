# First Quadrant :  x = Positive number
#                   y = Positive number
# Second Quadrant : x = Negative number
#                   y = Positive number
# Third Quadrant :  x = Negative number
#                   y = Negative number
# Fourth Quadrant : x = Positive number
#                   y = Negative number

while(1):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if x > 0 and y > 0:
        print("First")
    elif x < 0 and y > 0:
        print("Second")
    elif x < 0 and y < 0:
        print("Third")
    elif x > 0 and y < 0:
        print("Fourth")
    else:
        break