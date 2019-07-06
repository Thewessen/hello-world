'use strict'

export class CustomSet {
  constructor (arr = []) {
    this.set = arr.filter((e, i) => arr.indexOf(e) === i)
  }

  get size() {
    return this.set.length
  }

  empty () {
    return this.set.length === 0
  }

  contains (e) {
    return this.set.includes(e)
  }

  add (...els) {
    return this.union(new CustomSet(els))
  }

  subset (s) {
    return this.set.every((e) => s.contains(e))
  }

  disjoint (s) {
    return this.intersection(s).size === 0
  }

  eql (s) {
    return s.subset(this) && this.subset(s)
  }

  union (s) {
    return new CustomSet(
      s.set.concat(this.set)
    )
  }

  intersection (s) {
    return new CustomSet(
      this.set.filter((e) => s.contains(e))
    )
  }

  difference (s) {
    return new CustomSet(
      this.set.filter((e) => !s.contains(e))
    )
  }
}
