import React from 'react';
import "../css/Main.css";
import styled from 'styled-components';
import { windowScrollBy } from "seamless-scroll-polyfill";


function Main(){

      const handleTop2 = () => {
        windowScrollBy(window, { behavior: "smooth", top: 795, left: 0 });
      }

    return(
        <div className='defalutBGC'>
            <div className='star'></div>
            <button className='start' onClick={handleTop2}>Getting Start</button>
            <p className='first'>The first</p>
            <div className='mainCon'>
                <div className='mainImg' />
                <div className='mainTitle'>
                    <div className='titleCon1'>
                        <h1 className='hackphaistus'><span className='pink'>HACK</span>PH</h1>
                        <h1 className='hackphaistus'>AISTUS</h1>
                    </div>
                </div>
                <div className='subCon_B'>
                    <div className='subText'>
                        <h1 className='subTitle_B'>HACKPH</h1>
                        <h1 className='subTitle_B'>AISTUS</h1>
                    </div>
                    <div className='hide_B' />
                </div>
                <div className='subCon_U'>
                    <div className='subText'>
                        <h1 className='subTitle_B'>HACKPH</h1>
                        <h1 className='subTitle_B'>AISTUS</h1>
                    </div>
                    <div className='hide_U' />
                </div>
                <div className='backLight'/>
            </div>
            <div className='deco'>
                <div className='circleCon'>
                    <div className='circle'></div>
                    <div className='circle cdB'></div>
                    <div className='circle'></div>
                </div>
                <div className='otherDeco'></div>
            </div>
            <p className='year'>2022</p>
            <p className='SV'>Silicon Valley</p>
        </div>
    );
}

export default Main;