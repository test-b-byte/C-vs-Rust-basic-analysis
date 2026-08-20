fn fibit(n: u64, op_c: &mut u64) -> u64 {
    if n <= 2 { return 1; }
    let mut n_1: u64 = 1;
    let mut n_2: u64 = 1;
    for _i in 3..=n {
        let current = n_1 + n_2;
        *op_c += 1;
        n_1 = n_2;
        n_2 = current;
    }
    n_2
}

fn main() {
    let mut op_c: u64 = 0;
    let mut passed = 0;
    if fibit(1, &mut op_c) == 1                      { println!("test 1 passed"); passed += 1; }
    if fibit(2, &mut op_c) == 1                      { println!("test 2 passed"); passed += 1; }
    if fibit(7, &mut op_c) == 13                     { println!("test 3 passed"); passed += 1; }
    if fibit(10, &mut op_c) == 55                    { println!("test 4 passed"); passed += 1; }
    if fibit(20, &mut op_c) == 6765                  { println!("test 5 passed"); passed += 1; }
    if fibit(93, &mut op_c) == 12200160415121876738  { println!("test 6 passed"); passed += 1; }
    println!("{}/6 tests passed.", passed);
}
