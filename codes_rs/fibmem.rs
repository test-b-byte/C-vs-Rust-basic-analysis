use std::collections::HashMap;

//Unlike C, Rust uses a Hashmap, but to me the process isnt wildly different.
//Receives n(arg[1]) from terminal-main, iterates step by step to n-th term
//Operations counter present. Memo array is received, and space to count operations.
// if the calculation is made it deposits in into the index of memo so it gets spotted next time around.
fn fibmem(n: u64, memo: &mut HashMap<u64, u64>, op_c: &mut u64) -> u64 { 
    if n <= 2 {return 1;}
    if let Some(val) = memo.get(&n) {
        return *val;
    }
    let current = fibmem(n-1, memo, op_c) + fibmem(n-2, memo, op_c);
    *op_c +=1;
    memo.insert(n, current);
    current
    }


    /* functionally no different from the c versions. */
fn main() {
    let args: Vec<String> = std::env::args().collect();
    let n: u64 = args[1].parse().unwrap();
    let mut memo = HashMap::new();
    let mut op_c: u64 = 0;
    let start = std::time::Instant::now();
    for i in 1..=n {
        println!("term {}: {}", i, fibmem(i, &mut memo, &mut op_c));
    }
    let duration = start.elapsed();
    println!("Time: {}", duration.as_secs_f64());
    println!("Total Operations: {}", op_c);
}