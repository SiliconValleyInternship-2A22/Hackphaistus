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

      

  axios.post("http://localhost:5000/api/fileUpload" , formData, config).then(response=>{
      console.log(response.data);
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
