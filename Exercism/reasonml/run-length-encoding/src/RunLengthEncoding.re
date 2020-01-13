let tail = (str, n) => String.sub(str, n, String.length(str) - n)

let rec code = (regex, fn, str) =>
  switch (str|>Js.String.match(regex)) {
  | None => ""
  | Some(result) => fn(result)
    |. (++)(str->tail(String.length(result[0]))|>code(regex, fn))
  }

let encode = code([%re "/(\D)(\1*)/"], ([| f, g1, g2 |]) => g1
      |> (++)(g2 == "" ? "" : String.length(f)->string_of_int))

let decode = code([%re "/(\d*)(\D)/"], ([| _, g1, g2 |]) => g2.[0]
    |> String.make(g1 == "" ? 1 : int_of_string(g1)))
