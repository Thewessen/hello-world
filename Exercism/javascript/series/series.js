'use strict'

const slicer = (n) => (slcs, __, i, serie) =>
  n + i <= serie.length
    ? [...slcs, serie.slice(i, n + i)]
    : slcs

export class Series {
  constructor (string) {
    this.serie = Array.from(string).map(Number)
  }

  get digits () {
    return this.serie
  }

  slices (n) {
    if (n > this.serie.length) {
      throw new Error('Slice size is too big.')
    }
    return this.serie
      .reduce(slicer(n), [])
  }
}
