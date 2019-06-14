'use strict'

const string = (obj) => JSON.stringify(obj)

const methodCallToString = (that, method, ...args) =>
  `${string(that)}.${method.name}(${args}): ${method.call(that, ...args)}`

const boxFunctionOutput = (description, output) =>
  `${'-'.repeat(15)}
  ${description}
  ${output}
  ${'-'.repeat(15)}`

module.exports = {
  string: string,
  methodCallToString: methodCallToString,
  boxFunctionOutput: boxFunctionOutput
}
