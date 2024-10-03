from src.unichain import Unichain
from src.transaction import Transaction
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    unichain = Unichain()
    unichain.add_blockchain("Chain A")
    unichain.add_blockchain("Chain B")

    alice_private_key, alice_public_key = generate_key_pair()
    bob_private_key, bob_public_key = generate_key_pair()

    print("Adding transactions to Unichain...")
    
    transaction1 = Transaction(alice_public_key.public_bytes(), bob_public_key.public_bytes(), 1)
    transaction1.sign(alice_private_key)
    unichain.add_transaction(transaction1)

    transaction2 = Transaction(bob_public_key.public_bytes(), alice_public_key.public_bytes(), 0.5)
    transaction2.sign(bob_private_key)
    unichain.add_transaction(transaction2)

    print("\nRetrieving data from Chain A:")
    print(f"Block 1: {unichain.get_data('Chain A', 1)}")
    print(f"Block 2: {unichain.get_data('Chain A', 2)}")

    print("\nRetrieving data from Chain B:")
    print(f"Block 1: {unichain.get_data('Chain B', 1)}")
    print(f"Block 2: {unichain.get_data('Chain B', 2)}")

if __name__ == "__main__":
    main()
