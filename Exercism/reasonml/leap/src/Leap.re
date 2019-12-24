/* You can create your own operators */
let (%%) = (x, y) => x mod y == 0;

let isLeapYear = year =>
  switch (year) {
  | _ when year %% 400 => true
  | _ when year %% 100 => false
  | _ when year %% 4 => true
  | _ => false
};

