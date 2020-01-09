type planet =
  | Mercury
  | Venus
  | Earth
  | Mars
  | Jupiter
  | Saturn
  | Neptune
  | Uranus;


let ageOn = (planet, sec) => {
  let earthSec = 31557600.0
  let fromEarth = (fact) => sec /. (earthSec *. fact)
  
  switch(planet) {
  | Mercury => fromEarth(0.2408467)
  | Venus => fromEarth(0.61519726)
  | Earth => fromEarth(1.0)
  | Mars => fromEarth(1.8808158)
  | Jupiter => fromEarth(11.862615)
  | Saturn => fromEarth(29.447498)
  | Neptune => fromEarth(164.79132)
  | Uranus => fromEarth(84.016846)
  }
}
