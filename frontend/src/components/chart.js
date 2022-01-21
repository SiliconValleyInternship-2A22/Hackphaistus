import React, { PureComponent } from 'react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  {
    name: '지혜',
    uv: 40,
    pv: 24,
    amt: 24,
    score: 100,
  },
  {
    name: '매력',
    uv: 30,
    pv: 13,
    amt: 22,
    score: 80,
  },
  {
    name: '통솔력',
    uv: 20,
    pv: 98,
    amt: 22,
    score: 54,
  },
  {
    name: '열정',
    uv: 27,
    pv: 39,
    amt: 20,
    score: 43,
  },
  {
    name: '사회성',
    uv: 18,
    pv: 48,
    amt: 21,
    score: 64,
  },
  {
    name: '신뢰도',
    uv: 23,
    pv: 38,
    amt: 25,
    score: 52,
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
          <Area type="monotone" dataKey="score" stroke="#da3939" fill="#661E1E" />
        </AreaChart>
      </ResponsiveContainer>
    );
  }
}