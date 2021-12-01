// use matching_brackets::sol1::brackets_are_balanced;
use matching_brackets::sol2::brackets_are_balanced;

fn main() {
    let string = String::from("[hello]");
    println!("{}", brackets_are_balanced(&string));
}
