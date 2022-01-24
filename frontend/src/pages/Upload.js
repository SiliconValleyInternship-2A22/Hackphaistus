import React, {useState, useEffect} from 'react';
import axios from 'axios';
import "../css/Upload.css";
import Loading from '../components/loading';
import { windowScrollBy } from "seamless-scroll-polyfill";

function Upload(props){
    const [img,setImg] = useState(null);
    const [fileUrl, setFileUrl] = useState(null);
    const [filename,setFilename] = useState(null);
    const [taskID,setTaskID] = useState(1);
    const [isLoading,setIsLoading] = useState(false);
    const uploadImg = (e) => {
      const currentFile = e.target.files[0];
      setImg(currentFile);
    }

    // 페이지 슬라이드
    const handleTop2 = () => {
      windowScrollBy(window, { behavior: "smooth", top: 750, left: 0 });
    }
  
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
  //   useEffect(() => {
  //     axios.post("http://localhost:5000/api/receiveSignal")
  // }, []);

    const onSubmit = () => {
      setIsLoading(true);
      const formData = new FormData();
      formData.append('file', img);
      console.log(img);
      setFilename(img.name);
      axios.post("http://localhost:5000/api/fileUpload", formData).then(response=>{
        console.log(response.data);
        props.onSubmit(response.data.url,response.data.result);
        setIsLoading(false);
        handleTop2();
        // const task_id = response.data.task;
        // const req = setInterval(() => {
        //   axios.post("http://localhost:5000/api/printResult",{'id':task_id}).then(response=>{
        //   if (response.data.result.length != 0){ 
        //       props.onSubmit(response.data.url,response.data.result);
        //       setIsLoading(false);
        //       return clearInterval(req);
        //   }
        // })}, 5000);
        // setTaskID(response.data.task+1);
      })
      .catch(err=>{
        console.log('Failed to send img file to server');
      })
    }

    // const [counter,setCounter] = useState(0);
    // useEffect(() => {
    //   const req = setInterval(() => {
    //     //console.log(taskID);
    //     axios.post("http://localhost:5000/api/printResult",{'id':taskID}).then(response=>{
    //       console.log(response.data);
    //       //return clearInterval(req);
    //     if (response.data.result.length != 0){ 
    //       //if (response.data.file === filename){
    //         //console.log(filename);
    //         props.onSubmit(response.data.url,response.data.result);
    //         setIsLoading(false);
    //         return clearInterval(req);
    //     }
    //   })}, 10000);
    // }, [filename]);
    
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