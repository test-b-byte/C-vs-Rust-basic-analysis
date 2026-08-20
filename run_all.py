import subprocess
import csv

ns = list(range(1, 31))


programs = {
    "C Iterative":      "./codes_c/fibit.out",
    "C Recursive":      "./codes_c/fibrec.out",
    "C Memoization":    "./codes_c/fibmem.out",
    "Rust Iterative":   "./codes_rs/fibit",
    "Rust Recursive":   "./codes_rs/fibrec",
    "Rust Memoization": "./codes_rs/fibmem",
}

def get_ops(prog, n):
    out = subprocess.run([prog, str(n)], capture_output=True, text=True).stdout
    for line in out.strip().split("\n"):
        if "Operations" in line:
            return line.split(":")[1].strip()
    return ""

rows = []
for n in ns:
    row = [n]
    for name, prog in programs.items():
            row.append(get_ops(prog, n))
    rows.append(row)

headers = ["N"] + list(programs.keys())

with open("ops_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print("Done. ops_results.csv written.")