import unittest
from main import grid_size

class LayoutTests(unittest.TestCase):
    def test_grid_size_rounds_up(self):
        self.assertEqual(grid_size(10,4),(4,3))

    def test_rejects_invalid_columns(self):
        with self.assertRaises(ValueError):
            grid_size(3,0)

if __name__=="__main__": unittest.main()
