import React, {useState} from 'react';
import Main from './pages/Mainscreen'
import Upload from './pages/Upload'
import Result from './pages/Result';
import Header from './components/header';

const App = () => { 
  const [result,setResult] = useState(null);
  const [url,setUrl] = useState(null);
  const [ready,setReady] = useState(false);
  const onSubmitResult = (img,arr) => {
    setResult(arr);
    setUrl(img);
    setReady(true);
  }
  return (
    <div>
      <Header/>
      <Main/>
      <Upload onSubmit={onSubmitResult}/>
      {ready == true ?
      <Result skills={result} image={url}/>:<p></p>}
    </div>
  );
}

export default App;