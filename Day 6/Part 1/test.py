import solution
import unittest

class TestInputs(unittest.TestCase): 

  def testExitsSouth(self):      
    map, locX, locY, obstacles = solution.getInput('input1.txt')
    positions = solution.patrol(map, locX, locY, obstacles)
    self.assertEqual(positions, 41)

  def testExitNorth(self):      
    map, locX, locY, obstacles = solution.getInput('input2.txt')
    positions = solution.patrol(map, locX, locY, obstacles)
    self.assertEqual(positions, 7)

  def testExitEast(self):      
    map, locX, locY, obstacles = solution.getInput('input3.txt')
    positions = solution.patrol(map, locX, locY, obstacles)
    self.assertEqual(positions, 6)

  def testExitWest(self):      
    map, locX, locY, obstacles = solution.getInput('input4.txt')
    positions = solution.patrol(map, locX, locY, obstacles)
    self.assertEqual(positions, 6)

if __name__ == '__main__': 
    unittest.main() 