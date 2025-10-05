import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Layout from './layout.jsx'

import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Home from './component/home/home.jsx'
import About from './component/About/about.jsx'
import Contact from './component/Contact/contact.jsx'
import Github from './component/Github/github.jsx'
const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        path: "",
        element: <Home />
      },
      {
        path: "about",
        element: <About />
      },
       {
        path: "contact",
        element: <Contact />
      },
      {
        path: "github",
        element: <Github />
      }
    ]

  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
