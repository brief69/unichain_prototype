import unittest
from src.unichain import Unichain

class TestUnichain(unittest.TestCase):
    def setUp(self):
        self.unichain = Unichain()
        self.unichain.add_blockchain("ChainA")
        self.unichain.add_blockchain("ChainB")

    def test_add_blockchain(self):
        self.assertIn("ChainA", self.unichain.blockchains)
        self.assertIn("ChainB", self.unichain.blockchains)

    def test_add_data(self):
        self.unichain.add_data("Test Transaction")
        self.assertEqual(self.unichain.get_data("ChainA", 1), "Test Transaction")
        self.assertEqual(self.unichain.get_data("ChainB", 1), "Test Transaction")

    def test_get_data(self):
        self.unichain.add_data("Transaction 1")
        self.unichain.add_data("Transaction 2")
        self.assertEqual(self.unichain.get_data("ChainA", 1), "Transaction 1")
        self.assertEqual(self.unichain.get_data("ChainB", 2), "Transaction 2")

if __name__ == '__main__':
    unittest.main()
