let isPangram = (sentence) => {
  let s = sentence
    |> String.lowercase_ascii
    |> Js.String.replaceByRe([%re "/[^a-z]/g"], "")

  List.init(26, (+)(Char.code('a')))
    |> List.for_all(c => c|>Char.chr|>String.contains(s))
  }
