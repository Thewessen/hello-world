'use strict'

const POINTS = new Map()
  .set(10, 1)
  .set(5, 5)
  .set(1, 10)

export const solve = (x, y) => {
  const dist = Math.hypot(x, y)
  let score = 0
  for (const [dst, scr] of POINTS.entries()) {
    if (dist <= dst) {
      score = scr
    }
  }
  return score
}
