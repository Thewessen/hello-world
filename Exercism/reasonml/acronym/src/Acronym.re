let abbreviate = name => name
 |> String.uppercase_ascii
 |> Js.String.match([%re "/\\b\w/g"])
 |> fun
   | None => ""
   | Some(initials) => initials |> Array.fold_left((++), "")
