import React, {useState} from 'react';
import axios from 'axios';
import "../css/Upload.css";
import Loading from '../components/loading';

function Upload(props){
    const [img,setImg] = useState(null);
    const [fileUrl, setFileUrl] = useState(null);
    const [result,setResult] = useState(null);
    const [isLoading,setIsLoading] = useState(false);
    const uploadImg = (e) => {
      const currentFile = e.target.files[0];
      setImg(currentFile);
    }

    // 페이지 슬라이드
    // const handleTop2 = () => {
    //   windowScrollBy(window, { behavior: "smooth", top: 795, left: 0 });
    // }
  
    // const postImg = () => {
    //   const formData = new FormData();
    //   formData.append('file', img);
    //   console.log(img);
    //   axios.post("http://localhost:5000/api/fileUpload", formData).then(response=>{
    //     console.log(response.data);
    //     setResult(response.data);
    //   })
    //   .catch(err=>{console.log('Failed to send img file to server');})
    // }

    const onSubmit = () => {
      setIsLoading(true);
      const formData = new FormData();
      formData.append('file', img);
      console.log(img);
      axios.post("http://localhost:5000/api/fileUpload", formData).then(response=>{
        console.log(response.data);
        props.onSubmit(response.data.url,response.data.result);
        setIsLoading(false);
      })
      .catch(err=>{
        console.log('Failed to send img file to server');
      })
      // props.onSubmit(response.data);
    }

    
    return (
      <div className='App defalutBGC2' >
        <div className='leftPart'>
            <h2 className='second'>Second step</h2>
            <h1 className='upload'>UPLOAD</h1>
            <h1 className='your'>YOUR</h1>
            <h1 className='picture'>PICTURE</h1>

            {img == null ? <p></p> :<img src={fileUrl}/>}
            <label for="profile-upload" className='selectPic'>Select a picture</label>
            <input id="profile-upload" type="file" accept="image/*" style={{display:"none"}} onChange={uploadImg}/>
            {/* <button onClick={postImg}>관상 보기</button> */}
            {isLoading?<Loading/>:<button onClick={onSubmit} className='loadResult'>Check the result</button>}
        </div>

        <div className='rightPart'>
            <div className='uploadImg' />
            <div className='details'>
                <div className='circles'>
                    <div className='circle2 C1'></div>
                    <div className='circle2 C2'></div>
                    <div className='circle2 C3'></div>
                </div>
                <hr className='line' />
                <p className='decoText marginAdd'>hackphaistus</p>
                <p className='decoText'>physiognomy</p>
            </div>
        </div>
      </div>
    );
}

export default Upload;