count = 0

with open('./data.txt') as f:
  lastNumber = f.readline()
  for index, line in enumerate(f):
      number = line.strip()
      if lastNumber > number:
        count += 1
      lastNumber = number

  f.close()

print("count is : {}".format(count))

