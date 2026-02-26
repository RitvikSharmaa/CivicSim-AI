'use client'

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

interface ImpactChartProps {
  data: any
}

export default function ImpactChart({ data }: ImpactChartProps) {
  if (!data) return null

  const chartData = [
    {
      name: 'Congestion',
      value: data.congestion_score || 0
    },
    {
      name: 'Inflation',
      value: data.inflation_rate || 0
    },
    {
      name: 'Dissatisfaction',
      value: data.dissatisfaction_index || 0
    },
    {
      name: 'Energy Stress',
      value: data.energy_stress || 0
    }
  ]

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="value" fill="#3B82F6" />
      </BarChart>
    </ResponsiveContainer>
  )
}
