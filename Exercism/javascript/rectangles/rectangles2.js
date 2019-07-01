'use strict'

// Move:
// right [0, 1]
// bottom [1, 0]
// left [0, -1]
// top [-1, 0]

const move = ([x, y], [dx, dy], data) => {
  let [a, b] = [x + dx, y + dy]
  let line = dy === 0 ? '|' : '-'
  while (data[a] && data[a][b] && data[a][b] === line) {
    [a, b] = [a + dx, b + dy]
  }
  if (data[a] && data[a][b] && data[a][b] === '+') {
    return [a, b]
  }
  return [x, y]
}


const samePoint = (p1, p2) => p1[0] === p2[0] && p1[1] === p2[1]

const countSquares = (start, curr, count, data) => {
  let point = move(curr, [0, 1], data)
  // console.log(start, curr, point, lastMove)
  if (!samePoint(point, curr)) {
    count += countSquares(start, point, count, data)
    count += countSquares(point, point, count, data)
    curr = point
  } else {
    return 0
  }
  point = move(curr, [1, 0], data)
  if (!samePoint(point, curr)) {
    count += countSquares(start, point, count, data)
    count += countSquares(point, point, count, data)
    curr = point
  } else {
    return 0
  }
  point = move(curr, [0, -1], data)
  if (!samePoint(point, curr)) {
    count += countSquares(start, point, count, data)
    count += countSquares(point, point, count, data)
    curr = point
  } else {
    return 0
  }
  point = move(curr, [-1, 0], data)
  if (!samePoint(curr, start) && !samePoint(point, curr)) {
    count += countSquares(start, point, count, data)
    count += countSquares(point, point, count, data)
    curr = point
  } else {
    return 0
  }
  if (samePoint(curr, start)) {
    return 1
  }
  return 0
}

const data = [
  '+-+',
  '| |',
  '+-+'
]

module.exports = countSquares([0,0],[0,0],[0,0],0,data)
// module.exports = samePoint([0,-1],[0,1])
// module.exports = move

// export class Rectangles {
class Rectangles {
  static count (data) {
    return countSquares([0, 0], [0, 0], [0, 0], 0, data)
  }
}
