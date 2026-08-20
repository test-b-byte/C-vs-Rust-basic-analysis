import subprocess
import csv
import time

ns = list(range(1, 60))
total_budget = 60  # seconds total per language

programs = {
    "C Recursive":    "./codes_c/fibrec.out",
    "Rust Recursive": "./codes_rs/fibrec",
}

def run_language(name, prog):
    results = {}
    elapsed_total = 0
    for n in ns:
        start = time.time()
        try:
            subprocess.run([prog, str(n)], capture_output=True, text=True,
                           timeout=total_budget - elapsed_total)
        except subprocess.TimeoutExpired:
            print(f"{name} timed out at n={n}")
            break
        elapsed = time.time() - start
        elapsed_total += elapsed
        results[n] = round(elapsed, 4)
        print(f"{name} n={n}: {elapsed:.4f}s (total {elapsed_total:.2f}s)")
        if elapsed_total >= total_budget:
            print(f"{name} budget exhausted at n={n}")
            break
    return results

c_results = run_language("C Recursive", programs["C Recursive"])
rust_results = run_language("Rust Recursive", programs["Rust Recursive"])

all_ns = sorted(set(c_results.keys()) | set(rust_results.keys()))
rows = [[n, c_results.get(n, "DNF"), rust_results.get(n, "DNF")] for n in all_ns]

with open("rec_times.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "C Time (s)", "Rust Time (s)"])
    writer.writerows(rows)

print("Done. rec_times.csv written.")

import matplotlib.pyplot as plt

c_ns = [r[0] for r in rows if r[1] != "DNF"]
c_times = [r[1] for r in rows if r[1] != "DNF"]
rust_ns = [r[0] for r in rows if r[2] != "DNF"]
rust_times = [r[2] for r in rows if r[2] != "DNF"]

plt.figure(figsize=(10, 6))
plt.plot(c_ns, c_times, label="C Recursive", color="blue")
plt.plot(rust_ns, rust_times, label="Rust Recursive", color="orange")
plt.xlabel("N")
plt.ylabel("Time (seconds)")
plt.title("Recursive Fibonacci: C vs Rust (60s budget)")
plt.legend()
plt.savefig("rec_race.png")
print("Graph saved as rec_race.png")