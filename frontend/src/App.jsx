import { useState } from 'react'


function getTitle(name){
    return name;
}
function App() {

  return (
    <>
        <h1>Welcome To Post Management</h1>
        <p>Welcome {getTitle('Deven')}</p>

    </>
  )
}

export default App
