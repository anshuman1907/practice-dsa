import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card  from './components/card'
function App() {
  const [count, setCount] = useState(0)
  // let myObj= {
  //   name: "anshuman",
  //   age:23
  // }

  // let newarry= [1,3,45,6,76,78,8,3]

  return (
    <>
      <h1 className='bg-green-400 text-black m-4 rounded-1xl
      .'>tailwind test</h1>
     
    <Card username ="Anshu"/>
     
    <Card username ="Anshuman"/>
    <Card username="Anshuman1" btn = "modified"/>



    
    </>
  )
}

export default App
