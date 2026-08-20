fn fibrec(n: u64, op_c: &mut u64) -> u64 {
    if n <= 2 { return 1; }
    let x: u64 = fibrec(n-1, op_c) + fibrec(n-2, op_c);
    *op_c += 1;
    x
}

fn main() {
    let mut op_c: u64 = 0;
    let mut passed = 0;
    if fibrec(1, &mut op_c) == 1    { println!("test 1 passed"); passed += 1; }
    if fibrec(2, &mut op_c) == 1    { println!("test 2 passed"); passed += 1; }
    if fibrec(7, &mut op_c) == 13   { println!("test 3 passed"); passed += 1; }
    if fibrec(10, &mut op_c) == 55  { println!("test 4 passed"); passed += 1; }
    if fibrec(20, &mut op_c) == 6765{ println!("test 5 passed"); passed += 1; }
    println!("{}/5 tests passed.", passed);
}
