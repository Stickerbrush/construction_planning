import React, { useState }  from 'react';
import './scss/style.scss';
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import { MyContext } from './MyContext'

function App() {

  const [isLoggedIn, setLoggedIn] = useState(0);
  return (
    <div className="App">
      <MyContext.Provider value = {{isLoggedIn, setLoggedIn}}> 
         {(() => {
           switch (isLoggedIn) {
              case 0:
                  return (
                    <div>
                      <Login/>
                      {console.log(isLoggedIn)}
                    </div>
                  )
              case 1:
                 return (
                    <div>
                      <Dashboard/>
                      {console.log(isLoggedIn)}
                    </div>
                  )
              default:
                  return (
                    <div>You are a User.</div>
                  )
           }
        })()} 
      </MyContext.Provider>
    </div>
  )
}


export default App;
