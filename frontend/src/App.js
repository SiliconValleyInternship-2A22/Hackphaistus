import axios from 'axios';

const App = () => {
  const setBtn = () => {
  axios.post("http://localhost:5000/api/checkCors").then(
    response=>{
      console.log(response.data);
    }
  )}
  return (
    <div className="App">
      <p>Hey</p>
      <button onClick={setBtn}>2A22</button>
    </div>
  );
}

export default App;
