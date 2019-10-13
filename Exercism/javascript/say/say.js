'use strict'

const UNITY = new Map([
  'zero',
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine'
].map((e, i) => [i, e]))

const SPECIAL = new Map([
  [10, 'ten'],
  [11, 'eleven'],
  [12, 'twelve'],
  [13, 'thirteen'],
  [14, 'fourteen'],
  [15, 'fifteen'],
  [16, 'sixteen'],
  [17, 'seventeen'],
  [18, 'eighteen'],
  [19, 'nineteen'],
  [20, 'twenty'],
  [30, 'thirty'],
  [50, 'fifty'],
  [80, 'eighty']
])

const GROUPS = new Map([
  'ty',
  'hundred',
  'thousand',
  'million',
  'billion'
].map((e, i) => [i, e]))

export class Say {
  inEnglish(number) {
    if (number < 0 || 1e12 <= number) {
      throw new Error('Number must be between 0 and 999,999,999,999.');
    }
  }
}
