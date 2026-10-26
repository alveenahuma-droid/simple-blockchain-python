# Simple Blockchain in Python

A minimal blockchain implementation in Python that demonstrates the core ideas behind blockchain technology: blocks, transactions, hash linking, proof of work, and chain validation. It uses only the Python standard library.

## Features

- Genesis block created automatically
- Add transactions to a pending pool
- Mine new blocks with a simple proof-of-work algorithm
- SHA-256 hashing to link blocks together
- Chain validation to detect tampering

## How It Works

1. **Transactions** are added to a pending list.
2. **Proof of work**: find a number such that `sha256(prev_proof + proof)` starts with `0000`.
3. **New block**: stores the pending transactions, the proof, and the hash of the previous block.
4. **Validation**: for every block, check that `prev_hash` matches the real hash of the previous block and that the proof is valid.

## Requirements

- Python 3.8+
- No external libraries

## Installation

```bash
git clone https://github.com/<your-username>/simple-blockchain-python.git
cd simple-blockchain-python
```

## Usage

Run the built-in demo:

```bash
python blockchain.py
```

Or use it in your own code:

```python
from blockchain import Blockchain

chain = Blockchain()
chain.add_transaction("Alice", "Bob", 50)

prev = chain.get_last_block()
proof = chain.proof_of_work(prev['proof'])
chain.create_block(proof, chain.hash_block(prev))

print(chain.validate_chain())  # True
```

## Example Output

```
Chain valid? True
Blocks: 2
```

## Limitations

This is a learning project, not a production blockchain. It has no networking, no digital signatures, no balance checks, and a fixed mining difficulty.

## Possible Improvements

- Adjustable mining difficulty
- Digital signatures for transactions
- Balance validation
- A Flask API and multiple nodes with a consensus algorithm

## License

MIT
