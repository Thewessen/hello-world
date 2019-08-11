'use strict'

const ALPHA_TO_ROMAN = new Map()
  .set('M', 1000)
  .set('CM', 900)
  .set('D', 500)
  .set('CD', 400)
  .set('C', 100)
  .set('XC', 90)
  .set('L', 50)
  .set('XL', 40)
  .set('X', 10)
  .set('IX', 9)
  .set('V', 5)
  .set('IV', 4)
  .set('I', 1)

export const toRoman = (number) => {
  let result = ''
  for (const [roman, arabic] of ALPHA_TO_ROMAN.entries()) {
    result += roman.repeat(Math.floor(number / arabic))
    number %= arabic
  }
  return result
};
