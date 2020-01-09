let phoneNumber = (nr) => nr
  |> Js.String.replaceByRe([%re "/[^0-9]/g"], "")
  |> Js.String.match([%re "/^1?((?:[2-9][0-9]{2}){2}[0-9]{4})$/"])
  |. Belt.Option.map(r => r[1])
