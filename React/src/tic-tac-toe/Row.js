import React from 'react'
import Square from './Square'

export default ({ row, onClick }) => (
  <div>
    <div className="board-row">
      { row.map((square, i) => (
            <Square
              state={square}
              key={i}
              onClick={() => onClick(i)}
            />
        )) }
    </div>
  </div>
)

