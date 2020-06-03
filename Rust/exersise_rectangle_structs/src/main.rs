// The Debug derictive makes pretty printing possible
#[derive(Debug)]
struct Rectangle {
    width: i32,
    height: i32,
}

fn main() {
    let r = Rectangle {
        width: 30,
        height: 50
    };
    println!("rect = {:#?}", &r);
    println!("area = {}", calc_area(&r));
}

fn calc_area(r: &Rectangle) -> i32 {
    r.width * r.height
}
