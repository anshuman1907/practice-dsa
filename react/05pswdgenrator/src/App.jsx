import { useCallback, useState, useEffect, useRef } from 'react'
import './App.css'

function App() {
  const [length, setLength] = useState(8)
  const [numberallow, setnumberallow] = useState(false);
  const [charallow, setcharallow] = useState(false);
  const [Password, setPassword] = useState("")

  // userefhook

  const pswdref = useRef(null)

  const passwordgenrator = useCallback(() => {

    let pass = ""
    let str = "abcdefghijklmnopqrstuvwxyz"
    if (numberallow) str += "0123456789"
    if (charallow) str += "!@#$%^&*()-+=[]{}~"
    for (let i = 1; i <= length; i++) {
      let char = Math.floor(Math.random() * str.length + 1)


      pass += str.charAt(char)
    }
    setPassword(pass)

  }, [length, numberallow, charallow, setPassword])

  const copypswdtoclipboard = useCallback(() => {
    pswdref.current?.select()
    pswdref.current?.setSelectionRange(0, 9)
    window.navigator.clipboard.writeText(Password)


  }, [Password])

  useEffect(() => { passwordgenrator() }, [length, numberallow, passwordgenrator])
  return (
    <>
      <div className='w-full max-w-md mx-auto shadow-md rounded-lg px-4 my-8  bg-green-700'>
        <h1 className='text-white text-center'>Password Genrator</h1>
      </div>

      <div className='flex shadow rounded-lg overflow-hidden mb-4 bg-white text-black-200'>
        <input type="text"
          value={Password}
          className="outline-none w-full pt-1 px-3"
          placeholder='Password'
          readOnly
          ref={pswdref}
        />
        <button onClick={copypswdtoclipboard} className='bg-red-500 outline-none hover:bg-green-300 text-white px-3  shrink-0'>Copy</button>
      </div>

      <div className='flex text-sm gap-x-2'>

        <div className='flex items-center gap-x-1'>
          <input type="range"
            min={6}
            max={100}
            value={length}
            className='cursor-pointer'
            onChange={(e) => { setLength(e.target.value) }}
          />
          <label className='text-red-600'>length:  {length}</label>
        </div>

        <input type="checkbox"
          defaultChecked={numberallow}
          id='numberinput'
          onChange={(e) => { setnumberallow((prev) => !prev) }}
        />
        <label className='text-red-600' >Number:  {numberallow}</label>

        <input type="checkbox"
          defaultChecked={charallow}
          id='charinput'
          onChange={(e) => { setcharallow((prev) => !prev) }}
        />
        <label className='text-red-600' >Charecter:  {charallow}</label>

      </div>
    </>
  )
}

export default App
