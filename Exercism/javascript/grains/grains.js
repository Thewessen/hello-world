'use strict'

import BigInt from './lib/big-integer';

export class Grains {
  square (value) {
    return BigInt(2)
      .pow(value - 1)
      .toString()
  }

  total() {
    return BigInt(2)
      .pow(64)
      .minus(1)
      .toString()
  }
}
