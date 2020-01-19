#!/usr/bin/env node --no-warnings

const fs = require('fs')

const parseArgs = (args) => {
  const noPattern = args
    .findIndex(x => !/^-\w$/.test(x))

  const flags = args.slice(0, noPattern)
  const p = args[noPattern]
  const pattern = new RegExp(
    flags.includes('-x') ?  `^${p}$` : p,
    flags.includes('-i') ? 'i' : ''
  )

  const files = args.slice(noPattern + 1)

  return {
    pattern,
    flags,
    files,
  }
}

const main = async () => {
  const args = process.argv.slice(2)
  const { pattern, flags, files } = parseArgs(args)

  for (const file of files) {
    const f = fs.readFileSync(file).toString()

    let sameFile = false
    f.split('\n').forEach((line, i) => {
      if (pattern.test(line) ^ flags.includes('-v')) {
        let result = ''
        if (flags.includes('-l')) {
          if (!sameFile) {
            sameFile = true
            result = file
          }
        } else {
          if (files.length > 1) result += `${file}:`
          if (flags.includes('-n')) result += `${i+1}:`
          result += line
        }
        console.log(result)
      }
    })
  }
}

main()
