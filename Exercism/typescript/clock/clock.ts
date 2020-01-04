const MINSINHOUR = 60
const HOURSINDAY = 24

const grepHours = (min: number): number => {
  if (min < 0) {
    return -1 + grepHours(min + MINSINHOUR)
  } else if (min >= MINSINHOUR) {
    return 1 + grepHours(min - MINSINHOUR)
  } else {
    return 0
  }
}

const convert = (time: number, too: number): number => {
  const mod = time % too
  return mod < 0
    ? too + mod
    : mod
}

export default class Clock {
  constructor (private hours = 0, private minutes = 0) {
    this.sanitize()
  }

  sanitize(): void {
    const h = this.hours
    const m = this.minutes
    this.hours = convert(h + grepHours(m), HOURSINDAY)
    this.minutes = convert(m, MINSINHOUR)
  }

  toString (): string {
    return [this.hours, this.minutes]
      .map((t) => t.toString())
      .map((t) => t.padStart(2, '0'))
      .join(':')
  }

  plus (m: number): Clock {
    this.minutes += m
    this.sanitize()
    return this
  }

  minus (m: number): Clock {
    this.minutes -= m
    this.sanitize()
    return this
  }

  equals (clock: Clock): boolean {
    return this.toString() === clock.toString()
  }
}
