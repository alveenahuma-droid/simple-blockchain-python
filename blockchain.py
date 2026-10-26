import hashlib
import json
import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending = []
        # Genesis block
        self.create_block(proof=1, prev_hash='0')

    def create_block(self, proof, prev_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending,
            'proof': proof,
            'prev_hash': prev_hash
        }
        self.pending = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount):
        self.pending.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time.time()
        })

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, prev_proof):
        new_proof = 1
        while not self.valid_proof(prev_proof, new_proof):
            new_proof += 1
        return new_proof

    @staticmethod
    def valid_proof(prev_proof, proof):
        guess = f'{prev_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash_block(self, block):
        encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr['prev_hash'] != self.hash_block(prev):
                return False

            if not self.valid_proof(prev['proof'], curr['proof']):
                return False

        return True


if __name__ == "__main__":
    # Demo
    chain = Blockchain()
    chain.add_transaction("Alice", "Bob", 50)
    chain.add_transaction("Bob", "Charlie", 25)

    prev = chain.get_last_block()
    proof = chain.proof_of_work(prev['proof'])
    prev_hash = chain.hash_block(prev)
    chain.create_block(proof, prev_hash)

    print("Chain valid?", chain.validate_chain())
    print(f"Blocks: {len(chain.chain)}")
