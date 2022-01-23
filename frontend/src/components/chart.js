import React, { PureComponent, useState, useEffect } from 'react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';


// const Arr = (props) => {
//   const [result,setResult] = useState(props.skills);

  const data = [
    {
      name: '지혜',
      score: 10,
    },
    {
      name: '매력',
      score: 20,
    },
    {
      name: '통솔력',
      score: 30,
    },
    {
      name: '열정',
      score: 20,
    },
    {
      name: '사회성',
      score: 40,
    },
    {
      name: '신뢰도',
      score: 50,
      //score:result[5]
    },
  ];

export default class Chart extends PureComponent {
  static demoUrl = 'https://codesandbox.io/s/simple-area-chart-4ujxw';

  

  render() {
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
          <Area type="monotone" dataKey={data} stroke="#da3939" fill="#661E1E" />
        </AreaChart>
      </ResponsiveContainer>
    );
  }
}