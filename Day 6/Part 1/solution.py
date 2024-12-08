import pathlib

def getInput(inputFile = 'input.txt'):
  fileContents = []
  obstacles = {
    "x": {},
    "y": {}
  }
  with open(pathlib.Path(__file__).parent.resolve().joinpath(inputFile)) as f:
    for y, line in enumerate(f):
      for i, position in enumerate(line):
        if position == "^":
          locX, locY  = (i, y)
        if position == "#":
          obstacles["x"].setdefault(i, []).append(y)
          obstacles["y"].setdefault(y, []).append(i)
      fileContents.append(list(line.rstrip()))
  f.close()
  return fileContents, locX, locY, obstacles;

def isObstacle(position):
  return position == '#'

def patrol(map, locX, locY, obstacles):
  TOP = 0
  BOTTOM = len(map)
  LEFT = 0
  RIGHT = len(map[0])

  NORTH = 'N'
  EAST = 'E'
  SOUTH = 'S'
  WEST = 'W'

  positions = 1
  direction = NORTH
  while LEFT <= locX and locX < RIGHT - 1 and TOP <= locY and locY < BOTTOM - 1:
    if direction == NORTH:
      for next in reversed(range(min(TOP, locY - 1), max(TOP, locY))):
        if next < TOP:
          positions += 1
          locY = next
          break
        if isObstacle(map[next][locX]):
          direction = EAST
          break
        positions += 1
        locY = next

    elif direction == SOUTH:
      for next in range(locY + 1, BOTTOM):
        if next == BOTTOM:
          break
        if isObstacle(map[next][locX]):
          direction = WEST
          break
        positions += 1
        locY = next
    elif direction == EAST:
      for next in range(locX + 1, RIGHT):
        if next == RIGHT:
          break
        if isObstacle(map[locY][next]):
          direction = SOUTH
          break
        positions += 1
        locX = next
    elif direction == WEST:
      for next in reversed(range(min(LEFT, locX - 1), max(LEFT, locX))):
        if next < LEFT:
          positions += 1
          locX = next
          break
        if isObstacle(map[locY][next]):
          direction = NORTH
          break
        locX = next
        positions += 1
  return positions

map, locX, locY, obstacles = getInput('input3.txt')
print(patrol(map, locX, locY, obstacles))