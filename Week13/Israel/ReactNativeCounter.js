import React, { useState } from 'react'
import { Text, View } from 'react-native'

const SimpleCounter = () => {
  const [count, setCount] = useState(0)
  const incrementHandler = () => {
    setCount(count + 1)
  }
  return (
    <View>
      <Text>
        button count: <span id='actualCount'>{count}</span>
      </Text>
      <button id='mainButton' onClick={incrementHandler}>
        Increment
      </button>
    </View>
  )
}

export default SimpleCounter
