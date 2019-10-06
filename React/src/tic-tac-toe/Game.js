import React, { useReducer } from 'react'
import { initialState, reducer } from './state'
import Board from './Board'
import History from './History'

export default () => {
  const [state, dispatch] = useReducer(reducer, initialState)

  const current = state.history[state.turn]
  const status = current.winner
    ? `Winner: ${current.winner}`
    : current.turn === 9
      ? `Draw`
      : `Next player: ${current.turnX ? 'X' : 'O'}`

  return (
    <div className="game">
      <div className="game-board">
        <Board
          squares={current.squares}
          onClick={(i, j) => { dispatch({ type: 'MOVE', i, j })}}
        />
      </div>
      <div className="game-info">
        <div>{status}</div>
        <History
          history={state.history}
          turnNr={state.turn}
          onClick={(i) => { dispatch({ type: 'JUMP', i })}}
        />
      </div>
    </div>
  )
}
