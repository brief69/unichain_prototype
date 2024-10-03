import unittest
from src.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain("TestChain")

    def test_genesis_block(self):
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.previous_hash, "0")
        self.assertIn("Genesis Block of TestChain", genesis_block.data)

    def test_add_block(self):
        self.blockchain.add_block("Test Transaction")
        new_block = self.blockchain.chain[-1]
        self.assertEqual(new_block.index, 1)
        self.assertEqual(new_block.data, "Test Transaction")
        self.assertEqual(new_block.previous_hash, self.blockchain.chain[-2].hash)

    def test_verify_transaction(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        
        valid_transaction = Transaction("sender_public_key", "recipient", 100)
        valid_transaction.sign(private_key)
        
        self.assertTrue(self.blockchain.verify_transaction(valid_transaction))
        
        invalid_transaction = Transaction("sender_public_key", "recipient", -100)
        invalid_transaction.sign(private_key)
        
        self.assertFalse(self.blockchain.verify_transaction(invalid_transaction))
        
        unsigned_transaction = Transaction("sender_public_key", "recipient", 100)
        self.assertFalse(self.blockchain.verify_transaction(unsigned_transaction))

    def test_add_invalid_transaction(self):
        invalid_transaction = Transaction("sender_public_key", "recipient", -100)
        with self.assertRaises(ValueError):
            self.blockchain.add_block(invalid_transaction)

if __name__ == '__main__':
    unittest.main()
