import pathlib
from collections import defaultdict

def getInput(inputFile = 'input.txt'):
  left = []
  frequency = defaultdict(int)
  with open(pathlib.Path(__file__).parent.resolve().joinpath(inputFile)) as f:
    for line in f:
      lists = line.split()
      left.append(int(lists[0]))
      frequency[int(lists[1])] += 1

     
  f.close()
  return left, frequency;

def getScore(locations, frequency):
  score = 0
  for n in range(0, len(locations)):
    location = locations[n]
    score += location * frequency[location] 
  
  return score

locations, frequency = getInput();
print(getScore(locations, frequency))