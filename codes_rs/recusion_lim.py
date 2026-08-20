import subprocess
import csv

ns = list(range(1, 40))
timeout_seconds = 60

programs = {
    "C Recursive":    "./codes_c/fibrec.out",
    "Rust Recursive": "./codes_rs/fibrec",
}

def get_ops(prog, n):
    try:
        out = subprocess.run(
            [prog, str(n)],
            capture_output=True,
            text=True,
            timeout=timeout_seconds
        ).stdout
        for line in out.strip().split("\n"):
            if "Operations" in line:
                return line.split(":")[1].strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    return ""

rows = []
for n in ns:
    c_ops = get_ops(programs["C Recursive"], n)
    rust_ops = get_ops(programs["Rust Recursive"], n)
    rows.append([n, c_ops, rust_ops])
    print(f"n={n}: C={c_ops}, Rust={rust_ops}")
    if c_ops == "TIMEOUT" and rust_ops == "TIMEOUT":
        break

with open("rec_comparison.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["N", "C Recursive", "Rust Recursive"])
    writer.writerows(rows)

print("Done. rec_comparison.csv written.")