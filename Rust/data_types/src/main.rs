fn integers() {
    // note the different ways of writing numbers

    let x: u32 = 5; // 32-bit unsigned integer (default)
    
    let x: u64 = 0xffffff; // 64-bit unsigned integer
    let x: i64 = -198_000; // 64-bit signed integer

    let x: isize = 0b0101_1111; // os dependend size

    let b: u8 = b'A'; // bite (u8 only)

    println!("The value of x is: {}", x);
    println!("The value of b is: {}", b);
}

fn floats() {
    let x = 2.0; // 64-bit float

    let x: f32 = 3.2; // 32-bit float
}

fn operations() {
    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;

    // remainder
    let remainder = 43 % 5;
}

fn chars() {
    let c = 'z';
    println!("{}", c);
    let z = 'ℤ';
    println!("{}", z);
    let heart_eyed_cat = '😻';
    println!("{}", heart_eyed_cat);
}

fn compound() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);

    // indices
    let five_hundred = tup.0;
    let six_point_four = tup.1;
    let one = tup.2;
    println!("Tupple is: ({}, {}, {})", five_hundred, six_point_four, one);

    let array: [i32; 3] = [1, 2, 3];
    let one = array[0];
    let two = array[1];
    let three = array[2];
    println!("Array is: [{}, {}, {}]", one, two, three);

    let a = [3; 5]; // [3, 3, 3, 3, 3]
}

fn main() {
    integers();
    floats();
    operations();
    chars();
    compound();
}
