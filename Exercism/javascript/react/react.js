// Making sure custom props won't overwrite these properties
const hooks = Symbol('Current hooks on object')
const oldValue = Symbol('Old prop value')
const cleanup = Symbol('Stable state, initiate callbacks')
const callbacks = Symbol('callbacks')

class Watcher {
  constructor() {
    this[hooks] = []
    this[callbacks] = new Set()
    return new Proxy(this, {
      set(obj, prop, value) {
        if(typeof obj[oldValue] === 'undefined') {
          obj[oldValue] = obj[prop]
        }
        obj[prop] = value
        Watcher.changed.add(obj)
        obj[hooks].forEach(f => f(obj))
        return true
      }
    })
  }

  setValue(input) {
    this.value = input
    this[cleanup]()
  }

  hook(fn) {
    this[hooks].push(fn)
  }

  addCallback(cell) {
    this[callbacks].add(cell.callback)
  }

  removeCallback(cell) {
    this[callbacks].delete(cell.callback)
  }

  [cleanup]() {
    for (const cell of Watcher.changed) {
      if (cell.value !== cell[oldValue]) {
        cell[callbacks].forEach(f => f(cell))
      }
      delete cell[oldValue]
    }
    Watcher.changed.clear()
  }
}

Watcher.changed = new Set()

class InputCell extends Watcher {
  constructor(input) {
    super()
    this.value = input
  }
}

class ComputeCell extends Watcher {
  constructor(cells, fn) {
    super()
    cells.forEach(cell => {
      cell.hook((
        () => this.value = fn(cells)
      ).bind(this))
    })
    this.value = fn(cells)
  }
}

class CallbackCell {
  constructor(fn) {
    this.values = []
    this.callback = new Proxy(fn, {
      apply(fn, that, args) {
        const value = fn(...args)
        that.values.push(value)
        return value
      }
    }).bind(this)
  }
}

export {
  InputCell,
  ComputeCell,
  CallbackCell
}
