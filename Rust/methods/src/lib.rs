#[derive(Debug)]
pub struct Rectangle {
    pub width: i32,
    pub height: i32,
}

impl Rectangle {
    pub fn area(&self) -> i32 {
        self.width * self.height
    }

    pub fn can_hold(&self, r: &Rectangle) -> bool {
        self.width > r.width && self.height > r.height
    }

    // associate functions!
    pub fn square(size: i32) -> Rectangle {
        Rectangle {
            width: size,
            height: size
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(larger.can_hold(&smaller));
    }

    #[test]
    fn smaller_can_not_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };
        assert!(!smaller.can_hold(&larger));
    }

    #[test]
    fn should_construct_square() {
        let square = Rectangle::square(5);
        assert_eq!(
            square.width,
            square.height,
            "A square should have equal width and height, square: {:#?}",
            square,
        );
    }
}

