import { file1 } from '../../node_packages'

const compile = () => {
  document.getElementById('app').innerHTML = file1()
  const text = file1()
  return `This module got imported: ${text}`
}

console.log(compile())
