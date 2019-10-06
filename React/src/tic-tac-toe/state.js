import calculateWinner from './calculate-winner'

const initialState = {
  history: [{
    squares: Array.from(
      {length: 9}, () => ({ value: null, winning: false })
    ),
    turnX: true,
    winner: null,
    move: 'start of game',
  }],
  turn: 0,
}

const reducer = (state, action) => {
  switch (action.type) {
    case 'MOVE': {
      const { i, j } = action
      const index = i * 3 + j
      const current = state.history[state.turn]
      const squares = [...current.squares]
      if (state.winner || squares[index].value) {
        return state
      }
      squares[index] = {
        ...squares[index],
        value: current.turnX ? 'X' : 'O'
      }
      return {
        history: [...state.history.slice(0, state.turn + 1), {
          squares,
          turnX: !current.turnX,
          winner: calculateWinner(squares),
          move: `${squares[index].value} at (${j+1},${3-i})`,
        }],
        turn: state.turn + 1
      }
    }
    case 'JUMP': {
      return {
        ...state,
        turn: action.i
      }
    }
    default: {
      return state
    }
  }
}

export {
  initialState,
  reducer
}
