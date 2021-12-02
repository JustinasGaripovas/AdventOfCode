import enum

class Directions(enum.Enum):
   forward = 'forward'
   down = 'down'
   up = 'up'

with open('./data.txt') as f:
  directions = {Directions.forward.value: 0, Directions.down.value: 0, Directions.up.value: 0}
  for index, line in enumerate(f):
      direction, amount = line.strip().split(" ")
      directions[direction] += int(amount)
#       print("{} : {}".format(direction, amount))

  f.close()

print("forward {}".format(directions[Directions.forward.value]))
print("down {}".format(directions[Directions.down.value]))
print("up {}".format(directions[Directions.up.value]))
print("total {}".format(directions[Directions.forward.value] * abs(directions[Directions.down.value] - directions[Directions.up.value])))

