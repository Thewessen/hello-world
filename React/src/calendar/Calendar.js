import React, { useReducer } from 'react'
import Datetime from './Datetime.js'

const initialState = new Datetime()

const reducer = (state, action) => {
  switch (action.type) {
    case 'SET_DAY': {
      try {
        return new Datetime(action.value, state.month, state.year)
      } catch (e) {
        console.log(e)
        return state
      }
    }
    case 'SET_MONTH': {
      try {
        return new Datetime(state.day, action.value, state.year)
      } catch (e) {
        console.log(e)
        return state
      }
    }
    case 'SET_YEAR': {
      try {
        return new Datetime(state.day, state.month, action.value)
      } catch (e) {
        console.log(e)
        return state
      }
    }
    default: {
      return state
    }
  }
}

const Input = ({ day, setDay, month, setMonth, year, setYear }) => (
  <div className="input-group">
    <input type="number" min="0" value={day} onChange={(e) => setDay(e.target.value)} />
    <input type="number" min="0" value={month} onChange={(e) => setMonth(e.target.value)} />
    <input type="number" min="0" value={year} onChange={(e) => setYear(e.target.value)} />
  </div>
)

const Week = ({ week }) => (
  <div className="calendar-week">
    {week.map(day =>
      <div className="calendar-day" key={day}>{ day }</div>)}
  </div>
)

const Month = ({ month }) => month.map(week =>
    <Week week={week} key={week.join('')} />)

const Calendar = () => {
  const [state, dispatch] = useReducer(reducer, initialState)

  return (
    <div className="calendar-container">
      <Input
        day={state.day}
        setDay={(value) => dispatch({ type: 'SET_DAY', value })}
        month={state.month}
        setMonth={(value) => dispatch({ type: 'SET_MONTH', value })}
        year={state.year}
        setYear={(value) => dispatch({ type: 'SET_YEAR', value })}
        />
      <Month className="calendar-month" month={[...state.monthDays()]} />
    </div>
  )
}

export default Calendar
