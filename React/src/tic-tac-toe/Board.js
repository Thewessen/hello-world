import React from 'react'
import Row from './Row'

export default ({ squares, onClick }) => 
  squares.reduce((rows, __, i, squares) => {
    return i % 3
      ? rows
      : [...rows,
          <Row
            key={i}
            row={squares.slice(i, i + 3)}
            onClick={(j) => onClick(Math.trunc(i / 3), j)}
          />
        ]
  }, [])
