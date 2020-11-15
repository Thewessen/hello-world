import React, { lazy, Suspense } from 'react'
import { BrowserRouter as Router, Switch, Route, useRouteMatch } from 'react-router-dom'
const Page1 = lazy(() => import('./pages/Page1'))
const Page2 = lazy(() => import('./pages/Page2'))
const Page3 = lazy(() => import('./pages/Page3'))
import Navigation from './Navigation'

const App = () => {
  const pages = ['/page1', '/page2', '/page3']
  return (
    <Router>
      <Suspense fallback={<div>loading...</div>}>
        <Switch>
          <Route path="/page1" component={Page1} />
          <Route path="/page2" component={Page2} />
          <Route path="/page3" component={Page3} />
        </Switch>
      </Suspense>
      <Navigation pages={pages} />
    </Router>
  )
}

export default App
