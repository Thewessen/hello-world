'use strict'

class LinkNode {
  constructor (value, before = null, after = null) {
    this.value = value
    this.before = before
    this.after = after
  }
}

export class LinkedList {
  constructor (data = []) {
    if (!data[Symbol.iterator]) {
      return new Error('Data is not iterable')
    }
    this.data = Array.from(data)
      .map((e) => new LinkNode( e, null, null))
      .map((e, i, arr) => {
        e.before = i > 0 ? arr[i - 1] : null
        e.after = i < arr.length - 1 ? arr[i + 1] : null
        return e
      })
  }

  last () {
    return this.data[this.data.length - 1] || null
  }

  first () {
    return this.data[0] || null
  }

  push (value) {
    const node = new LinkNode(
      value, this.last(), null
    )
    if (this.data.length > 0) {
      this.last().after = node
    }
    this.data.push(node)
    return this.data.length
  }

  pop () {
    const node = this.data.pop()
    if (this.data.length > 0) {
      this.last().after = null
    }
    return node.value
  }

  shift () {
    const node = this.data.shift()
    if (this.data.length > 0) {
      this.first().before = null
    }
    return node.value
  }

  unshift (value) {
    const node =  new LinkNode(
      value, null, this.first()
    )
    if (this.data.length > 0) {
      this.first().before = node
    }
    this.data.unshift(node)
    return this.data.length
  }

  delete (value) {
    const index = this.data.map(
        (node) => node.value
      ).indexOf(value)
    if (index >= 0) {
      const node = this.data.splice(index, 1)[0]
      if (node.before !== null) {
        this.data[index - 1].after = node.after
      }
      if (node.after !== null) {
        this.data[index].before = node.before
      }
      return this.data.length
    }
  }

  count() {
    return this.data.length
  }
}
