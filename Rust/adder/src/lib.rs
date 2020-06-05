#[cfg(test)]
mod tests {
    // #[test]
    // fn it_works() {
    //     assert_eq!(2 + 2, 4);
    // }

    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two should be four"))
        }
    }

    #[test]
    #[should_panic(expected = "test fail")]
    fn it_fails() {
        panic!("Make this test fail");
    }
}
