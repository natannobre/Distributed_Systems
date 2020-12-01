iterations = int(input())

while(iterations > 0):
    iterations -= 1

    value = int(input())
    index = 0
    sum = 0
    while(index < value):
        sum += 2 ** index
        index += 1
    print(sum)
