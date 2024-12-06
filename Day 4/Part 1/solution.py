import pathlib

def getInput():
  inputFile = "input.txt"
  fileContents = []
  with open(pathlib.Path(__file__).parent.resolve().joinpath(inputFile)) as f:
    for line in f:
      fileContents.append(list(line))
  f.close()
  return fileContents;


def searchXmas(window, gX, gY, seent):
  xmas = "XMAS"
  samx = xmas[::-1]
  validXmas = [xmas, samx]

  diagLeft = ''
  for d in range(4):
    diagLeft += window[d][d]
                  
  if diagLeft in validXmas:
    offset = diagLeft.index("X");
    if offset == 0:
      seent["".join((str(gX), ",", str(gY), ",DLF"))] = diagLeft
    else:
      seent["".join((str(gX + offset), ",", str(gY + offset), ",DLB"))] = diagLeft

  diagRight = ''
  for d in range(4):
    diagRight += window[d][3 - d]
                  
  if diagRight in validXmas:
    offset = diagRight.index("X");
    if offset == 0:
      seentKey = "".join((str(gX + 3), ",", str(gY), ",DRF"))
      seent[seentKey] = diagRight
    else:
      seentKey = "".join((str(gX), ",", str(gY + offset), ",DRB"))
      seent[seentKey] = diagRight

  maybeY = []
  for y in range(4):
    maybe = "".join(window[y]);
    maybeY.append(maybe)
    if maybe in validXmas:
      offsetX = maybe.index("X");
      seentKey = "".join((str(gX + offsetX), ",", str(gY + y), ",R" if offsetX == 0 else ",L"));
      seent[seentKey] = maybe

  maybeX = [] 
  for x in range(4):
    maybe = "".join(window[y][x] for y in range(4));
    maybeX.append(maybe)
    if maybe in validXmas:
      offsetY = maybe.index("X");
      seentKey = "".join((str(gX + x), ",", str(gY), ",D" if offsetY == 0 else ",U"))
      seent[seentKey] = maybe

input = getInput()
seent = {}
for y, row in enumerate(input):
  if len(input) - 4 < y:
    break

  for x in range(len(row) - 4):
    searchWindow = [
      [input[  y  ][x], input[  y  ][x + 1], input[  y  ][x + 2], input[  y  ][x + 3]],
      [input[y + 1][x], input[y + 1][x + 1], input[y + 1][x + 2], input[y + 1][x + 3]],
      [input[y + 2][x], input[y + 2][x + 1], input[y + 2][x + 2], input[y + 2][x + 3]],
      [input[y + 3][x], input[y + 3][x + 1], input[y + 3][x + 2], input[y + 3][x + 3]],
    ]
    searchXmas(searchWindow, x, y, seent)

print(len(seent))