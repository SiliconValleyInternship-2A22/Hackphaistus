import React, {useState, useEffect, useRef} from 'react';
import "../css/Result.css";
import styled from 'styled-components';
import Chart from '../components/chart'
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
            <div id='topWrap'>
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
                        <p> 매력있는 사람은 타인의 시선을 끄는 능력이 뛰어납니다. 관상학적으로 매력이 있는 사람은 
                            도화가 있는 사람을 의미하며, 이는 인간 관계에서 경쟁력을 가질 수 있지만 한편으로는 불필요한 
                            갈등을 겪을 수 있습니다.</p>
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
                        <p> 통솔력이 뛰어난 사람은 주변 사람들을 이끌고 효율적으로 문제를 해결하는 능력이 뛰어납니다. 이들은 평소 
                            주변 사람들을 이끌어 공동의 목표를 달성하는데 능하고, 사회성이 좋으며 무엇이든 강단있게 해결해나갈 수 있습니다.</p>
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
                        <p> 열정이 가득한 사람은 높은 집중력과 적극성을 무언가를 해냅니다. 이들은 이러한 활동을 통해 얻는 성취감을 좋아하고, 
                            배움을 게을리하지 않습니다. 이러한 특성 떄문에, 이들 중에는 사회적 성취를 이룬 사람이 많습니다.</p>
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
                        <p> 사회성이 뛰어난 사람은 타인으로부터 배척받지 않고 호감을 얻는 능력이 뛰어납니다. 이들은 눈치가 빠르고, 
                            상대의 기분을 매우 세심하게 알아차립니다. 또한 이들은 사고가 유연하여 어떤 문제에 대한 대처능력이 뛰어납니다.</p>
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
                        <p> 신뢰도를 주는 사람은 믿음직스럽고, 정직한 인상을 가집니다. 이들은 정의롭고 가치관이 뚜렷하여, 주변 사람들은 
                            이들을 호감있는 인물로 생각할 가능성이 높습니다. 이들은 비교적 쉽게 타인의 신뢰를 얻습니다.</p>
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
            </div>
            <div className='lastPart'>
                <button className='restartBtn' onClick={onRefresh}>Restart</button>
                <button className='saveBtn' onClick={onDownloadBtn}>Save</button>
            </div>
        </div>
    );
}

export default Result;