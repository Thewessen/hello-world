pub fn brackets_are_balanced(string: &str) -> bool {
    let mut stack: Vec<char> = Vec::new();
    string.chars().all(|ch| match ch {
        '}'|')'|']' => match_brackets(stack.pop(), ch),
        '{'|'('|'[' => {
            stack.push(ch);
            true
        },
        _ => true
    }) && stack.is_empty()
}

fn match_brackets(opt_ch: Option<char>, ch: char) -> bool {
    match opt_ch {
        Some('{') => ch == '}',
        Some('(') => ch == ')',
        Some('[') => ch == ']',
        _ => false
    }
}
