fn fibrec(n: u64, op_c: &mut u64) -> u64 {
    if n <= 2 {return 1;}
    let x: u64 = fibrec(n-1, op_c) + fibrec(n-2, op_c);
    *op_c +=1;
    x
}
    /* functionally no different from the c versions. */
fn main() {
    let args: Vec<String> = std::env::args().collect();
    let n: u64 = args[1].parse().unwrap();
    let mut op_c: u64 = 0;
    let start = std::time::Instant::now();
    for i in 1..=n {
        println!("term {}: {}", i, fibrec(i, &mut op_c));
    }
    let duration = start.elapsed();
    println!("Time: {}", duration.as_secs_f64());
    println!("Total Operations: {}", op_c);
}