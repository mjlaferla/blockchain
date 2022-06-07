import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Hello World", proof=100)

    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions
        self.chain.append(block)

        return block

# Search chain for the most recent block

    @property
    def last_block(self): 

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount # perhaps adapt this to a different use case 
        }
        self.pending_transactions.append(transaction)

        return self.last_block['index'] + 1
    
    def hash(self, block):
        string_object =json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash



blockchain = Blockchain()
t1 = blockchain.new_transaction("Mitchell", "Village Property Management", "0.083 BTC")
t2 = blockchain.new_transaction("Ilsa", "Mitchell", "0.041 BTC")
t3 = blockchain.new_transaction ("Judo", "Village Property Management", "0.041 BTC")
blockchain.new_block(1234)

t4 = blockchain.new_transaction("Mitchell", "SDGE", "0.0075 BTC")
t5 = blockchain.new_transaction("Ilsa", "Mitchell", "0.0025 BTC")
t6 = blockchain.new_transaction("Judo", "Mitchell", "0.0025 BTC")
blockchain.new_block(5678)

print("Blockchain: ", blockchain.chain)