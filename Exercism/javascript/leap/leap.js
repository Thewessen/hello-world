'use strict'

export const isLeap = (year) => (
  Number.isInteger(year) && year > 0
  && (
    year % 4 === 0
    && (
      year % 100 !== 0
      || year % 400 === 0
    )
  )
)
