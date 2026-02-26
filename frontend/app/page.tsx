'use client'

import { useState } from 'react'
import Header from './components/Header'
import Footer from './components/Footer'
import HeroSection from './components/HeroSection'
import FeaturesSection from './components/FeaturesSection'
import StatesShowcase from './components/StatesShowcase'
import PolicyInput from './components/PolicyInput'
import Dashboard from './components/Dashboard'
import PolicyDocumentation from './components/PolicyDocumentation'
import InteractiveIndiaMap from './components/InteractiveIndiaMap'
import { useSimulationStore } from './store/simulationStore'

type ViewMode = 'home' | 'simulator' | 'documentation'

export default function Home() {
  const { simulationResult, isLoading } = useSimulationStore()
  const [viewMode, setViewMode] = useState<ViewMode>('home')

  return (
    <div className="min-h-screen flex flex-col">
      <Header onNavigate={setViewMode} currentView={viewMode} />
      
      <main className="flex-grow">
        {viewMode === 'home' ? (
          <>
            <HeroSection onStartSimulation={() => setViewMode('simulator')} />
            <FeaturesSection />
            <StatesShowcase onStartSimulation={() => setViewMode('simulator')} />
            
            {/* CTA Section */}
            <section className="py-20 bg-gradient-to-r from-blue-900 to-indigo-900 text-white">
              <div className="container mx-auto px-4 text-center">
                <h2 className="text-4xl font-bold mb-6">
                  Ready to Start Simulating?
                </h2>
                <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
                  Experience the power of AI-driven policy analysis with real data from all 36 states and UTs
                </p>
                <div className="flex justify-center space-x-4">
                  <button
                    onClick={() => setViewMode('simulator')}
                    className="px-12 py-5 bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white text-lg font-semibold rounded-lg shadow-2xl transform hover:scale-105 transition-all duration-200"
                  >
                    Launch Simulator Now
                  </button>
                  <button
                    onClick={() => setViewMode('documentation')}
                    className="px-12 py-5 bg-white hover:bg-gray-100 text-blue-900 text-lg font-semibold rounded-lg shadow-2xl transform hover:scale-105 transition-all duration-200"
                  >
                    📚 View Policy Docs
                  </button>
                </div>
              </div>
            </section>
          </>
        ) : viewMode === 'simulator' ? (
          <section id="simulator" className="py-12 bg-gray-50">
            <div className="container mx-auto px-4">
              {/* Navigation Tabs */}
              <div className="mb-6 flex items-center justify-between">
                <div className="flex space-x-2">
                  <button
                    onClick={() => setViewMode('home')}
                    className="flex items-center space-x-2 px-4 py-2 text-blue-600 hover:text-blue-700 font-medium hover:bg-blue-50 rounded-lg transition-colors"
                  >
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    <span>Home</span>
                  </button>
                  <button
                    onClick={() => setViewMode('documentation')}
                    className="flex items-center space-x-2 px-4 py-2 text-gray-600 hover:text-blue-600 font-medium hover:bg-blue-50 rounded-lg transition-colors"
                  >
                    <span>📚</span>
                    <span>Policy Documentation</span>
                  </button>
                </div>
              </div>

              {/* Simulator Header */}
              <div className="bg-gradient-to-r from-blue-900 to-indigo-900 text-white rounded-2xl p-8 mb-8 shadow-xl">
                <h1 className="text-3xl font-bold mb-2">Policy Simulator</h1>
                <p className="text-gray-300">
                  Select from 37 cities across all 28 states and 8 UTs to run AI-powered simulations
                </p>
              </div>

              {/* Simulator Content */}
              <div className="space-y-6">
                {/* Top Section - Region Select and Policy Input side by side */}
                <PolicyInput />
                
                
                {/* Results Section - Full width below */}
                {isLoading && (
                  <div className="bg-white rounded-2xl shadow-xl p-12">
                    <div className="flex flex-col items-center justify-center">
                      <div className="relative w-24 h-24 mb-6">
                        <div className="absolute inset-0 border-4 border-blue-200 rounded-full"></div>
                        <div className="absolute inset-0 border-4 border-blue-600 rounded-full border-t-transparent animate-spin"></div>
                      </div>
                      <h3 className="text-xl font-semibold text-gray-900 mb-2">
                        Running Simulation...
                      </h3>
                      <p className="text-gray-600 text-center">
                        AI agents are analyzing your policy with real Indian data
                      </p>
                    </div>
                  </div>
                )}
                
                {!isLoading && simulationResult && (
                  <div id="results-section" className="scroll-mt-6">
                    <Dashboard data={simulationResult} />
                  </div>
                )}
                
                {!isLoading && !simulationResult && (
                  <div className="bg-white rounded-2xl shadow-xl p-12 text-center">
                    <div className="w-24 h-24 mx-auto mb-6 bg-blue-100 rounded-full flex items-center justify-center">
                      <svg className="w-12 h-12 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                      </svg>
                    </div>
                    <h3 className="text-2xl font-bold text-gray-900 mb-3">
                      Ready to Simulate
                    </h3>
                    <p className="text-gray-600 mb-6">
                      Enter your policy details above to begin the simulation
                    </p>
                    <div className="flex items-center justify-center space-x-2 text-sm text-gray-500">
                      <svg className="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                      </svg>
                      <span>6 AI Agents Ready</span>
                      <span className="text-gray-400">•</span>
                      <span>99.86% Accuracy</span>
                      <span className="text-gray-400">•</span>
                      <span>36 States & UTs Available</span>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </section>
        ) : (
          <section id="documentation" className="py-12 bg-gray-50">
            <div className="container mx-auto px-4">
              {/* Navigation Tabs */}
              <div className="mb-6 flex items-center justify-between">
                <div className="flex space-x-2">
                  <button
                    onClick={() => setViewMode('home')}
                    className="flex items-center space-x-2 px-4 py-2 text-blue-600 hover:text-blue-700 font-medium hover:bg-blue-50 rounded-lg transition-colors"
                  >
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    <span>Home</span>
                  </button>
                  <button
                    onClick={() => setViewMode('simulator')}
                    className="flex items-center space-x-2 px-4 py-2 text-gray-600 hover:text-blue-600 font-medium hover:bg-blue-50 rounded-lg transition-colors"
                  >
                    <span>🎯</span>
                    <span>Run Simulation</span>
                  </button>
                </div>
              </div>

              {/* Documentation Component */}
              <PolicyDocumentation />
            </div>
          </section>
        )}
      </main>
      
      <Footer />
    </div>
  )
}
