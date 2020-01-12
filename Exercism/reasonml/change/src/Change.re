type coins = list(int);

let min = (a, b) => List.length(a) < List.length(b) ? a : b

let makeChange = (value, change) => {
  let rec make = (result: array(option(coins)), ch: coins): array(option(coins)) =>
    switch (ch) {
    | [] => result
    | [coin, ...rest] => result
      |> Array.iteri((i, r) => {
        if (i >= coin) {
          switch(result[i - coin], r) {
          | (None, _) => ()
          | (Some(l), None) =>
              Array.unsafe_set(result, i, Some(l @ [coin]))
          | (Some(l), Some(r)) =>
              Array.unsafe_set(result, i, Some(min(l @ [coin], r)))
          }
        }
      })
    |> () => make(result, rest)
  }

  value < 0 ? None :
  make(Array.make(value + 1, Some([])), change)[value]
}
