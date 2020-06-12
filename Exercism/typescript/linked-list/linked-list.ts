interface LinkNode<T> {
  value: T | null,
  previous: LinkNode<T> | null,
  next: LinkNode<T> | null
}

export default class LinkedList<T> {
  constructor (
    private head: LinkNode<T> | null = null,
  ) {}

  last (): LinkNode<T> | null {
    let lastNode = this.head
    while (
      lastNode !== null &&
      lastNode.next !== null
    ) {
      lastNode = lastNode.next
    }
    return lastNode
  }

  push (value: T): void {
    const lastNode = this.last()
    if (lastNode !== null) {
      lastNode.next = {
        value,
        previous: lastNode,
        next: null 
      }
    } else {
      this.head = {
        value,
        previous: null,
        next: null
      }
    }
  }

  pop (): T {
    const lastNode = this.last()
    if (lastNode === null) {
      throw new Error('Empty list!')
    }
    const previous = lastNode.previous
    if (previous !== null) {
      previous.next = null
    } else {
      this.head = null
    }
    return lastNode.value
  }

  shift (): T {
    const firstNode = this.head
    if (firstNode === null) {
      throw new Error('List empty!')
    }

    const next = firstNode.next
    if (next !== null) {
      next.previous = null
    }

    this.head = next
    return firstNode.value
  }

  unshift (value: T): void {
    const newNode = {
      value,
      previous: null,
      next: this.head
    }
    if (this.head !== null) {
      this.head.previous = newNode
    }
    this.head = newNode
  }

  count(): number {
    let count = 0
    let node = this.head
    while (node !== null) {
      count += 1
      node = node.next
    }
    return count
  }

  delete (value: T): boolean {
    let node = this.head
    while (node !== null && node.value !== value) {
      node = node.next
    }
    if (node !== null) {
      const previous = node.previous
      const next = node.next
      if (previous !== null) {
        previous.next = next
      } else {
        this.head = next
      }
      if (next !== null) {
        next.previous = previous
      }
      return true
    }
    return false
  }
}
