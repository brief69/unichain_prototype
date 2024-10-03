from .block import Block
import time
import hashlib

class Blockchain:
    def __init__(self, name):
        self.name = name
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), f"Genesis Block of {self.name}", self.calculate_hash("0", int(time.time()), f"Genesis Block of {self.name}"))

    def calculate_hash(self, previous_hash, timestamp, data):
        value = str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def verify_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            return False
        
        if transaction.amount <= 0:
            return False
        
        # トランザクション形式の検証
        if not all(isinstance(field, str) for field in [transaction.sender, transaction.recipient]):
            return False
        
        # デジタル署名の検証
        if not transaction.signature:
            return False
        
        public_key = rsa.PublicKey.from_pem(transaction.sender.encode())
        return Transaction.verify_signature(transaction.to_dict(), transaction.signature, public_key)

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def add_block(self, transaction):
        if not self.verify_transaction(transaction):
            raise ValueError("Invalid transaction")
        
        last_block = self.chain[-1]
        proof = self.proof_of_work(last_block.hash)
        previous_hash = last_block.hash
        block = self.create_block(proof, previous_hash, transaction.to_dict())
        self.chain.append(block)
        return block

    def create_block(self, proof, previous_hash, data):
        index = len(self.chain)
        timestamp = int(time.time())
        hash = self.calculate_hash(previous_hash, timestamp, data, proof)
        return Block(index, previous_hash, timestamp, data, hash)
