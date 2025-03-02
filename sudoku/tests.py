import unittest

from parameterized import parameterized
from table_gen.table_gen import gen_base_table, gen_table, generate_sudoku
from verifier.verifier import verifier


class TestIntegration(unittest.TestCase):
    def test_match_table(self):
        """Creating match table"""
        self.assertTrue(verifier(gen_table(gen_base_table(), 30)))

    @parameterized.expand([30, 50, 80, 99, 3, 28])
    def test_match_table_with_multiple_iterations(self, iter):
        self.assertTrue(verifier(gen_table(gen_base_table(), iter)))

    @parameterized.expand([30, 50, 80, 99, 3, 28])
    def test_match_with_alternative_table_gen(self, iter):
        self.assertTrue(verifier(generate_sudoku()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
