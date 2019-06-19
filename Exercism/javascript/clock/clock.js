'use strict'

const MINSINHOUR = 60
const HOURSINDAY = 24

const grepHours = (min) => {
  if (min < 0) {
    return -1 + grepHours(min + MINSINHOUR)
  } else if (min >= MINSINHOUR) {
    return 1 + grepHours(min - MINSINHOUR)
  } else {
    return 0
  }
}

const convert = (time, too) => {
  let mod = time % too
  return mod < 0
    ? too + mod
    : mod
}

class Clock {
  constructor (h = 0, m = 0) {
    this.time = [h, m]
  }

  set time (value) {
    let [
      h = this.hours,
      m = this.minutes
    ] = value
    this.hours = convert(h + grepHours(m), HOURSINDAY)
    this.minutes = convert(m, MINSINHOUR)
  }

  toString () {
    return [this.hours, this.minutes]
      .map((t) => t.toString())
      .map((t) => t.padStart(2, '0'))
      .join(':')
  }

  plus (m) {
    this.time = [, this.minutes + m]
    return this
  }

  minus (m) {
    this.time = [, this.minutes - m]
    return this
  }

  equals (obj) {
    return this.toString() === obj.toString()
  }
}

export const at = (h = 0, m = 0) => new Clock(h, m)
