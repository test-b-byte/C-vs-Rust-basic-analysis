fn fibit(n: u64, op_c: &mut u64) -> u64 {
    if n <= 2 { return 1;}
    let mut n_1: u64 =1;
    let mut n_2: u64 =1;

// learning for loop notation in rust. a bit different and has some peices automated instead of articulated ((i++))
    for _i in 3..=n {
        let current = n_1 + n_2;
        *op_c += 1;
        n_1 = n_2;
        n_2= current;
    }
    n_2
}
/*same as the other 5 programs. I figured out how to get rid of the micro seconds in rust. Functionally this is 
just different syntax, its not much different from the c version */
fn main() {
    let args: Vec<String> = std::env::args().collect();
    let n: u64 = args[1].parse().unwrap();
    let mut op_c: u64 = 0;
    let start = std::time::Instant::now();
    for i in 1..=n {
        println!("term {}: {}", i, fibit(i, &mut op_c));
    }
    let duration = start.elapsed();
    println!("Time: {}", duration.as_secs_f64());
    println!("Total Operations: {}", op_c);
}