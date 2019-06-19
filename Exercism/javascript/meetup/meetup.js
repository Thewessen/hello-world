'use strict'

const DAYTOINT = new Map([
  ['Sunday', 0],
  ['Monday', 1],
  ['Tuesday', 2],
  ['Wednesday', 3],
  ['Thursday', 4],
  ['Friday', 5],
  ['Saturday', 6]
])

const isFunction = (obj) =>
  Object.prototype.toString.call(obj) === '[object Function]'

const dateFn = (year) => (month) => (day) => new Date(year, month, day)

const meetupFn = (dayStr) => {
  const day = DAYTOINT.get(dayStr)
  return (datefn, startday, convert = undefined) => {
    while (datefn(startday).getDay() !== day) {
      startday += 1
    }
    if (isFunction(convert)) {
      startday = convert(startday)
    }
    return datefn(startday)
  }
}

export const meetupDay = (year, month, dayStr, isth) => {
  const monthFn = dateFn(year)
  const getMeetup = meetupFn(dayStr)

  let meetup
  if (isth === 'last') {
    meetup = getMeetup(monthFn(month + 1), -6)
  }
  if (isth === 'teenth') {
    meetup = getMeetup(monthFn(month), 13)
  }
  let nr = Number.parseInt(isth)
  if (Number.isInteger(nr)) {
    meetup = getMeetup(monthFn(month), 1,
      (d) => d + 7 * (nr - 1))
  }
  if (meetup.getMonth() !== monthFn(month)(1).getMonth()) {
    throw new Error('Invalid meetup day')
  }
  return meetup
}
