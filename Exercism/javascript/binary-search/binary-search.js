'use strict'

const isSorted = (array) =>
  array.every(
    (e, i) => i === 0 || e >= array[i - 1]
  )

export class BinarySearch {
  constructor (array) {
    if (Array.isArray(array) && isSorted(array)) {
      this.array = array
    }
  }

  indexOf(el, array = this.array) {
    const mid = Math.trunc(array.length / 2)
    if (array.length === 0) {
      return -1
    }
    if (el === array[mid]) {
      return mid
    }
    if (el < array[mid]) {
      return this.indexOf(el, array.slice(0, mid))
    }
    const index = this.indexOf(el, array.slice(mid + 1))
    return index === -1
      ? index
      : mid + 1 + index
  }
}
