import enum

class Directions(enum.Enum):
   forward = 'forward'
   down = 'down'
   up = 'up'

with open('./data.txt') as f:
  directions = {Directions.forward.value: 0, Directions.down.value: 0, Directions.up.value: 0}
  depth = 0
  for index, line in enumerate(f):
      direction, amount = line.strip().split(" ")
      aim = abs(directions[Directions.down.value] - directions[Directions.up.value])
      if direction == Directions.forward.value:
        depth += int(amount) * aim
      directions[direction] += int(amount)
  f.close()

print("forward/horizontal {}".format(directions[Directions.forward.value]))
print("depth {}".format(depth))
print("total {}".format(directions[Directions.forward.value] * depth))
