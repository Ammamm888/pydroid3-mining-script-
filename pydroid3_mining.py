"""
Developer name: [Pluto88]
Date: [20/10/2023]
Details: [This is an example of simulating scraping with python. This code can be developed further]
"""

from hashlib import sha256
import time
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value: {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")

if __name__=='__main__':
    difficulty = 4  # Try changing this to a higher number for increased difficulty
    transactions = ''
    prefix_zeros = 5  # Number of leading zeros for a valid hash
    previous_hash = '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7'

    while True:
        import time
        start = time.time()
        print("Started mining...")
        new_hash = mine(5, transactions, previous_hash, prefix_zeros)
        total_time = str((time.time() - start))
        print(f"Ending mining. Mining took: {total_time} seconds")
        previous_hash = new_hash  # Set the new hash as the previous hash for the next block
        print(f"New block mined with hash: {new_hash}")