# input Sample:  1 1 0 1 0
#               0 0 1 0 1
# output Sample: Y

firstConnector = input().split()
secondConnector = input().split()

count = 0
while (count < 5):
    if firstConnector[count] == secondConnector[count]:
        print("N")
        break
    count += 1

if count == 5:
    print("Y")
