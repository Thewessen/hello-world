use control_flow::fibbonaci;

#[allow(unused_variables)]
fn main() {
    let b = if_else(10);
    keep_looping();
    return_from_loop();
    while_loop();
    lift_off();
    combined_lift_off();
    fibbonaci();
}

fn if_else(x: i32) -> bool {
    // if-else is an expression!
    let boolean = if x < 5 {
        println!("Too small!");
        false
    } else if x == 5 {
        println!("You win!");
        true
    } else {
        println!("Too large");
        false
    };
    boolean
}

fn keep_looping() {
    loop {
        println!("again!");
        break;
    }
    println!("only once");
}

fn return_from_loop() {
    let mut counter: i32 = 0;
    // the exit is not needed (but nicer)
    let x = 'exit: loop {
        counter += 1;
        if counter == 10 {
            break 'exit counter * 2;
        }
    };
    println!("The value of x is {}", x);
}

fn while_loop() {
    let mut number: i32 = 3;
    while number != 0 {
        println!("{}", number);
        number -= 1;
    }
    println!("LIFT OFF!");
}

fn lift_off() {
    let a: [u32; 3] = [3, 2, 1];
    for element in a.iter() {
        println!("{}", element);
    }
    println!("LIFT OFF!");
}

fn combined_lift_off() {
    for element in (1..=3).rev() {
        println!("{}", element);
    }
    println!("LIFT OFF!");
}
