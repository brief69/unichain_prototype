from .blockchain import Blockchain
from .transaction import Transaction

class Unichain:
    def __init__(self):
        self.blockchains = {}

    def add_blockchain(self, name):
        self.blockchains[name] = Blockchain(name)

    def add_transaction(self, transaction):
        for blockchain in self.blockchains.values():
            try:
                blockchain.add_block(transaction)
            except ValueError as e:
                print(f"Failed to add transaction to {blockchain.name}: {str(e)}")

    def get_data(self, blockchain_name, index):
        return self.blockchains[blockchain_name].chain[index].data
