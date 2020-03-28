pub fn fibbonaci() {
    fn memo(x: u32, y: u32) {
        println!("{}", x + y);
        memo(y, x + y);
    }
    memo(0, 1);
}
