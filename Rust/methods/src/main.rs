use methods::Rectangle;

fn main() {
    let r1 = Rectangle {
        width: 30,
        height: 50
    };
    let r2 = Rectangle {
        width: 20,
        height: 40
    };
    let r3 = Rectangle {
        width: 10,
        height: 60
    };
    println!("rect1 = {:#?}", &r1);
    println!("rect2 = {:#?}", &r2);
    println!("rect3 = {:#?}", &r3);
    println!("area r1 = {}", r1.area());
    println!("can rect1 hold rect2? {}", r1.can_hold(&r2));
    println!("can rect1 hold rect3? {}", r1.can_hold(&r3));

    println!("This is a square: {:#?}", Rectangle::square(10));
    // automatic referencing and dereferincing
    // (no need for r->area())
    // or (&r).area()
}
