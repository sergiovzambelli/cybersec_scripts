import csv
import matplotlib.pyplot as plt
import numpy as np

input_file = "mining_results.csv"

def read_csv(file_name):
    data = {}
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            difficulty = row["Difficulty Level"]
            time = float(row["Mining Time (s)"])
            if difficulty not in data:
                data[difficulty] = []
            data[difficulty].append(time)
    return data

def calculate_statistics(data):
    stats = {}
    for difficulty, times in data.items():
        mean_time = np.mean(times)
        std_dev = np.std(times)
        stats[difficulty] = (mean_time, std_dev)
    return stats

def plot_statistics(stats):
    difficulties = list(stats.keys())
    means = [stats[difficulty][0] for difficulty in difficulties]
    std_devs = [stats[difficulty][1] for difficulty in difficulties]

    x_pos = np.arange(len(difficulties))

    plt.plot(x_pos, means, marker='o', linestyle='-', color='blue', label='Media')
    
    plt.errorbar(x_pos, means, yerr=std_devs, fmt='o', capsize=5, color='blue', label='Deviazione Standard', alpha=0.5)

    plt.xticks(x_pos, [len(difficulties[i]) for i in range(len(difficulties))])
    plt.xlabel("Livello di Difficoltà")
    plt.ylabel("Tempo Medio di Mining (s)")
    plt.title("Performance del Mining per Livello di Difficoltà")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("mining_statistics.png")
    plt.show()
    

if __name__ == "__main__":
    data = read_csv(input_file)
    stats = calculate_statistics(data)
    plot_statistics(stats)
    
