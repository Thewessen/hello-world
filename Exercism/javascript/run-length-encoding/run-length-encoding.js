'use strict'

export const encode = (string) => string.replace(/(.)\1+/g,
    (match, char) => match.length + char)

export const decode = (string) => string.replace(/(\d+)(.)/g,
    (__, n, char) => char.repeat(n))
