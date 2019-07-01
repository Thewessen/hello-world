'use strict'

const POINT = '+'

const vertical = (char) => char === '|' || char === POINT
const horizontal = (char) => char === '-' || char === POINT

const isConnected = function([x1, y1], [x2, y2], data) {
  if (x1 === x2 && y2 < data.length) {
    return data
      .slice(y1, y2 + 1)
      .map((row) => row[x1])
      .every(vertical)
  }
  if (y1 === y2 && x2 < data[y1].length) {
    return data[y1]
      .split('')
      .slice(x1, x2 + 1)
      .every(horizontal)
  }
  return false
}

const connections = function * ([x, y], [dx, dy], data) {
  let [a, b] = [x, y]
  do {
    [a, b] = [a + dx, b + dy]
    if (data[b] && data[b][a] === POINT) {
      yield [a, b]
    }
  } while (isConnected([x, y], [a, b], data))
}

const pointsIn = function * (data) {
  for (const y in data) {
    for (const x in data[y]) {
      if (data[y][x] === POINT) {
        yield [x, y].map(Number)
      }
    }
  }
}

const countSquares = function * (data) {
  for (const point of pointsIn(data)) {
    let count = 0
    for (const [x1, y1] of connections(point, [1, 0], data)) {
      for (const [x2, y2] of connections(point, [0, 1], data)) {
        if (
          data[y2][x1] === POINT &&
          isConnected([x1, y1], [x1, y2], data) &&
          isConnected([x2, y2], [x1, y2], data)
        ) {
          count += 1
        }
      }
    }
    yield count
  }
}

export class Rectangles {
  static count (data) {
    return [...countSquares(data)].reduce((a, b) => a + b, 0)
  }
}
