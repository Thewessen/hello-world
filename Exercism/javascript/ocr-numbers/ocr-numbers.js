'use strict'

const NUMBERS = new Map([
[[' _ ',
  '| |',
  '|_|',
  '   '].join('\n'), 0],
[['   ',
  '  |',
  '  |',
  '   '].join('\n'), 1],
[[' _ ',
  ' _|',
  '|_ ',
  '   '].join('\n'), 2],
[[' _ ',
  ' _|',
  ' _|',
  '   '].join('\n'), 3],
[['   ',
  '|_|',
  '  |',
  '   '].join('\n'), 4],
[[' _ ',
  '|_ ',
  ' _|',
  '   '].join('\n'), 5],
[[' _ ',
  '|_ ',
  '|_|',
  '   '].join('\n'), 6],
[[' _ ',
  '  |',
  '  |',
  '   '].join('\n'), 7],
[[' _ ',
  '|_|',
  '|_|',
  '   '].join('\n'), 8],
[[' _ ',
  '|_|',
  ' _|',
  '   '].join('\n'), 9]
])

const splitLines = function* (data) {
  const lines = data.split('\n')
  for (let i = 0; i < lines.length; i += 4) {
    yield lines.slice(i, i + 4)
  }
}

const splitNumbers = function* (lines) {
  for (let i = 0; i < lines[0].length; i += 3) {
    yield lines.map((line) => line.substr(i, 3)).join('\n')
  }
}

const convertNumber = function* (numbers) {
  for (const number of numbers) {
    yield NUMBERS.has(number)
      ? NUMBERS.get(number)
      : '?'
  }
}

export const convert = (numbers) => {
  const lines = []
  for (const line of splitLines(numbers)) {
    lines.push([...convertNumber(splitNumbers(line))].join(''))
  }
  return lines.join(',')
}
