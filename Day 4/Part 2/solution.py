import pathlib

def getInput():
  inputFile = "input.txt"
  fileContents = []
  with open(pathlib.Path(__file__).parent.resolve().joinpath(inputFile)) as f:
    for line in f:
      fileContents.append(list(line))
  f.close()
  return fileContents;


def searchXmas(window):
  mas = "MAS"
  sam = mas[::-1]
  validMas = [mas, sam]

  diagLeft = ''
  for d in range(3):
    diagLeft += window[d][d]

  diagRight = ''
  for d in range(3):
    diagRight += window[d][2 - d]
                  
  if diagLeft in validMas and diagRight in validMas:
    return 1
  
  return 0

input = getInput()
count = 0
for y, row in enumerate(input):
  if len(input) - 3 < y:
    break

  for x in range(len(row) - 3):
    searchWindow = [
      [input[  y  ][x], input[  y  ][x + 1], input[  y  ][x + 2]],
      [input[y + 1][x], input[y + 1][x + 1], input[y + 1][x + 2]],
      [input[y + 2][x], input[y + 2][x + 1], input[y + 2][x + 2]]
    ]
    count += searchXmas(searchWindow)

print(count)