#![allow(unused_variables)]
fn main() {
    let s1 = String::from("hello");

    // give calculate_length a reference to s1
    let len = calculate_length(&s1);

    // s1 is still useable here
    println!("The length of '{}' is {}.", s1, len);

    // rules
    only_one_mut_ref();
    no_mut_and_imut_same_time();
    // let reference_to_nothing = dangle();
    let reference_to_something = no_dangle();
}

fn calculate_length(s: &String) -> usize {
    // cannot mutate s!
    // s.push_str(", world!");

    s.len()
}

fn only_one_mut_ref() {
    let mut s = String::from("hello");

    // only one mutable reference to a particular piece of data in a particular scope
    {
        let r1 = &mut s;
    }
    let r2 = &mut s;

    println!("r1 = {}", r2);
}

#[allow(unused_mut)]
fn no_mut_and_imut_same_time() {
    let mut s = String::from("hello");

    // cannot have a mutable reference while we have an immutable one
    let r1 = &s;
    // let r2 = &mut s;
    println!("r1 = {}", r1);
}


//fn dangle() -> &String { // dangle returns a reference to a String
fn no_dangle() -> String { // the solution is to return a string

    let s = String::from("hello");

    // &s // we return a reference to the String, s
    s // this is ok, ownership is moved out of scope
} // Here, s goes out of scope, and is dropped. Its memory goes away.
  // Danger!
