#![allow(dead_code, unused_variables)]
fn main() {
    structs();
    tuple_structs();
}

#[derive(Debug)]
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

fn structs() {
    
    let mut user1 = build_user(
        String::from("someone@example.com"),
        String::from("someusername123")
    );

    // Change one prop
    // user1 has to be mutable!
    user1.email = String::from("anotheremail@example.com");

    // Struct update syntax
    // use user1 to create user2
    let user2 = User {
        username: String::from("someoneelse456"),
        email: String::from("someoneelse@example.com"),
        ..user1
    };

    println!("User 1: {:#?}", user1);
    println!("User 2: {:#?}", user2);
}

fn build_user(email: String, username: String) -> User {
    // Field init shorthand
    // when params have the same name as props
    // like Javascript
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}

// tuple structs
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn tuple_structs() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);

    print_color(black);
    // print_color(origin); // ERROR origin not a color
}

fn print_color(c: Color) {
    println!("{} {} {}", c.0, c.1, c.2);
}

// unit like structs
struct UnitType ();
