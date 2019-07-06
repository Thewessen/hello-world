'use strict'

const includes = (arr1, arr2) =>
  arr2.length === 0 ||
  arr1.some((__, i) =>
    arr2.every((e, j) =>
      e === arr1[i + j]
    )
  )

export class List {
  constructor (list = []) {
    this.list = list
  }

  compare (list) {
    const l1 = this.list
    const l2 = list.list
    if (
      l1.length === l2.length &&
      l1.every((e, i) => e === l2[i])
    ) {
      return 'EQUAL'
    }
    if (includes(l2, l1)) {
      return 'SUBLIST'
    }
    if (includes(l1, l2)) {
      return 'SUPERLIST'
    }
    return 'UNEQUAL'
  }
}
