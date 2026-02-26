'use client';

import { useState, useEffect } from 'react';
import IndiaMapWithHover from './IndiaMapWithHover';

interface HeroSectionProps {
  onStartSimulation?: () => void;
}

export default function HeroSection({ onStartSimulation }: HeroSectionProps) {
  const [stats] = useState({ cities: 37, states: 36, accuracy: 99.86, faster: 85, cost: 0 });
  const [hoveredState, setHoveredState] = useState<string | null>(null);
  const [stateData, setStateData] = useState<any>(null);
  const [tooltipPos, setTooltipPos] = useState({ x: 0, y: 0 });

  // Track global mouse position
  useEffect(() => {
    const handleGlobalMouseMove = (e: MouseEvent) => {
      if (hoveredState) {
        setTooltipPos({ x: e.clientX, y: e.clientY });
      }
    };

    window.addEventListener('mousemove', handleGlobalMouseMove);
    return () => window.removeEventListener('mousemove', handleGlobalMouseMove);
  }, [hoveredState]);

  const handleStateHover = async (stateName: string, x: number, y: number) => {
    console.log('=== HERO HOVER TRIGGERED ===');
    console.log('State Name:', stateName);
    console.log('Position:', x, y);
    setHoveredState(stateName);
    setTooltipPos({ x, y });
    console.log('hoveredState set to:', stateName);
    
    try {
      const response = await fetch(`http://localhost:8000/india/state-data/${stateName}`);
      const data = await response.json();
      console.log('State data received:', data);
      setStateData(data);
    } catch (error) {
      console.error('Error fetching state data:', error);
    }
  };

  const handleStateLeave = () => {
    setHoveredState(null);
    setStateData(null);
  };

  return (
    <section className="relative bg-gradient-to-br from-blue-900 via-blue-800 to-indigo-900 text-white py-16">
      {/* Indian Flag Accent */}
      <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-500 via-white to-green-600"></div>

      <div className="container mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
          {/* Left Content */}
          <div className="space-y-8 pt-8">
            {/* Badge */}
            <div className="inline-flex items-center space-x-2 bg-orange-500 bg-opacity-20 px-4 py-2 rounded border border-orange-400">
              <svg className="w-5 h-5 text-orange-400" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
              <span className="text-sm font-semibold text-orange-300">Government of India Initiative</span>
            </div>

            {/* Main Heading */}
            <div>
              <h1 className="text-5xl lg:text-6xl font-bold leading-tight mb-4">
                <span className="text-white">Complete </span>
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-orange-400 to-green-400">India</span>
                <br />
                <span className="text-white">Policy Simulation</span>
              </h1>
              <p className="text-xl text-gray-300 leading-relaxed">
                Covering <span className="text-orange-400 font-semibold">ALL 28 States + 8 UTs</span> with 
                real data and <span className="text-green-400 font-semibold">99.86% accuracy</span>. 
                Make informed decisions for every corner of India.
              </p>
            </div>

            {/* Features Grid */}
            <div className="grid grid-cols-2 gap-4">
              <div className="flex items-start space-x-3">
                <svg className="w-6 h-6 text-green-400 flex-shrink-0 mt-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                <div>
                  <div className="font-semibold text-white">Complete Coverage</div>
                  <div className="text-sm text-gray-400">All 36 states & UTs</div>
                </div>
              </div>
              <div className="flex items-start space-x-3">
                <svg className="w-6 h-6 text-green-400 flex-shrink-0 mt-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                <div>
                  <div className="font-semibold text-white">6 AI Agents</div>
                  <div className="text-sm text-gray-400">Advanced orchestration</div>
                </div>
              </div>
              <div className="flex items-start space-x-3">
                <svg className="w-6 h-6 text-green-400 flex-shrink-0 mt-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                <div>
                  <div className="font-semibold text-white">100% FREE</div>
                  <div className="text-sm text-gray-400">No paid APIs</div>
                </div>
              </div>
              <div className="flex items-start space-x-3">
                <svg className="w-6 h-6 text-green-400 flex-shrink-0 mt-1" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                <div>
                  <div className="font-semibold text-white">85% Faster</div>
                  <div className="text-sm text-gray-400">Optimized performance</div>
                </div>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-wrap gap-4 pt-4">
              <button 
                onClick={onStartSimulation}
                className="px-8 py-4 bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-lg transition-colors duration-200"
              >
                Start Simulation
              </button>
              <button 
                onClick={() => document.getElementById('states-showcase')?.scrollIntoView({ behavior: 'smooth' })}
                className="px-8 py-4 bg-white bg-opacity-10 hover:bg-opacity-20 text-white font-semibold rounded-lg border border-white border-opacity-30 transition-all duration-200"
              >
                View All States
              </button>
            </div>
          </div>

          {/* Right Content - Interactive Map */}
          <div className="relative">
            <div className="hero-map-container bg-white bg-opacity-5 rounded-2xl p-6">
              <div className="text-center mb-4">
                <h3 className="text-xl font-bold text-white mb-1">
                  Interactive India Map
                </h3>
                <p className="text-sm text-gray-300">Hover over any state for real-time data</p>
              </div>

              <div className="flex justify-center">
                <IndiaMapWithHover
                  onStateHover={handleStateHover}
                  onStateLeave={handleStateLeave}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* State Hover Tooltip */}
      {hoveredState && (
        <div
          className="fixed z-[9999] pointer-events-none"
          style={{ 
            left: `${tooltipPos.x + 15}px`, 
            top: `${tooltipPos.y + 15}px`,
          }}
        >
          <div className="bg-gray-900 text-white rounded-lg shadow-2xl p-4 border-2 border-orange-500 min-w-[300px] max-w-[350px]">
            <div className="font-bold text-lg mb-3 border-b border-orange-500 pb-2 text-orange-400">
              {hoveredState}
            </div>
            {stateData ? (
              <div className="space-y-2 text-sm">
                <div className="flex justify-between">
                  <span className="text-gray-400">Population:</span>
                  <span className="font-semibold">{stateData.demographics.population.toLocaleString('en-IN')}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Vehicles:</span>
                  <span className="font-semibold">{stateData.demographics.vehicles.toLocaleString('en-IN')}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Literacy:</span>
                  <span className="font-semibold">{stateData.demographics.literacy_rate}%</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Congestion:</span>
                  <span className="font-semibold text-orange-400">{stateData.traffic.congestion_level}%</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Income:</span>
                  <span className="font-semibold">₹{stateData.demographics.median_income_inr.toLocaleString('en-IN')}</span>
                </div>
              </div>
            ) : (
              <div className="text-sm text-gray-400 flex items-center space-x-2">
                <div className="w-4 h-4 border-2 border-orange-400 border-t-transparent rounded-full animate-spin"></div>
                <span>Loading data...</span>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Bottom Accent */}
      <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-orange-500 via-white to-green-600"></div>
    </section>
  );
}
