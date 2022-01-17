import React from 'react';
import "../css/Result.css";
import styled from 'styled-components';

function Result(){

    const statRange = styled.div`
    width: 80%;
    height: 100%;
   
    background-color: #FE5657;
`;

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
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>80</h4>
                        </div>
                        <div className='statBar'>
                            <div className='statRange'></div>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>지</span>혜</h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>80</h4>
                        </div>
                        <div className='statBar'>
                            <div className='statRange'></div>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>지</span>혜</h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>80</h4>
                        </div>
                        <div className='statBar'>
                            <div className='statRange'></div>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>지</span>혜</h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>80</h4>
                        </div>
                        <div className='statBar'>
                            <div className='statRange'></div>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>지</span>혜</h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>80</h4>
                        </div>
                        <div className='statBar'>
                            <div className='statRange'></div>
                        </div>
                    </div>
                    <div className='statContainer'>
                    <h3><span>지</span>혜</h3>
                        <p> 지혜로운 사람은 평소 사리를 분별하며 적절히 처리하는 능력이 뛰어납니다. 이들의 
                            특징은 평소 주변 사람들에 대한 이해가 뛰어나고, 효율적으로 자신의 지식 및 주변 환경을 
                            이용하여 원하는 결과를 생성하는 것입니다.</p>
                        <div className='title'>
                            <h4>점수</h4>
                            <h4>80</h4>
                        </div>
                        <div className='statBar'>
                            <div className='statRange'></div>
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
