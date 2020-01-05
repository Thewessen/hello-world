let rec splitInt = n =>
  switch (n) {
  | 0 => []
  | _ => [(n mod 10), ...splitInt(n / 10)]
  };
  

let lenInt = number => number->string_of_int->String.length
let pow = (exp, base) => (base->float_of_int) ** (exp->float_of_int)
  |> int_of_float

let validate = number => {
  let len = number->lenInt
  number
    |> splitInt
    |> List.map(pow @@ len)
    |> List.fold_left((+), 0)
    |> (==)(number)
}
