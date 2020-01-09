let is_isogram = (word) => word
  |> String.lowercase_ascii
  |> Js.String.replaceByRe([%re "/[^a-z]/g"], "")
  |> Js.Re.test_([%re "/([a-z]).*\1/g"])
  |> (!)
