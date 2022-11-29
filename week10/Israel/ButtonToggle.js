import React, { useState } from 'react'
import ReactDOM from 'react-dom'

function Toggle () {
  const [toggle, setToggle] = useState(true)

  function handleClick () {
    // document.getElementById('button').innerText='OFF'
    setToggle(!toggle)
  }

  return (
    <button id='button' onClick={handleClick}>
      {toggle ? 'ON' : 'OFF'}
    </button>
  )
}

ReactDOM.render(<Toggle />, document.getElementById('root'))
