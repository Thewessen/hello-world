let (%%) = (x, y) => x mod y == 0

let hasSound = (number, (value, sound)) =>
  number %% value ? sound : ""

let raindrops = (number) =>
  [(3, "Pling"), (5, "Plang"), (7, "Plong")]
  |> (List.map @@ hasSound @@ number)
  |> String.concat("")
  |> result => switch(result) {
    | "" => string_of_int(number)
    | _ => result
  };
