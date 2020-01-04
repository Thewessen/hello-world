let count = (dict, word) => {
  switch(Js.Dict.get(dict, word)) {
    | Some(result) => Js.Dict.set(dict, word, result + 1)
    | None => Js.Dict.set(dict, word, 1)
  };
  dict
};

let wordCount = (sentence) => sentence
  |> String.lowercase_ascii
  |> Js.String.replaceByRe([%re "/[^a-z0-9' ]+| '|' /g"], " ")
  |> Js.String.replaceByRe([%re "/ +/g"], " ")
  |> String.trim
  |> Js.String.split(" ")
  |> Js.Array.reduce(count, Js.Dict.empty())
