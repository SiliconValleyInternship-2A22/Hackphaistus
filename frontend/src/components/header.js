import React from 'react';
import styled from 'styled-components';


const Positioner = styled.div`
    display: flex;
    flex-direction: column;
    position: fixed;
    top: 0px;
    width: 100%;
`;

const WhiteBackground = styled.div`
    background: linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(4,4,4,0) 100%);
    display: flex;
    justify-content: center;
    height: auto;
`;

const HeaderContents = styled.div`
    width: 100%;
    height: 5.5vh;
    display: flex;
    flex-direction: row;
    align-items: center;
`;

const Logo = styled.div`
    width: 2.5vw;
    height: 4vh;

    background-image: url('/logo.png');
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    margin: auto;
`;

const Header = ({children}) => {
    return (
        <Positioner>
            <WhiteBackground>
                <HeaderContents>
                    <Logo />
                    {children}
                </HeaderContents>
            </WhiteBackground>
        </Positioner>
    );
};

export default Header;