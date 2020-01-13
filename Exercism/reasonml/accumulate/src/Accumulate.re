let rec accumulate = f =>
  fun
  | [] => []
  | [a, ...b] => [f(a), ...accumulate(f, b)]
