import React, { PureComponent, useState, useEffect } from 'react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const Chart = (props) => {
    const [result,setResult] = useState(props.skills);
    console.log(props.skills)
    const data = [
      {
        name: '지혜',
        score: result[0],
      },
      {
        name: '매력',
        score: result[1],
      },
      {
        name: '통솔력',
        score: result[2],
      },
      {
        name: '열정',
        score: result[3],
      },
      {
        name: '사회성',
        score: result[4],
      },
      {
        name: '신뢰도',
        score: result[5],
      },
    ];  
    return (
      <ResponsiveContainer width="93%" height="80%">
        <AreaChart
          width={500}
          height={400}
          data={data}
          margin={{
            top: 20,
            right: 0,
            left: -16,
            bottom: 0,
          }}
        >
          <CartesianGrid strokeDasharray="1 1" stroke='#8E8E8E'/>
          <XAxis dataKey="name" fontSize={11} />
          <YAxis fontSize={10}/>
          <Tooltip />
          <Area type="monotone" dataKey="score" stroke="#da3939" fill="#661E1E" />
        </AreaChart>
      </ResponsiveContainer>
    );
}


export default Chart;