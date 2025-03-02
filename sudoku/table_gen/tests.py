import unittest

from table_gen import gen_base_table

# fmt: off
# this is materialization of the table we expect from gen_base_table
base_table = [
  [1,2,3, 4,5,6, 7,8,9],
  [4,5,6, 7,8,9, 1,2,3],
  [7,8,9, 1,2,3, 4,5,6],

  [2,3,4, 5,6,7, 8,9,1],
  [5,6,7, 8,9,1, 2,3,4],
  [8,9,1, 2,3,4, 5,6,7],
  
  [3,4,5, 6,7,8, 9,1,2],
  [6,7,8, 9,1,2, 3,4,5],
  [9,1,2, 3,4,5, 6,7,8],
]
# fmt: on


class TestTableGen(unittest.TestCase):
    def test_base(self):
        """Check base table"""
        self.assertEqual(base_table, gen_base_table())


if __name__ == "__main__":
    unittest.main(verbosity=2)
