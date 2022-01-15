import React from 'react';
import "../css/Result.css";
import styled from 'styled-components';

function Result(){

    return(
        <div className='defalutBGC3'>
            <div className='firstpart'>
                <div className='resultImg'></div>
                <div className='overView'></div>
                <div className='topValue'></div>
            </div>
            <div className='secondpart'>
                <div className='containerWrap'>
                    <div className='statContainer'></div>
                    <div className='statContainer'></div>
                    <div className='statContainer'></div>
                    <div className='statContainer'></div>
                    <div className='statContainer'></div>
                    <div className='statContainer'></div>
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
