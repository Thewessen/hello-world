let get = (mines, x, y) =>
  switch (mines[x].[y]) {
  | exception Invalid_argument(_) => ' '
  | m => m
  }

let sur = (x, y, mines) => [
  (0, 1),
  (1, 1),
  (1, 0),
  (1, -1),
  (0, -1),
  (-1, -1),
  (-1, 0),
  (-1, 1)
] |> List.map(((dx, dy)) => mines->get(x + dx, y + dy))

let count = (char, surr) => surr
  |> List.filter(c => c == char)
  |> List.length

let annotate = mines => mines
  |> Array.mapi((x, row) => row
    |> String.mapi((y, char) =>
      switch(char) {
      | '*' => char
      | _ => mines
        |> sur(x, y)
        |> count('*')
        |> string_of_int
        |. String.get(0)
        |> char => char == '0' ? ' ' : char
      })
  )
