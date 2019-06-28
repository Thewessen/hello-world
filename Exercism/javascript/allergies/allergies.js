'use strict'

const ALLERGIES = [
  'eggs',
  'peanuts',
  'shellfish',
  'strawberries',
  'tomatoes',
  'chocolate',
  'pollen',
  'cats'
]

export class Allergies {
  constructor (score) {
    if (!Number.isInteger(score)) {
      throw new Error('Score is not an integer')
    }

    const gen = score
      .toString(2)
      .split('')
      .reverse()
      .map(Number)

    this.allergens = ALLERGIES
      .filter((e, i) => !!gen[i])
  }

  list () {
    return this.allergens
  }

  allergicTo (allergy) {
    return this.allergens.includes(allergy)
  }
}
