import React, {useState, useEffect, useRef} from 'react';
import "../css/Result.css";
import styled from 'styled-components';
import Chart from '../components/chart'

// const newArr = [...result];
//     newArr = newArr.sort((a, b) => b - a);
//     setResult(newArr);

import domtoimage from 'dom-to-image';
import { saveAs } from 'file-saver';

const Result = (props) => {

    const [result,setResult] = useState(props.skills);
    const [url,setUrl] = useState(props.image);
    const [newArr, setNewArr] = useState(result);
    // console.log(result)
    // console.log(url)
    // console.log(newArr)

    const secondArr = [['지혜',result[0]],['매력',result[1]],['통솔력',result[2]],['열정',result[3]],['사회성',result[4]],['신뢰도',result[5]]];
    //console.log(secondArr);

    secondArr.sort((a,b) => b[1]-a[1]);
    //console.log(secondArr);

    

    const ResultImg = styled.div`
        width: 200px;
        height: 200px;
        border-radius: 150px;
        background-image: url(${props => props.url});
        background-size: cover;
        margin-right: 27px;
        margin-top: 10px;
    `
    const StatRange = styled.div`
    width: ${props => props.width}%;
    height: 100%;
    background-color: #FE5657;
`;
    // const onSaveResult = () => {
    //     const final = {data:data}
    //     axios({
	// 		url: 'http://localhost:5000/api/exportResult', //your url
	// 		method: 'POST',
	// 		data: final,
	// 		responseType: 'blob', // important
	// 	  })
	// .then((response) => {
	// 	const url = window.URL.createObjectURL(new Blob([response.data]));
	// 	const link = document.createElement('a');
	// 	link.href = url;
	// 	link.setAttribute('download', 'result.csv'); //or any other extension
	// 	document.body.appendChild(link);
	// 	link.click();
	//  });
    // }

    const onRefresh = () => {
        window.location.reload();
    }
    const resultRef = useRef();
    const onDownloadBtn = () => {
        const resultCap = resultRef.current;
        domtoimage.toBlob(resultCap)
        .then((blob) => {
        saveAs(blob, 'Hackphaistus.png');
        });
    };

    return(
        <div className='defalutBGC3' ref={resultRef}>
            <div className='firstpart'>
                <ResultImg url={url}/>
                <div className='overView'>
                    <h2><span>O</span>VERVIEW</h2>
                    <Chart skills={result}/>
                </div>
                <div className='topValue'>
                    <h2><span>T</span>OP 3 VALUE</h2>
                    <div className='topCon'>
                        <div>
                            <div className='title'>
                                <h4>{secondArr[0][0]}</h4>
                                <h4>{secondArr[0][1]}</h4>
                            </div>
                            <div className='statBar'>
                                <StatRange width={secondArr[0][1]}/>
                            </div>
                        </div>
                        <div>
                            <div className='title'>
                                <h4>{secondArr[1][0]}</h4>
                                <h4>{secondArr[1][1]}</h4>
                            </div>
                            <div className='statBar'>
                                <StatRange width={secondArr[0][1]}/>
                            </div>
                        </div>
                        <div>
                            <div className='title'>
                                <h4>{secondArr[2][0]}</h4>
                                <h4>{secondArr[2][1]}</h4>
                            </div>
                            <div className='statBar'>
                                <StatRange width={secondArr[2][1]}/>
                            </div>
                        </div>
                    </div>
                </div>
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
                    <h3><span>통</span>솔력</h3>
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
                    <h3><span>사</span>회성</h3>
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
                    <h3><span>신</span>뢰도</h3>
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
                <button className='restartBtn' onClick={onRefresh}>Restart</button>
                <button className='saveBtn' onClick={onDownloadBtn}>Save</button>
            </div>
        </div>
    );
}

export default Result;
