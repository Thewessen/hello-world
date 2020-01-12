let tail = (str, n) => String.sub(str, n, String.length(str) - n)

let rec encode = str =>
  switch (str|>Js.String.match([%re "/(\D)(\1*)/"])) {
  | None => ""
  | Some([| f, g1, g2 |]) => g1
      |> (++)(g2 == "" ? "" : String.length(f)->string_of_int)
      |. (++)(str->tail(String.length(f))->encode)
  }

let rec decode = str =>
  switch(str|>Js.String.match([%re "/(\d*)(\D)/"])) {
  | None => ""
  | Some([| f, g1, g2 |]) => g2.[0]
    |> String.make(g1 == "" ? 1 : int_of_string(g1))
    |. (++)(str->tail(String.length(f))->decode)
  }
