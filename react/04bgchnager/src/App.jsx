import { useState } from "react"


function App() {
  const [color, setColor] = useState("")



  return (

    <div className="w-full h-screen duration-200"
      style={{ backgroundColor: color }}>
      <div className="  justifiy-center      insert-x-0 px-2">
        
        <div className="flex flex-wrap justify-center gap-3 shadow-lg bg-amber-50 px-3 py-2 rounded-3xl">
         
         <button onClick={()=> setColor("red")} className=" outline-none px-4 py-1  rounded-full text-white shadow-lg "
            style={{ backgroundColor: "red" }}>Red</button>

          <button onClick={()=> setColor("green")} className=" outline-none px-4 py-1 rounded-full text-white shadow-lg "
            style={{ backgroundColor: "green" }}>Green</button>

          <button onClick={()=> setColor("Blue")} className=" outline-none px-4 py-1  rounded-full text-white shadow-lg "
            style={{ backgroundColor: "blue" }}>Blue</button>
          
          <button onClick={()=> setColor("orange")} className=" outline-none px-4 py-1  rounded-full text-white shadow-lg "
            style={{ backgroundColor: "orange" }}>Orange</button>

               <button onClick={()=> setColor("Pink")} className=" outline-none px-4 py-1  rounded-full text-white shadow-lg "
            style={{ backgroundColor: "pink" }}>Pink</button>

   <button onClick={()=> setColor("black")} className=" outline-none px-4 py-1  rounded-full text-white shadow-lg "
            style={{ backgroundColor: "black" }}>Black</button>

   <button onClick={()=> setColor("skyblue")} className=" outline-none px-4 py-1  rounded-full text-white shadow-lg "
            style={{ backgroundColor: "skyblue" }}>Sky Blue</button>

   <button onClick={()=> setColor("Gray")} className=" outline-none px-4 py-1  rounded-full text-white shadow-lg "
            style={{ backgroundColor: "Gray" }}>Gray</button>


        </div>

      </div>

    </div>


  )
}

export default App
