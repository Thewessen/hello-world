use std::iter::FromIterator;

pub fn brackets_are_balanced(string: &str) -> bool {
    let brackets = (*string)
        .chars()
        .filter(|ch| ['{','}','[',']','(',')'].contains(ch));
    matching_brackets(String::from_iter(brackets))
}

fn matching_brackets(string: String) -> bool {
    if string.contains("{}") {
        matching_brackets(string.replace("{}", ""))
    } else if string.contains("[]") {
        matching_brackets(string.replace("[]", ""))
    } else if string.contains("()") {
        matching_brackets(string.replace("()", ""))
    } else {
        string.is_empty()
    }
}
