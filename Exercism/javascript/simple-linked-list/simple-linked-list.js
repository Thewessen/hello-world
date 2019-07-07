'use strict'

export class List {
  constructor (array = []) {
    this.length = 0
    this.head = null
    this.add(...array.map((e) => new Element(e)))
  }

  add (...elems) {
    for (const elem of elems) {
      this.length += 1
      elem.next = this.head
      this.head = elem
    }
  }
  
  toArray (elem = this.head) {
    if (elem === null) {
      return []
    }
    return [elem.value, ...this.toArray(elem.next)]
  }

  reverse (elem = this.head, prev = null) {
    if (elem === null) {
      this.head = prev
    } else {
      this.reverse(elem.next, elem)
      elem.next = prev
    }
    return this
  }
}

export class Element {
  constructor (value, next = null) {
    this.value = value
    this.next = next
  }
}
