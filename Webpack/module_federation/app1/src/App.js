import React from 'react'
import Page1 from './Page1'
import Page2 from './Page2'
import { Router } from 'react-router-dom'

const App = ({ routes }) => (
  <Router>
    <nav>
      <ul>
        <li>
          <Link to='/page1'>Page1</Link>
        </li>
        <li>
          <Link to='/page2'>Page2</Link>
        </li>
      </ul>
    </nav>
    {routes}
  </Router>
)

export default App
