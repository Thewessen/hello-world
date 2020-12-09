/* eslint-disable */
const utils = require('eslint-utils')

const prohibit = ['entries']

module.exports = {
  rules: {
    'no-template-literals': {
      create: function (context) {
        return {
          NewExpression (node) {
            if (node.callee.name === 'Map') {
              if (node.parent.type === 'Property') {
                // console.log(node.parent.parent)
                const variable = utils.findVariable(context.getScope(), node.parent.parent.parent.id)
                // console.log(variable.references[1].identifier.parent.parent)
                const method = variable.references[1].identifier.parent.parent
                if (prohibit.some(m => m === utils.getPropertyName(method))) {
                  context.report(method.property, 'Do not use entries() method on Map')
                }
              }
            }
          }
          // MemberExpression (node) {
          //   if (prohibit.some(method => method === utils.getPropertyName(node))) {
          //     const variable = utils.findVariable(context.getScope(), node.object)
          //     if (variable) {
          //       const def = variable.defs[0].node.init
          //       console.log(def)
          //       if (def.type === 'NewExpression' && def.callee.name === 'Map') {
          //         context.report(node, 'Do not use entries() method on Map')
          //       }
          //     }
          //   }
          // }
        }
      }
    }
  }
}
