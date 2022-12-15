import React, { useState } from 'react'
import ReactDOM from 'react-dom'

function DataList (props) {
  const listItems = data.map(d => (
    <ul>
      <span>
        <li>{d.name}</li>
      </span>
      <span>
        <li>{d.age}</li>
      </span>
    </ul>
  ))
  return <h2>{listItems}</h2>
}

const data = [
  { name: 'Daniel', age: 25 },
  { name: 'John', age: 24 },
  { name: 'Jen', age: 31 }
]

ReactDOM.render(<DataList data={data} />, document.getElementById('root'))
