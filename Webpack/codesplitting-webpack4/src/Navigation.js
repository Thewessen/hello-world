import React from 'react'
import { Link, useLocation, useHistory } from 'react-router-dom'

const Navigation = ({ pages }) => {
  const { pathname } = useLocation();
  const history = useHistory();
  const currentIndex = pages.indexOf(pathname)
  const next = () => {
    history.push(pages[(currentIndex + 1) % pages.length])
  }
  const previous = () => {
    history.push(pages[(currentIndex + pages.length - 1) % pages.length])
  }
  return (
    <nav>
      <button onClick={previous}>
        vorige
      </button>
      <button onClick={next}>
        volgende
      </button>
    </nav>
  )
}

export default Navigation
