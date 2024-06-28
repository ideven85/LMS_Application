//import { useState } from 'react'
import {Routes,Route} from "react-router-dom";
import {Home} from "./pages/Home.jsx";
import CourseGoal from "./pages/check.jsx";



function App() {
const data = [
        {"title":"Learn React", "description":"In-depth"},{"title":"Hi","description": "Hello"}]
  return (


        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/udemy" element={<CourseGoal title={data[0].title} description={data[0].description}  />} />

        </Routes>

  )
}

export default App
