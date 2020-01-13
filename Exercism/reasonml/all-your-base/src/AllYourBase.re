let rec (**) = (a: int) =>
  fun
  | 0 => 1
  | b => a * (a ** (b - 1))

let rec toBase = _to =>
  fun
  | 0 => []
  | n => toBase(_to, n / _to) @ [n mod _to]

let fromBase = (_from, digits) => digits
  |> List.rev
  |> List.mapi((i, v) => v * _from ** i)
  |> List.fold_left((+), 0)

let rebase = _from =>
  fun
  | digits when (
      List.exists((<=)(_from), digits) ||
      List.exists((>)(0), digits) ||
      List.fold_left((+), 0, digits) == 0
    ) => (_) => None
  | digits =>
    fun
    | _to when _to <= 0 => None
    | _to => digits
      |> fromBase(_from)
      |> toBase(_to)
      |> result => Some(result)
