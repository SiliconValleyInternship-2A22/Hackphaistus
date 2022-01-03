import React, {useState} from 'react';
import axios from 'axios';

const App = () => {
  
   const [fileUrl, setFileUrl] = useState(null);
  
   function processImage(event){
    event.preventDefault();

    const imageFile = event.target.files[0];

    const imageUrl = URL.createObjectURL(imageFile);
    setFileUrl(imageUrl)

    
  }

  const setBtn = (fileUrl) => {
    const formData = new FormData()
    const config = {
      header: {'content-type': 'multipart/form-data'}
  }
  formData.append('file',fileUrl)

      

  axios.post("http://localhost:5000/api/checkCors" , formData, config).then(
    response=>{
      if (response.data.success) {
        alert('파일 저장 성공?!')
    } else {
        alert('파일 저장 실패')
    }
    }
  )}

  return (
    <div className='App'>
      <img alt="hey" src={fileUrl}></img>
    <input id="profile-upload" type="file" accept="image/*" onChange={processImage}/>
    <button onClick={setBtn}>2A22</button>
    </div>
  );
}

export default App;
