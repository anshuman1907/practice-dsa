import { useState } from 'react'

import './App.css'

function App() {

  let [counter, setCounter] = useState(10)

  // let counter =7
  const addValue = () => {

    if (counter>19){

    alert("Maximum count limit reached")

      return "counter maximum limit is reached "
    }
    // counter= counter+1
    setCounter(counter + 1)

  }
  const removeValue = () => {

    if (counter<1){
    alert("Minimum Count reached")
      return "counter not in negative "
    }
    setCounter(counter - 1)


  }


  return (
    <>
      <h1>Counter Count: {counter}  </h1>
      <button onClick={addValue}>Add Value</button>
      <br />
      <br />

      <button onClick={removeValue} >Remove Value</button>

      <footer>
<p>Counter count maximum is 20 and minimum is 0 </p>
      </footer>

    </>
  )
}

export default App
