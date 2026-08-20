import csv
import matplotlib.pyplot as plt

ns, c_times, rust_times = [], [], []

with open("rec_times.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ns.append(int(row["N"]))
        c_times.append(float(row["C Time (s)"]))
        rust_times.append(float(row["Rust Time (s)"]) if row["Rust Time (s)"] != "DNF" else None)

rust_ns = [ns[i] for i in range(len(rust_times)) if rust_times[i] is not None]
rust_vals = [v for v in rust_times if v is not None]

plt.figure(figsize=(10, 6))
plt.plot(ns, c_times, label="C Recursive", color="blue", linewidth=2)
plt.plot(rust_ns, rust_vals, label="Rust Recursive", color="orange", linestyle="--", linewidth=2)
plt.xlabel("N")
plt.ylabel("Time (seconds)")
plt.title("Recursive Fibonacci: C vs Rust (60s budget)")
plt.legend()
plt.tight_layout()
plt.savefig("rec_race.png", dpi=150)
print("Saved rec_race.png")