let allergies = [
  "eggs",
  "peanuts",
  "shellfish",
  "strawberries",
  "tomatoes",
  "chocolate",
  "pollen",
  "cats",
]

let rec filterBin = (n, l) =>
  switch (l) {
    | [] => []
    | [head, ...tail] =>
      switch(n mod 2 == 1) {
      | true => [head, ...filterBin(n / 2, tail)]
      | false => filterBin(n / 2, tail)
      }
    }

let toList = (i) => allergies |> filterBin(i)

let isAllergicTo = (str, i) => toList(i) |> List.mem(str)
