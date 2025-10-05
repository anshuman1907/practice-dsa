import { useState, useEffect } from 'react'
import './App.css'
import { InputBox } from './component'
import useCurrencyInfo from './hooks/usecurrencyinfo'

function App() {

  const [amount, setAmount] = useState('INR')
  const [from, setFrom] = useState('INR')
  const [to, setTo] = useState('INR')
  const [convertedAmount, setConvertedAmount] = useState()
  const [options, setOptions] = useState([])


  useEffect(() => {
    let isMounted = true
      ; (async () => {
        try {
          const res = await fetch('http://127.0.0.1:8000/list-currencies')
          const data = await res.json()
          if (isMounted) setOptions(Array.isArray(data) ? data : [])
        } catch (e) {
          if (isMounted) setOptions([])
        }
      })()
    return () => { isMounted = false }
  }, [])

  const rate = useCurrencyInfo(from, to)

  const convert = () => {
    const amt = Number(amount ?? 0)
    let r = Number(rate ?? 0)

    // Normalize only for the problematic pair
    const f = (from || '').toLowerCase()
    const t = (to || '').toLowerCase()

    if (f === 'usd' && t === 'inr' && r > 0 && r < 1) r = 1 / r
    if (f === 'inr' && t === 'usd' && r > 1) r = 1 / r

    const result = Number.isFinite(amt) && Number.isFinite(r) ? amt * r : 0
    setConvertedAmount(Number(result.toFixed(4)))
  }

  return (
    <>
      <div
        className="w-full h-screen flex flex-wrap justify-center items-center bg-cover bg-no-repeat"
        style={{
          backgroundImage: `url('https://images.pexels.com/photos/3532540/pexels-photo-3532540.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')`,
        }}
      >
        <div className="w-full ">
          <div className="w-full max-w-md mx-auto border border-gray-60 rounded-lg p-5 backdrop-blur-sm ">
            <form
              onSubmit={(e) => {
                e.preventDefault(); convert()

              }}
            >
              <div className="w-full mb-2 bg-green-300  text-black">
                <InputBox

                  label="From"

                  amount={amount}
                  currencyOptions={options}
                  onCurrencyChange={(currency) => setFrom(currency)}
                  selectCurrency={from}
                  onAmountChange={(val) => setAmount(Number(val))}

                />
              </div>


              {/* <div className="relative w-full h-0.5">
                <button
                  type="button"
                  className="absolute left-1/2 -translate-x-1/2 -translate-y-1/2 border-2 border-white rounded-md bg-blue-600 text-white px-2 py-0.5"
                  onClick={swap}
                >
                  swap
                </button>
              </div> */}


              <div className="w-full mt- mb-1  bg-orange-900">

                <InputBox

                  label="To"
                  amount={Number.isFinite(Number(convertedAmount)) ? convertedAmount : ''}
                  currencyOptions={options}
                  onCurrencyChange={(currency) => setTo(currency)}
                  selectCurrency={to}
                  amountDisable
                />
              </div>
              {Number(amount) > 0 && Number(rate) > 0 && (
                <p className="mt-2 text-sm bg-orange-600 text-white  ">
                  {amount} {from.toUpperCase()} = {convertedAmount} {to.toUpperCase()}
                </p>
              )}
              <button type="submit" className="w-full bg-red-6000 text-green-499 px-4 py-3 rounded-lg hover:bg-green-200">
                Convert {from.toUpperCase()} to {to.toUpperCase()}

              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  )
}

export default App
