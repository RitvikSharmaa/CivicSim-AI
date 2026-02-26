interface MetricsCardProps {
  title: string
  value: number
  predicted: number | null
  unit: string
  color: 'blue' | 'red' | 'yellow' | 'green'
}

const colorClasses = {
  blue: 'bg-blue-50 text-blue-700 border-blue-200',
  red: 'bg-red-50 text-red-700 border-red-200',
  yellow: 'bg-yellow-50 text-yellow-700 border-yellow-200',
  green: 'bg-green-50 text-green-700 border-green-200'
}

export default function MetricsCard({ title, value, predicted, unit, color }: MetricsCardProps) {
  return (
    <div className={`rounded-lg border-2 p-4 ${colorClasses[color]}`}>
      <h4 className="text-sm font-medium mb-2">{title}</h4>
      <div className="flex items-baseline gap-2">
        <span className="text-3xl font-bold">
          {value?.toFixed(2) || '0.00'}
        </span>
        <span className="text-sm">{unit}</span>
      </div>
      {predicted !== null && (
        <p className="text-xs mt-2">
          Predicted: {predicted?.toFixed(2)}
        </p>
      )}
    </div>
  )
}
