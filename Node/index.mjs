#!/usr/local/bin/node --experimental-modules

// Run a child process async
import { spawn } from 'child_process'
// Promises instead of callbacks
import fs from 'fs-extra'

const dir = '/home/sthewessen/Websites'

const stdin = process.stdin
const stdout = process.stdout

const norm = (string) =>
  string
    .toLowerCase()
    .replace(' ', '')

const isPart = (substring) => (string) =>
  norm(string).includes(norm(substring))

const chooseProject = async (files) =>
  new Promise((resolve, reject) => {
    for (const [index, file] of files.entries()) {
      console.log(`${index + 1}: ${file}`)
    }
    stdin.resume()
    stdout.write('Choose a project: ')
    stdin.once('data', data => {
      const input = data.toString().trim()
      if (/^\d+$/.test(input)) {
        const index = parseInt(input) - 1
        if (index >= files.length) {
          console.log('This project does not exist')
          reject()
        } else {
          resolve(files[index])
        }
      } else {
        if (files.some(isPart(input))) {
          resolve(files.find(isPart(input)))
        } else {
          console.log('Project not found!')
          reject()
        }
      }
    })
  })

fs.readdir(dir)
  .then(chooseProject)
  .catch(e => console.log(e))
  .then(project => {
    stdin.destroy()
    spawn('nvim -S', {
      stdio: 'inherit',
      cwd: `${dir}/${project}`,
      shell: true
    })
  })
