import csv
import matplotlib.pyplot as plt

ns, cIt, cMem, rIt, rMem = [], [], [], [], []

with open("linear_times.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['N']:
            ns.append(int(row['N']))
            cIt.append(float(row['C Iterative']) * 1000)
            cMem.append(float(row['C Memoization']) * 1000)
            rIt.append(float(row['Rust Iterative']) * 1000)
            rMem.append(float(row['Rust Memoization']) * 1000)

plt.figure(figsize=(12, 6))
plt.plot(ns, cIt, label="C Iterative", color="blue", linewidth=1)
plt.plot(ns, cMem, label="C Memoization", color="green", linestyle="--", linewidth=1)
plt.plot(ns, rIt, label="Rust Iterative", color="orange", linewidth=1)
plt.plot(ns, rMem, label="Rust Memoization", color="purple", linestyle="--", linewidth=1)
plt.xlabel("N")
plt.ylabel("Time (ms)")
plt.title("Iterative vs Memoization: C and Rust (N=1 to N=999)")
plt.legend()
plt.tight_layout()
plt.savefig("linear_race.png", dpi=150)
print("Saved linear_race.png")