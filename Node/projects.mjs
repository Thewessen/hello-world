#!/usr/local/bin/node --experimental-modules

// Run a child process async
import { spawn } from 'child_process'
// Promises instead of callbacks
import fs from 'fs-extra'
import program from 'commander'
import path from 'path'
import Table from 'cli-table'
import colors from 'colors'

// Global options (editor and project dir)
const OPTIONS = {
  projects: process.env.HOME + '/.project-stack',
  cmd: process.env.EDITOR,
  project: null,
  cmdOptions: (project) => ({
    stdio: 'inherit',
    cwd: project,
    shell: '/usr/bin/zsh'
  })
}

// CMD-line options
// =================================
program
  .version('v8', '-v, --version', 'Output current version')
  .description(`
    Cmd utility that lets you pick a directory (project) and run your prefered
    editor inside the given directory. Start editing immediatly!`
    .replace(/ {2,}/g, ' ')
    .replace('\n', '')
  )
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
const stdout = process.stdout

const norm = (string) =>
  string
    .toLowerCase()
    .replace(' ', '')

const isPart = (substring) => (string) =>
  norm(string).includes(norm(substring))

const replaceENV = dir => dir.replace(/\$([A-Z]+)/, (__, p1) => process.env[p1])
const error = (e) => console.error(e)

const listFiles = (files) => {
  const projects = [...files.map(file => path.basename(file)).entries()]
    .map(row => {
      row[0] = row[0].toString().padStart(3).green
      return row
    })
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
  table.push(...projects)
  console.log(table.toString())
}

const filterProject = async (files, input) => 
  new Promise((resolve, reject) => {
    const projects = files.filter(isPart(input))
    switch (projects.length) {
      case 1: {
        resolve(projects.pop())
        break
      }
      case 0: {
        reject('No specific project found.')
        break
      }
      default: {
        reject('Project not found!')
      }
    }
  })

const chooseProject = async (files) =>
  new Promise((resolve, reject) => {
    listFiles(files)
    stdout.write('Choose a project: ')
    stdin.on('data', data => {
      const input = data.toString().trim()
      if (/^\d+$/.test(input)) {
        const index = parseInt(input) - 1
        if (index >= files.length) {
          reject('This project does not exist')
        } else {
          resolve(files[index])
        }
      } else {
        filterProject(files, input)
        .then(resolve)
        .catch(reject)
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
    const { cmd, cmdOptions } = OPTIONS
    stdin.destroy()
    if (fs.existsSync(path.join(project, 'Session.vim'))) {
      return spawn(cmd + ' -S', cmdOptions(project))
    }
    return spawn(cmd + ' -c Obsession', cmdOptions(project))
  })
  .catch(e => {
    error(e)
    process.exit(1)
  })
