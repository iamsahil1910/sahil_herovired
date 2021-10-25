import unittest
from maths import Maths

class TestMaths(unittest.TestCase):
  def setUp(self):
    self.maths = Maths()
  def test_add(self):
    self.assertEqual(self.maths.add(4,7), 12)  
  def test_subtract(self):
    self.assertEqual(self.maths.subtract(10,5), 5)
  def test_multiply(self):
    self.assertEqual(self.maths.multiply(3,7), 22)


if __name__ == "__main__":
  unittest.main()