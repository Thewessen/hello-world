let head = (arr, n) => Array.sub(arr, 0, n)
let tail = (arr, n) => Array.sub(arr, n, Array.length(arr) - n)

let rec find = (arr, n) => {
  switch(Array.length(arr)) {
    | 0 => None
    | i => switch(compare(arr[i / 2], n)) {
            | 0 => Some(i / 2)
            | 1 => find(arr->head(i / 2), n)
            | -1 => switch(find(arr->tail(succ(i / 2)), n)) {
                    | Some(a) => Some(a + succ(i / 2))
                    | _ => None
                    }
            | _ => None
            }
    }
}
