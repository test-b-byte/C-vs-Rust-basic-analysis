import subprocess
import csv

results = []
ns = [5, 10, 15, 20, 25, 30]
rec_ns = [5, 10, 15, 20, 25, 30]

programs = [
    ("C Iterative", "./codes_c/fibit.out"),
    ("C Memoization", "./codes_c/fibmem.out"),
    ("Rust Iterative", "./codes_rs/fibit"),
    ("Rust Memoization", "./codes_rs/fibmem"),
]

rec_programs = [
    ("C Recursive", "./codes_c/fibrec.out"),
    ("Rust Recursive", "./codes_rs/fibrec"),
]

for name, prog in programs:
    for n in ns:
        out = subprocess.run([prog, str(n)], capture_output=True, text=True).stdout
        lines = out.strip().split("\n")
        time_line = [l for l in lines if "Time" in l][0]
        ops_line = [l for l in lines if "Operations" in l][0]
        results.append([name, n, time_line.split(":")[1].strip(), ops_line.split(":")[1].strip()])

for name, prog in rec_programs:
    for n in rec_ns:
        out = subprocess.run([prog, str(n)], capture_output=True, text=True).stdout
        lines = out.strip().split("\n")
        time_line = [l for l in lines if "Time" in l][0]
        ops_line = [l for l in lines if "Operations" in l][0]
        results.append([name, n, time_line.split(":")[1].strip(), ops_line.split(":")[1].strip()])

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Implementation", "N", "Time", "Operations"])
    writer.writerows(results)

print("Done. results.csv written.")