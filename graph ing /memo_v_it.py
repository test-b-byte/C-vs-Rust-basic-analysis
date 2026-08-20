import subprocess
import csv
import time

ns = list(range(1, 1000))

programs = {
    "C Iterative":      "./codes_c/fibit.out",
    "C Memoization":    "./codes_c/fibmem.out",
    "Rust Iterative":   "./codes_rs/fibit",
    "Rust Memoization": "./codes_rs/fibmem",
}

def get_time(prog, n):
    start = time.time()
    subprocess.run([prog, str(n)], capture_output=True, text=True)
    return round(time.time() - start, 6)

rows = []
for n in ns:
    row = [n]
    for name, prog in programs.items():
        row.append(get_time(prog, n))
    rows.append(row)
    print(f"n={n}: {row[1:]}")

with open("linear_times.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N"] + list(programs.keys()))
    writer.writerows(rows)

print("Done. linear_times.csv written.")