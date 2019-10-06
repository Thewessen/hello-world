import React from 'react'
import Board from './Board.js'

export default ({ history, turnNr,  onClick }) => (
  <ol>
    { history.map((state, i) => {
        let desc = i
          ? `#${i}: ${state.move}`
          : `Go to game start`
        return (
          <li key={i}>
            <a href="_blank" onClick={(ev) => { ev.preventDefault(); onClick(i)}}>
                <Board
                  squares={state.squares}
                  onClick={() => {}}
                />
              { i === turnNr ? <b>{desc}</b> : desc}
            </a>
          </li>
        )
      }) }
  </ol>
)
