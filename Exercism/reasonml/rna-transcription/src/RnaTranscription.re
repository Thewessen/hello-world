type dna =
  | A
  | C
  | G
  | T;

type rna =
  | A
  | C
  | G
  | U;

let transToRna = (nucleo: dna) =>
  switch(nucleo) {
    | G => C
    | C => G
    | T => A
    | A => U
  };

let toRna = List.map(transToRna);
