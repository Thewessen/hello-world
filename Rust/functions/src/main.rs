fn main() {
    defined_after();
    params(5, -10);
    let z = {
        let n = 3;
        expression_end(n)
    };

    println!("The value of z is {}", z);
}

fn expression_end(x: i32) -> i32 {
    x + 5
}

fn params(x: u32, y: i32) {
    println!("The value of x is {}", x);
    println!("The value of y is {}", y);
}

fn defined_after() {
    println!("Rust doesn't care!");
}
