import React from 'react'
import Page1 from './Page1'
import Page2 from './Page2'
import { Route, Switch } from 'react-router-dom'

const App = ({ routes }) => (
  <Router>
    <nav>
      <ul>
        <li>
          <Link to='/page3'>Page1</Link>
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
const Router = () => (
  <Switch>
    <Router page="/page1">
      <Page1 />
    </Router>
    <Router page="/page2">
      <Page2 />
    </Router>
  </Switch>
)

export default Routes
