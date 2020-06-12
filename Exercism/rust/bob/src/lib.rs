pub fn reply(message: &str) -> &str {
    match Say::from(message) {
        Say::Yell         => "Whoa, chill out!",
        Say::Question     => "Sure.",
        Say::Silent       => "Fine. Be that way!",
        Say::AnythingElse => "Whatever.",
        Say::YellQuestion =>
            "Calm down, I know what I'm doing!",
    }
}

enum Say {
    YellQuestion,
    Yell,
    Question,
    Silent,
    AnythingElse,
}

impl From<&str> for Say {
    fn from(msg: &str) -> Say {
        if is_silent(msg) {
            Say::Silent
        }
        else if is_yell(msg) && is_question(msg) {
            Say::YellQuestion
        }
        else if is_yell(msg) {
            Say::Yell
        }
        else if is_question(msg) {
            Say::Question
        }
        else {
            Say::AnythingElse
        }
    }
}

fn is_question(msg: &str) -> bool {
    msg.trim().ends_with('?')
}

fn is_yell(msg: &str) -> bool {
    msg.chars().all(|ch| !ch.is_ascii_lowercase()) &&
    msg.chars().any(|ch| ch.is_ascii_uppercase())
}

fn is_silent(msg: &str) -> bool {
    msg.chars().all(|ch| ch.is_ascii_whitespace())
}
