numOfTests = int(input())
numOfLEDs = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

while (numOfTests):
    num = input()
    totalOfLEDs = 0

    for index in num:
        totalOfLEDs += numOfLEDs[int(index)]

    print(str(totalOfLEDs) + " leds")
    numOfTests -= 1