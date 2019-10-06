import React from 'react'

export default ({ state: { winning, value }, onClick }) => (
  <button
    className={"square" + (winning ? ' winning' : '')}
    onClick={onClick}
  >
    { value }
  </button>
)

