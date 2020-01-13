let codonToProtein =
  fun
  | "AUG" => "Methionine"
  | "UUU"
  | "UUC" => "Phenylalanine"
  | "UUA"
  | "UUG" => "Leucine"
  | "UCU"
  | "UCC"
  | "UCA"
  | "UCG"	=> "Serine"
  | "UAU"
  | "UAC"	=> "Tyrosine"
  | "UGU"
  | "UGC"	=> "Cysteine"
  | "UGG"	=> "Tryptophan"
  | _	=> "STOP"

let rec proteins = rna =>
  switch(rna->String.sub(0, 3)->codonToProtein) {
  | exception Invalid_argument(_) => []
  | "STOP" => []
  | protein => [protein, ...proteins(rna->String.sub(3, String.length(rna) - 3))]
  }
