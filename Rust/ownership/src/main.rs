fn main() {
    // String class is stored on the heap (variable size)
    let mut s = String::from("hello");
    s.push_str(", world!");
    println!("{}", s);
    move_vs_copy();
    function_and_ownership();
    function_return_ownership();
}

fn move_vs_copy() {
    // Borrow of moved value error: s1 was moved to s2
    // let s1 = String::from("hello");
    // let s2 = s1;

    // correct (but expensive)
    let s1 = String::from("hello");
    let s2 = s1.clone();
    println!("s1 = {}, s2 = {}", s1, s2);

    // values that are stored on the stack (fixed size) dont have that problem
    // i32.., u32.., bool, f62.., tupple of those
    let x = 5;
    let y = x;
    println!("x = {}, y = {}", x, y);
}

// this is the same for function calls...
fn function_and_ownership() {
    // let s = String::from("hello");
    // print_string(s);
    // s is no longer valid here...
    // println!("s = {}", s);

    let s = String::from("hello");
    print_string(s.clone());
    println!("s = {}", s);

    let x = 5;
    print_int(x);
    println!("x = {}", x);
}

fn print_string(s: String) {
    println!("s = {}", s);
}

fn print_int(x: i32) {
    println!("x = {}", x);
}

fn function_return_ownership() {
    let s1 = gives_ownership();
    let s2 = takes_ownership_and_gives_back(s1);
    println!("s2 = {}", s2);
}

// Function and there returns
fn gives_ownership() -> String {
    let s = String::from("hello");
    s
}

fn takes_ownership_and_gives_back(s: String) -> String {
    s
}
