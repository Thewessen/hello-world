'use strict'

export const isLeap = (year) => (
  !isNaN(year)
  && (
    year%4 === 0
    && (
      year%100 !== 0
      || year%400 === 0
    )
  )
)
