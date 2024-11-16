import hashlib
import datetime
import os
import time
import csv
import json
from tqdm import tqdm

difficulty_max = 10
difficulty_levels = ["0" * i for i in range(1, difficulty_max + 1)]
trials = 1

output_file = "mining_results.csv"
state_file = "mining_state.json"


'''
Block class with a nonce that increments by 1 during the mining process.

The mining process involves generating a hash for the block and comparing the first 
`len(difficulty)` characters of the hash with the given difficulty level. 
The process continues until the hash satisfies the difficulty condition.
'''
class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.nonce).encode("utf-8")
            + str(self.data).encode("utf-8")
            + str(self.previous_hash).encode("utf-8")
        )
        return sha.hexdigest()

    def mine_block(self, difficulty_level):
        start_time = time.time()
        while self.hash[: len(difficulty_level)] != difficulty_level:
            self.nonce += 1
            self.hash = self.hash_block()
        elapsed_time = time.time() - start_time
        return elapsed_time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, new_block, difficulty_level):
        new_block.previous_hash = self.chain[-1].hash
        mining_time = new_block.mine_block(difficulty_level)
        self.chain.append(new_block)
        return mining_time


'''
Utility functions to save and load the state of the mining process.

These functions manage the persistence of the current state in a JSON file. 
The state includes the current difficulty level and trial, allowing the program 
to resume the mining process from the last saved point in case of non-continuous execution.
'''
def write_to_csv(file_name, results, write_header=False):
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Difficulty Level", "Trial", "Mining Time (s)"])
        writer.writerows(results)

def save_state(file_name, state):
    with open(file_name, mode="w") as file:
        json.dump(state, file)

def load_state(file_name):
    try:
        with open(file_name, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"difficulty_index": 0, "trial": 1}


'''
This program is designed to analyze and collect statistics on how computational time increases 
with the difficulty level during the mining process. The results are recorded in a CSV file 
for analysis. 

To allow for non-continuous execution of the script, the program saves the current state of 
the mining process in a JSON file. This state includes the last difficulty level and trial 
completed, enabling the script to resume from where it left off when executed again.
'''
if __name__ == "__main__":
    blockchain = Blockchain()

    # Managing the header of the CSV file 
    if not os.path.exists(output_file) or os.stat(output_file).st_size == 0:
        write_to_csv(output_file, [], write_header=True)

    # Load the state of previous iterations
    state = load_state(state_file)
    start_difficulty_index = state["difficulty_index"]
    start_trial = state["trial"]

    # Loop through the difficulty levels and trials
    for difficulty_index in range(start_difficulty_index, len(difficulty_levels)):
        difficulty = difficulty_levels[difficulty_index]
        print("Livello di Difficoltà: ", difficulty)

        # Progress bar for the mining process
        for trial in tqdm(
            range(start_trial, trials + 1),
            desc=f"Mining with difficulty {difficulty}",
            unit="trial",
        ):
            block = Block(f"Block {trial}", "")
            mining_time = blockchain.add_block(block, difficulty)
            result = [difficulty, trial, mining_time]

            write_to_csv(output_file, [result], write_header=False)
            
            save_state(
                state_file, {"difficulty_index": difficulty_index, "trial": trial + 1}
            )

        start_trial = 1

    print(f"Risultati salvati in {output_file}")
    save_state(state_file, {"difficulty_index": 0, "trial": 1})
