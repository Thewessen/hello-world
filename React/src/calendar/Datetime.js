const divmod = (c, d) => [Math.floor(c / d), c % d]

const DAY_TO_INT = new Map([
  'Monday',
  'Thuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saterday',
  'Sunday',
].map((day, index) => [day, index]))

const MONTH_TO_INT = new Map([
  'Januari',
  'Februari',
  'March',
  'April',
  'June',
  'Juli',
  'August',
  'September',
  'October',
  'November',
  'December',
].map((month, index) => [month, index]))

const MONTH_SIZE = new Map(
  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    .map((days, index) => [index, days])
)

const ZEROYEAR = 1976
const DAYS_IN_YEAR = [...MONTH_SIZE.values()].reduce((a, b) => a + b)

class InvalidDay extends Error {
  constructor(message = '') {
    super(message)
    this.name = 'InvalidDay'
  }
}

class InvalidMonth extends Error {
  constructor(message = '') {
    super(message)
    this.name = 'InvalidMonth'
  }
}

export default class Datetime {
  constructor(day = 0, month = 0, year = ZEROYEAR) {
    if (day > MONTH_SIZE.get(month)) {
      throw new InvalidDay(`The current month only has ${MONTH_SIZE.get(month)} days`)
    }
    if (day < 0) {
      throw new InvalidDay('Day cannot be negative')
    }
    if (month >= MONTH_SIZE.size) {
      throw new InvalidMonth(`Month cannot exceed ${MONTH_SIZE.size - 1}`)
    }
    if (month < 0) {
      throw new InvalidMonth('Month cannot be negative')
    }
    this._year = year
    this._month = month
    this._day = day
    this.value = (
      (year - ZEROYEAR) * DAYS_IN_YEAR +
      [...MONTH_SIZE.values()].slice(0, month).reduce((a, b) => a + b, 0) +
      day
    )
  }

  get year() {
    return this._year
  }

  get month() {
    return this._month
  }

  get day() {
    return this._day
  }

  * monthDays() {
    const dayInt = this.value % DAY_TO_INT.size
    let days = this.value % DAYS_IN_YEAR
    let i = 0
    while(MONTH_SIZE.get(i) <= days) {
      days -= MONTH_SIZE.get(i)
      i += 1
    }
    let monday = days - dayInt
    while(monday > 0) {
      monday -= DAY_TO_INT.size
    }
    for(let m = monday; m < MONTH_SIZE.get(i); m += DAY_TO_INT.size) {
      yield Array.from(
        {length: DAY_TO_INT.size},
        (__, index) => m + index)
        .map(day =>
          day < 0
            ? MONTH_SIZE.get((MONTH_SIZE.size + i - 1) % MONTH_SIZE.size) + day
            : day >= MONTH_SIZE.get(i) 
              ? day - MONTH_SIZE.get(i)
              : day)
    }
  }

  toString() {
    let [yearInt, dayInt] = divmod(this.value, DAYS_IN_YEAR)
    const year = ZEROYEAR + yearInt
    let day, month = 0
    for (const [m, size] of MONTH_SIZE.entries()) {
      if (size > dayInt) {
        [day, month] = [dayInt, m]
        break
      }
      dayInt -= size
    }
    return `${day + 1}-${month + 1}-${year}`
  }
}
