# Blockchain Mining Simulation

This project simulates the mining process of blocks in a blockchain. The mining process is based on the SHA-256 hashing algorithm, and the program calculates how long it takes to mine a block depending on the difficulty level. The results can be visualized and analyzed statistically to observe how the mining time scales with increasing difficulty.

## Overview

The script simulates the mining of blocks in a blockchain by finding a "nonce" value that results in a hash with a number of leading zeros equal to the current difficulty level. The difficulty starts low and increases progressively as more trials are conducted.

### Key Features:

- **Blockchain Mining**: The mining process involves adjusting the difficulty level (number of leading zeros in the hash) and tracking the time it takes to mine a block.
- **Persistence**: The mining process is stored in a CSV file (`mining_results.csv`) for easy analysis. Additionally, a JSON file (`mining_state.json`) stores the state of the process, allowing you to resume from where you left off in case of interruptions.
- **Statistical Analysis**: The `mean.py` script reads the mining results from the CSV, calculates the mean and standard deviation of the mining times at each difficulty level, and visualizes the performance.
- **Data Visualization**: The statistics (mean and standard deviation) are displayed in a graph to help understand how mining performance scales with the difficulty.

## Features

- Simulates blockchain mining with varying difficulty levels using the SHA-256 hashing algorithm.
- Saves the mining results in a CSV file, including difficulty level, trial number, and mining time.
- Tracks the state of the mining process in a JSON file, enabling you to resume from the last saved point.
- Provides statistical analysis of mining times, including the mean and standard deviation for each difficulty level.
- Generates a plot visualizing the mining performance across different difficulty levels, including error bars for standard deviation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blockchain-mining-simulation.git
   ```

2. Navigate into the project directory:
   ```bash
   cd blockchain
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the script, simply execute the following command:

```bash
python3 blockchain.py
```

This will start the mining process and save the results in `mining_results.csv`. If the process is interrupted, it will resume from the last saved state upon the next run.

Once the mining process is complete, you can analyze the results by generating statistics. To calculate and visualize the mining performance across different difficulty levels, run the following script:
```bash
python3 mean.py
```

## Output

The results will be stored in a CSV file (`mining_results.csv`) with the following columns:

- **Difficulty Level**: The current mining difficulty.
- **Trial**: The trial number.
- **Mining Time (s)**: The time taken to mine the block.