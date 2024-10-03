import unittest
from src.block import Block

class TestBlock(unittest.TestCase):
    def test_block_creation(self):
        block = Block(1, "previous_hash", 1234567890, "test_data", "test_hash")
        self.assertEqual(block.index, 1)
        self.assertEqual(block.previous_hash, "previous_hash")
        self.assertEqual(block.timestamp, 1234567890)
        self.assertEqual(block.data, "test_data")
        self.assertEqual(block.hash, "test_hash")

if __name__ == '__main__':
    unittest.main()
