import React, {useState} from 'react';
import axios from 'axios';

const App = () => { 
  const [img,setImg] = useState(null);
  const [fileUrl, setFileUrl] = useState(null);
  const uploadImg = (e) => {
    const currentFile = e.target.files[0];
    setImg(currentFile);
  }

  const postImg = () => {
    const formData = new FormData();
    formData.append('file', img);
    console.log(img);
    axios.post("http://localhost:5000/api/fileUpload", formData).then(response=>{
      console.log(response.data);
    })
    .catch(err=>{console.log('Failed to send img file to server');})
  }
  
  const getImg = () => {
    axios.post("http://localhost:5000/api/printResult").then(response=>{
      console.log(response.data);
    })
  }

  return (
    <div className='App'>
      {img == null ? <p></p> :<img src={fileUrl}/>}
      <input id="profile-upload" type="file" accept="image/*" onChange={uploadImg}/>
      <button onClick={postImg}>관상 보기</button>
      <button onClick={getImg}>결과 출력</button>
    </div>
  );
}

export default App;