import React, {useState} from 'react';
import axios from 'axios';
import Main from './pages/Mainscreen'
import Upload from './pages/Upload'
import Result from './pages/Result';
import Header from './components/header';

const App = () => { 
  
  return (
    <div>
      <Header/>
      <Main/>
      <Upload/>
      <Result/>
    </div>
  );
}

export default App;