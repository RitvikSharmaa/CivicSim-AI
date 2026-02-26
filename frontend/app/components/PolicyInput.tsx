'use client'

import { useState } from 'react'
import { useSimulationStore } from '../store/simulationStore'
import IndiaRegionSelector from './IndiaRegionSelector'

interface Region {
  state: string
}

export default function PolicyInput() {
  const [policyText, setPolicyText] = useState('')
  const [enableOptimization, setEnableOptimization] = useState(true)
  const [region, setRegion] = useState<Region>({ state: 'Karnataka' })
  const { runSimulation, isLoading } = useSimulationStore()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (policyText.trim()) {
      await runSimulation(policyText, enableOptimization, region)
    }
  }

  const handleRegionChange = (newRegion: Region) => {
    setRegion(newRegion)
  }

  const examplePolicies = [
    "Increase metro rail budget by ₹5000 crore to reduce traffic congestion",
    "Provide ₹2000 monthly assistance to women heads of families",
    "Build 100 new EV charging stations across the city with ₹500 crore investment",
    "Expand free healthcare coverage to ₹5 lakh per family annually",
    "Increase education budget by ₹3000 crore for government schools"
  ]

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      {/* Region Selector */}
      <IndiaRegionSelector onRegionChange={handleRegionChange} />

      {/* Policy Input */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-2xl font-semibold mb-4">Policy Input</h2>
        
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Describe your policy
            </label>
            <textarea
              value={policyText}
              onChange={(e) => setPolicyText(e.target.value)}
              className="w-full h-32 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
              placeholder="Enter policy description in natural language..."
              disabled={isLoading}
            />
          </div>

          <div className="mb-4">
            <label className="flex items-center">
              <input
                type="checkbox"
                checked={enableOptimization}
                onChange={(e) => setEnableOptimization(e.target.checked)}
                className="mr-2"
                disabled={isLoading}
              />
              <span className="text-sm text-gray-700">Enable AI Optimization</span>
            </label>
          </div>

          <button
            type="submit"
            disabled={isLoading || !policyText.trim()}
            className="w-full bg-primary text-white py-2 px-4 rounded-md hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed transition"
          >
            {isLoading ? 'Simulating...' : 'Run Simulation'}
          </button>
        </form>

        <div className="mt-6">
          <p className="text-sm font-medium text-gray-700 mb-2">Example Policies:</p>
          <div className="space-y-2">
            {examplePolicies.map((example, idx) => (
              <button
                key={idx}
                onClick={() => setPolicyText(example)}
                className="w-full text-left text-sm text-gray-600 hover:text-primary p-2 rounded hover:bg-gray-50 transition"
                disabled={isLoading}
              >
                {example}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
