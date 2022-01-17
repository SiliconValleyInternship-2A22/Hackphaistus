import React, {useState} from 'react';
import Main from './pages/Mainscreen'
import Upload from './pages/Upload'
import Result from './pages/Result';
import Header from './components/header';

const App = () => { 
  const [result,setResult] = useState(null);
  const onSubmitResult = (arr) => {
    console.log(arr);
    setResult(arr);
  }
  return (
    <div>
      <Header/>
      <Main/>
      <Upload onSubmit={onSubmitResult}/>
      {result!=null?
      <Result skills={result}/>:<p></p>}
    </div>
  );
}

export default App;