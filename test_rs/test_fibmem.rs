use std::collections::HashMap;

fn fibmem(n: u64, memo: &mut HashMap<u64, u64>, op_c: &mut u64) -> u64 {
    if n <= 2 { return 1; }
    if let Some(val) = memo.get(&n) { return *val; }
    let current = fibmem(n-1, memo, op_c) + fibmem(n-2, memo, op_c);
    *op_c += 1;
    memo.insert(n, current);
    current
}

fn main() {
    let mut memo = HashMap::new();
    let mut op_c: u64 = 0;
    let mut passed = 0;
    if fibmem(1, &mut memo, &mut op_c) == 1                     { println!("test 1 passed"); passed += 1; }
    if fibmem(2, &mut memo, &mut op_c) == 1                     { println!("test 2 passed"); passed += 1; }
    if fibmem(7, &mut memo, &mut op_c) == 13                    { println!("test 3 passed"); passed += 1; }
    if fibmem(10, &mut memo, &mut op_c) == 55                   { println!("test 4 passed"); passed += 1; }
    if fibmem(20, &mut memo, &mut op_c) == 6765                 { println!("test 5 passed"); passed += 1; }
    if fibmem(93, &mut memo, &mut op_c) == 12200160415121876738 { println!("test 6 passed"); passed += 1; }
    println!("{}/6 tests passed.", passed);
}
