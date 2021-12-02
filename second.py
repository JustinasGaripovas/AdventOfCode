count = 0
with open('./data.txt') as file:
    lastSum = None
    index = 0

    lines = [line.rstrip() for line in file.readlines()]

    for index in range(len(lines)-2):
        currentSum = int(lines[index]) + int(lines[index+1]) + int(lines[index+2])
        if index == 0:
            print("{} N/A - no previous measurement".format(currentSum))
            lastSum = currentSum
            continue
        if currentSum > lastSum:
            print("{} increased".format(currentSum))
            count += 1
        elif currentSum == lastSum:
            print("{} no change".format(currentSum))
        else:
            print("{} decreased".format(currentSum))
        lastSum = currentSum

print("count is : {}".format(count))

