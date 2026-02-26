import { create } from 'zustand'
import axios from 'axios'

const API_BASE = 'http://localhost:8000'

interface Region {
  state: string
}

interface SimulationResult {
  simulation_id: string
  results: {
    metrics: any
    impact_predictions: any
    optimization: any
    explanation: any
  }
}

interface SimulationStore {
  simulationResult: SimulationResult | null
  isLoading: boolean
  error: string | null
  runSimulation: (policyText: string, enableOptimization: boolean, region?: Region) => Promise<void>
  reset: () => void
}

export const useSimulationStore = create<SimulationStore>((set) => ({
  simulationResult: null,
  isLoading: false,
  error: null,

  runSimulation: async (policyText: string, enableOptimization: boolean, region?: Region) => {
    set({ isLoading: true, error: null })
    
    try {
      const payload: any = {
        policy_text: policyText,
        enable_optimization: enableOptimization
      }

      // Add region if provided
      if (region) {
        payload.region = region
      }

      const response = await axios.post(`${API_BASE}/simulation/simulate`, payload)
      
      set({ 
        simulationResult: response.data,
        isLoading: false 
      })

      // Auto-scroll to results section after a brief delay
      setTimeout(() => {
        const resultsSection = document.getElementById('results-section')
        if (resultsSection) {
          resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }
      }, 100)
    } catch (error: any) {
      set({ 
        error: error.message,
        isLoading: false 
      })
    }
  },

  reset: () => set({ simulationResult: null, error: null })
}))
