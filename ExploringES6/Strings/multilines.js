'use strict'

const print = require('../helpers/print')

// ES6 template literals can span multiple lines:
const htmlTemplate = `
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Template</title>
  </head>
  <body>
  </body>
</html>`
print(htmlTemplate)
