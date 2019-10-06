export default (squares) => {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ]
  for (const line of lines) {
    const sqrs = line.map((i) => squares[i])
    if (/XXX|OOO/.test(sqrs.map((sqr) => sqr.value).join(''))) {
      line.forEach((i) => { squares[i] = { ...squares[i], winning: true } })
      return squares[line[0]].value
    }
  }
  return null
}
