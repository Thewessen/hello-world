type coins = list(int);

let min = (a, b) => List.length(a) < List.length(b) ? a : b

let makeChange = (value, change) => {
  let rec make = results =>
    fun
    | [] => results
    | [coin, ...rest] => results
      |> Array.iteri(
        fun
        | 0 => (_) => results[0] = Some([])
        | i when i < coin => (_) => ()
        | i => r =>
          switch(results[i - coin], r) {
          | (None, _) => ()
          | (Some(prev), None) => results[i] = Some(prev @ [coin])
          | (Some(prev), Some(curr)) => results[i] = Some(min(prev @ [coin], curr))
          }
      )
    |> () => make(results, rest)

  value < 0 ? None :
  make(Array.make(value + 1, None), change)[value]
}
