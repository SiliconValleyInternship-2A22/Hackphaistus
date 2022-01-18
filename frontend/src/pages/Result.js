import React, {useState, useEffect} from 'react';
import axios from 'axios';
import "../css/Result.css";
import styled from 'styled-components';

const Result = (props) => {
    
    
    const [result,setResult] = useState(props.skills)
    console.log(result);
    const StatRange = styled.div`
    width: ${props => props.width}%;
    height: 100%;
    background-color: #FE5657;
`;
const getImg = () => {
    axios.post("http://localhost:5000/api/printResult").then(response=>{
      console.log(response.data);
      setResult(response.data);
    })
  }

  

    return(
        <div className='defalutBGC3'>
            <div className='firstpart'>
                <div className='resultImg'></div>
                <div className='overView'></div>
                <div className='topValue'></div>
            </div>
            <div className='secondpart'>
                <div className='containerWrap'>
                    <div className='statContainer'>
                        <h3><span>지</span>혜</h3>
                        <p>지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>{result[0]}</h4>
                        </div>
                        <div className='statBar'>
                            <StatRange width={result[0]}/>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>매</span>력</h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>{result[1]}</h4>
                        </div>
                        <div className='statBar'>
                            <StatRange width={result[1]}/>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>통</span>솔<span>력</span></h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>{result[2]}</h4>
                        </div>
                        <div className='statBar'>
                            <StatRange width={result[2]}/>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>열</span>정</h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>{result[3]}</h4>
                        </div>
                        <div className='statBar'>
                            <StatRange width={result[3]}/>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>사</span>회<span>성</span></h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>{result[4]}</h4>
                        </div>
                        <div className='statBar'>
                            <StatRange width={result[4]}/>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>신</span>뢰<span>도</span></h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>{result[5]}</h4>
                        </div>
                        <div className='statBar'>
                            <StatRange width={result[5]}/>
                        </div>
                    </div>
                </div>
            </div>
            <div className='lastPart'>
                <button className='restartBtn'>Restart</button>
                <button className='saveBtn'>Save</button>
            </div>
        </div>
    );
}

export default Result;
