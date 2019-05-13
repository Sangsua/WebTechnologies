import React from 'react';
import ReactDOM from 'react-dom';

 /* Components */
 import { Header_Home } from "./home/Header_Home";
 import { Main_Home } from "./home/Main_Home";
 import { Account_Home } from "./home/Account_Home";

  /* Stylesheet */
  import './css/style.css';
 

  function Home() {
 
    return (
      <div className="App">
  
          <Header_Home/>
          <Main_Home/>
          <Account_Home/>
          
      </div>
    );
  }
  
  
ReactDOM.render(routing, document.getElementById('root'));