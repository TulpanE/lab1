from main import find
import unittest

class TestFunction(unittest.TestCase):
	def test_find(self):
		self.assertEqual(find(5278), 4)


if __name__ == '__main__':
	unittest.main()