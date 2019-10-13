'use strict'

import { COLORS, value } from '../resistor-color-duo/resistor-color-duo'

export class ResistorColorTrio {
  constructor([st, nd, rd]) {
    if ([st, nd, rd].some(color => !COLORS.has(color))) {
      throw new Error('Trio contains invalid color!')
    }
    this.value = value([st, nd]) * 10 ** COLORS.get(rd)
  }

  get label() {
    let value = this.value
    let unit = 'ohms'
    if (!(value % 1000)) {
      value /= 1000
      unit = 'kiloohms'
    }
    return `Resistor value: ${value} ${unit}`
  }
}
