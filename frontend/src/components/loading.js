import { BallTriangle, TailSpin } from 'react-loader-spinner';
import styled from "styled-components";

function Loading () {

    const Flex = styled.div`
    position: absolute;
    left: 40.5vw;
    top: 180vh;
`;


    return(
        <Flex>
            <TailSpin color="#FE5657" height={30} width={30} />
        </Flex>
    );
}

export default Loading;