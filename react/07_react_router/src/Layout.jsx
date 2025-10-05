import React from "react";
import { Outlet } from "react-router-dom";

import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom'

import Header from "./component/header/header";
import Footer from "./component/Footer/footer";
import Home from "./component/home/home";
// import Contact from "./component/Contact/contact";


function Layout() {

    return(

        <>
        
        <Header/>
        <Outlet/>
        

        <Footer/>

        </>
    )
}
export default Layout