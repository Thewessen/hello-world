'use strict'

// Resistors have color coded bands, where each color maps to a number. The
// first 2 bands of a resistor have a simple encoding scheme: each color maps
// to a single number.

// These colors are encoded as follows:

// Black: 0
// Brown: 1
// Red: 2
// Orange: 3
// Yellow: 4
// Green: 5
// Blue: 6
// Violet: 7
// Grey: 8
// White: 9

// Mnemonics map the colors to the numbers, that, when stored as an array,
// happen to map to their index in the array: Better Be Right Or Your Great Big
// Values Go Wrong.

// More information on the color encoding of resistors can be found in the
// Electronic color code Wikipedia article

const COLORS = new Map([
  'Black',
  'Brown',
  'Red',
  'Orange',
  'Yellow',
  'Green',
  'Blue',
  'Violet',
  'Grey',
  'White'
].map((e, i) => [e, i]))

module.exports = (color) => COLORS.get(color)
