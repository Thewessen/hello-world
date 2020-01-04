let isQuestion = (sentence) => sentence |> Js.Re.test_([%re "/\\?$/"])
let isYell = (sentence) => sentence |> Js.Re.test_([%re "/^[^a-z]*[A-Z][^a-z]*$/"])
let isYellQuestion = (sentence) => isQuestion(sentence) && isYell(sentence)

let hey = (say) =>
  switch (say |> String.trim) {
    | "" => "Fine. Be that way!"
    | str when str->isYellQuestion => "Calm down, I know what I'm doing!"
    | str when str->isQuestion => "Sure."
    | str when str->isYell => "Whoa, chill out!"
    | _ => "Whatever."
  };
