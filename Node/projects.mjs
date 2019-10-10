#!/usr/local/bin/node --experimental-modules

// Run a child process async
import { spawn } from 'child_process'
// Promises instead of callbacks
import fs from 'fs-extra'
import commander from 'commander'
import path from 'path'
import Table from 'cli-table'
import colors from 'colors'

// Options (shell & editor)
// =================================
const OPTIONS = (dir) => ({
  cmd: process.env.EDITOR +
    (fs.existsSync(path.join(dir, 'Session.vim'))
      ? ' -S'
      : ' . -c Obsession'),
  cmdOptions: {
    stdio: 'inherit',
    cwd: dir,
    shell: '/usr/bin/zsh'
  }
})
// File to read containing list of projects
OPTIONS.projects = path.join(process.env.HOME, '.project-stack')

// Table output settings
const table = new Table({
  head: ['#'.padStart(3), 'project'],
  colWidths: [5, 50],
  chars: {
    'top': '', 'top-mid': '', 'top-left': '', 'top-right': '',
    'bottom': '', 'bottom-mid': '', 'bottom-left': '',
    'bottom-right': '', 'left': '', 'left-mid': '', 'mid': '',
    'mid-mid': '', 'right': '', 'right-mid': '', 'middle': '|'
  },
  style: { head: ['yellow'] }
})

// Commandline options
const program = new commander.Command()
  .version('v8', '-v, --version', 'Output current version')
  .description((
    "Cmd utility that lets you pick a directory (project) " +
    "and run your prefered editor inside the given directory. " +
    "Start editing immediatly!"
  ))
  .option('-l, --list', 'List all projects')
  .option( '--dir <dir>', 'Use the given dir for picking a project')
  .option( '-d, --debug', 'Show the arguments given and exit')
  .arguments('[project]')
  .action(project => {
    OPTIONS.project = project
  })

// Helpers
// =================================
const stdin = process.stdin.setEncoding('utf8')
const stdout = process.stdout.setEncoding('utf8')

const norm = (string) =>
  string.toLowerCase().replace(' ', '')

const isPart = (substring) => (string) =>
  norm(string).includes(norm(substring))

const replaceENV = dir =>
  dir.replace(/\$([A-Z]+)/, (__, p1) => process.env[p1])

const error = (e) => console.error(e)

const listFiles = (files) => {
  const projects = files.map((project, index) =>
    [(index + 1).toString().padStart(3).green,
      path.basename(project)])
  table.push(...projects)
  console.log(table.toString())
}

const filterProject = (files, input) => {
  const projects = files.filter(isPart(input))
  if (projects.length === 1) {
    return projects.pop()
  } else {
    throw new Error('Project not found!')
  }
}

const pickProject = (files, data) => {
  const input = data.toString().trim()
  try {
    return /^\d+$/.test(input) && parseInt(input) <= files.length
      ? files[parseInt(input) - 1]
      : filterProject(files, input)
  } catch (e) { error(e) }
}

const chooseProject = async (files) =>
  new Promise((resolve, reject) => {
    listFiles(files)
    stdout.write('Choose a project: ')
    stdin.on('data', data => {
      const project = pickProject(files, data)
      if (project && typeof project === 'string') {
        resolve(project)
      } else {
        reject('Project not found!')
      }
    })
  })

// Main
// =================================
program.parse(process.argv)

if (program.dir) {
  OPTIONS.dir = program.dir
}

const projects = fs
  .readFile(OPTIONS.projects)
  .then(buffer => buffer
    .toString()
    .split('\n')
    .map(replaceENV)
    .filter(dir => fs.existsSync(dir))
    .filter(dir => fs.lstatSync(dir).isDirectory())
    .sort((a, b) => path.basename(a).localeCompare(path.basename(b))))
  .then(dirs => {
    if (typeof OPTIONS.project !== 'undefined') {
      return dirs.filter(isPart(OPTIONS.project))
    }
    return dirs
  })
  .catch(error)

if (program.list) {
  projects
    .then(listFiles)
    .catch(error)
    .finally(() => process.exit(0))
}

if (program.debug) {
  console.log(program.opts())
}

projects
  .then(files =>
    files.length === 1
      ? files[0]
      : chooseProject(files))
  .then(project => {
    const { cmd, cmdOptions } = OPTIONS(project)
    stdin.destroy()
    return spawn(cmd, cmdOptions)
  })
  .catch(e => {
    error(e)
    process.exit(1)
  })
