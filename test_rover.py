from rover import *
import unittest

class TestRover(unittest.TestCase):
    def setUp(self):
        rover1 = Rover()
        rover1.direction = NORTH
        rover1.position = [1, 3]

        rover2 = Rover()
        rover2.direction = EAST
        rover2.position = [5, 1]

        rover3 = Rover()
        rover3.direction = SOUTH
        rover3.position = [2, 2]

        self.expected = [rover1, rover2, rover3]
        self.result = parseCommand('5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM\n2 3 W\nMMLM')
        self.expected
    

    def test_rover_position(self):
        self.assertEqual(self.result[0].position, self.expected[0].position)
        self.assertEqual(self.result[1].position, self.expected[1].position)

    def test_rover_direction(self):
        self.assertEqual(self.result[0].direction, self.expected[0].direction)
        self.assertEqual(self.result[1].direction, self.expected[1].direction)
    
    #A rover cannot move if another rover is in the path that it needs to into
    def test_rover_not_crash_in_rover_path(self):
        self.assertEqual(self.result[2].direction, self.expected[2].direction)
        self.assertEqual(self.result[2].position, self.expected[2].position)



if __name__ == "__main__":
    unittest.main()