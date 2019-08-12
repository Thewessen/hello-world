'use strict'

export class Series {
  constructor (string) {
    this.serie = [...string].map(Number)
  }

  get digits () {
    return this.serie
  }

  slices (n) {
    if (n > this.serie.length) {
      throw new Error('Slice size is too big.')
    }
    return this.serie
      .reduce((slcs, __, i, serie) =>
          n + i <= serie.length
            ? [...slcs, serie.slice(i, n + i)]
            : slcs
        , [])
  }
}
