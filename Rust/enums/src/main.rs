#![allow(dead_code, unused_variables)]
fn main() {
    enum IpAddr {
        V4(u8, u8, u8, u8),
        V6(String),
    }

    let home = IpAddr::V4(127, 0, 0, 1);

    let loopback = IpAddr::V6(String::from("::1"));

    enums();
}

enum Message {
    // just a variant, no data
    Quit,
    // an anonimous struct
    Move { x: i32, y: i32 },
    // a string
    Write(String),
    // three 32-bit integers
    ChangeColor(i32, i32, i32),
}

// enum can have methods!
impl Message {
    fn call(&self) {
        // do something here
    }
}

fn enums() {
    let m = Message::Write(String::from("hello!"));
    m.call();
}
