'use client'

import MetricsCard from './MetricsCard'
import ImpactChart from './ImpactChart'
import ExplanationPanel from './ExplanationPanel'

interface DashboardProps {
  data: any
}

export default function Dashboard({ data }: DashboardProps) {
  const { results } = data
  const { metrics, impact_predictions, optimization, explanation } = results

  return (
    <div className="space-y-6">
      {/* Metrics Overview */}
      <div className="grid grid-cols-2 gap-4">
        <MetricsCard
          title="Congestion Score"
          value={metrics?.congestion_score}
          predicted={impact_predictions?.congestion_score}
          unit=""
          color="blue"
        />
        <MetricsCard
          title="Dissatisfaction Index"
          value={metrics?.dissatisfaction_index}
          predicted={impact_predictions?.dissatisfaction_index}
          unit=""
          color="red"
        />
        <MetricsCard
          title="Energy Load"
          value={metrics?.energy_load}
          predicted={impact_predictions?.energy_stress}
          unit=""
          color="yellow"
        />
        <MetricsCard
          title="Economic Stability"
          value={metrics?.economic_stability}
          predicted={null}
          unit=""
          color="green"
        />
      </div>

      {/* Impact Predictions Chart */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-xl font-semibold mb-4">Impact Predictions</h3>
        <ImpactChart data={impact_predictions} />
      </div>

      {/* Optimization Results */}
      {optimization && (
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-xl font-semibold mb-4">Optimization Results</h3>
          <div className="grid grid-cols-3 gap-4">
            <div>
              <p className="text-sm text-gray-600">Reward Score</p>
              <p className="text-2xl font-bold text-primary">
                {optimization.reward_score?.toFixed(2)}
              </p>
            </div>
            <div>
              <p className="text-sm text-gray-600">Improvement</p>
              <p className="text-2xl font-bold text-green-600">
                +{optimization.improvement_percentage?.toFixed(1)}%
              </p>
            </div>
            <div>
              <p className="text-sm text-gray-600">Cost Efficiency</p>
              <p className="text-2xl font-bold text-blue-600">
                {(optimization.comparison_metrics?.cost_efficiency * 100)?.toFixed(0)}%
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Explanation Panel */}
      {explanation && <ExplanationPanel explanation={explanation} />}
    </div>
  )
}
