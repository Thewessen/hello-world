'use strict'

export class PhoneNumber {
  constructor (number) {
    this.nr = number.trim()
  }

  number () {
    const NANP = /^(?:\+?1[-. ]?)?\(?([2-9][0-9]{2})\)?(?:[-. ]+)?([2-9][0-9]{2})(?:[-. ]+)?([0-9]{4})$/
    if (NANP.test(this.nr)) {
      return NANP.exec(this.nr).splice(1).join('')
    }
    return null
  }
}
