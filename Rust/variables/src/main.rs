fn mutable() {
    let mut x = 5;
    println!("The value of x is: {}", x);

    x = 6;
    println!("The value of x is: {}", x);

    // not allowed!
    // let mut spaces = "   ";
    // spaces = spaces.len();
}

fn shadowing() {
    let x = 5;
    let x = x + 1;
    let x = x * 2;
    println!("The value of x is: {}", x);

    // allowed!
    let spaces = "   ";
    let spaces = spaces.len();
    println!("Number of spaces is {}", spaces);
}

fn main() {
    _title("mutable variables");
    mutable();
    _title("shadowing variables");
    shadowing();
}

fn _title(title: &str) {
    println!("+------------------------+");
    println!("{}", title);
    println!("+------------------------+");
}
