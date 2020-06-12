use matching_brackets::brackets_are_balanced;

fn main() {
    let string = String::from("[hello]");
    println!("{}", brackets_are_balanced(&string));
}
