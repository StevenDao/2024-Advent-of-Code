import pathlib

def getInput(inputFile = 'input.txt'):
  left = []
  right = []
  with open(pathlib.Path(__file__).parent.resolve().joinpath(inputFile)) as f:
    for line in f:
      numbers = line.split()
      left.append(int(numbers[0]))
      right.append(int(numbers[1]))
     
  f.close()
  return left, right;

def orderedSum(left, right):
  left.sort()
  right.sort()

  sum = 0
  for n in range(0, len(left)):
    sum += abs(left[n] - right[n]) 
  
  return sum

left, right = getInput();
print(orderedSum(left, right))