'use client'

import { useState, useEffect } from 'react'
import dynamic from 'next/dynamic'

// Dynamically import to avoid SSR issues
const IndiaMap = dynamic(() => import('react-svgmap-india'), { ssr: false })

interface StateData {
  population: number
  vehicles: number
  literacy_rate: number
  congestion_level: number
  median_income_inr: number
}

interface TooltipData {
  name: string
  data: StateData | null
  x: number
  y: number
}

// State code to full name mapping
const STATE_CODES: Record<string, string> = {
  'AN': 'Andaman and Nicobar Islands',
  'AP': 'Andhra Pradesh',
  'AR': 'Arunachal Pradesh',
  'AS': 'Assam',
  'BR': 'Bihar',
  'CH': 'Chandigarh',
  'CT': 'Chhattisgarh',
  'DD': 'Dadra and Nagar Haveli and Daman and Diu',
  'DL': 'Delhi',
  'DN': 'Dadra and Nagar Haveli and Daman and Diu',
  'GA': 'Goa',
  'GJ': 'Gujarat',
  'HP': 'Himachal Pradesh',
  'HR': 'Haryana',
  'JH': 'Jharkhand',
  'JK': 'Jammu and Kashmir',
  'KA': 'Karnataka',
  'KL': 'Kerala',
  'LA': 'Ladakh',
  'LD': 'Lakshadweep',
  'MH': 'Maharashtra',
  'ML': 'Meghalaya',
  'MN': 'Manipur',
  'MP': 'Madhya Pradesh',
  'MZ': 'Mizoram',
  'NL': 'Nagaland',
  'OR': 'Odisha',
  'PB': 'Punjab',
  'PY': 'Puducherry',
  'RJ': 'Rajasthan',
  'SK': 'Sikkim',
  'TG': 'Telangana',
  'TN': 'Tamil Nadu',
  'TR': 'Tripura',
  'UP': 'Uttar Pradesh',
  'UT': 'Uttarakhand',
  'WB': 'West Bengal'
}

export default function InteractiveIndiaMap() {
  const [tooltip, setTooltip] = useState<TooltipData | null>(null)
  const [stateDataCache, setStateDataCache] = useState<Record<string, StateData>>({})
  const [selectedState, setSelectedState] = useState<string | null>(null)

  const fetchStateData = async (stateName: string) => {
    // Check cache first
    if (stateDataCache[stateName]) {
      return stateDataCache[stateName]
    }

    try {
      const response = await fetch(`http://localhost:8000/india/state-data/${stateName}`)
      const data = await response.json()
      
      const stateData: StateData = {
        population: data.demographics.population,
        vehicles: data.demographics.vehicles,
        literacy_rate: data.demographics.literacy_rate,
        congestion_level: data.traffic.congestion_level,
        median_income_inr: data.demographics.median_income_inr
      }

      // Cache the data
      setStateDataCache(prev => ({ ...prev, [stateName]: stateData }))
      return stateData
    } catch (error) {
      console.error('Error fetching state data:', error)
      return null
    }
  }

  const handleMouseEnter = async (event: any, stateCode: string) => {
    const stateName = STATE_CODES[stateCode]
    if (!stateName) return

    const rect = event.target.getBoundingClientRect()
    const data = await fetchStateData(stateName)

    setTooltip({
      name: stateName,
      data,
      x: rect.left + rect.width / 2,
      y: rect.top
    })
  }

  const handleMouseLeave = () => {
    setTooltip(null)
  }

  const handleClick = (stateCode: string) => {
    const stateName = STATE_CODES[stateCode]
    setSelectedState(stateName)
  }

  useEffect(() => {
    // Add event listeners to all state paths
    const mapElement = document.querySelector('.india-map-container svg')
    if (!mapElement) return

    const paths = mapElement.querySelectorAll('path[id]')
    paths.forEach((path) => {
      const stateCode = path.getAttribute('id')
      if (stateCode && STATE_CODES[stateCode]) {
        path.addEventListener('mouseenter', (e) => handleMouseEnter(e, stateCode))
        path.addEventListener('mouseleave', handleMouseLeave)
      }
    })

    return () => {
      paths.forEach((path) => {
        path.removeEventListener('mouseenter', handleMouseEnter as any)
        path.removeEventListener('mouseleave', handleMouseLeave)
      })
    }
  }, [])

  return (
    <div className="relative w-full">
      {/* Map Container */}
      <div className="india-map-container bg-white rounded-xl shadow-lg p-6 border-2 border-gray-100">
        <h3 className="text-2xl font-bold text-gray-900 mb-4 flex items-center space-x-2">
          <span>🗺️</span>
          <span>Interactive India Map</span>
        </h3>
        <p className="text-sm text-gray-600 mb-6">
          Hover over any state to see real-time data • Click to select
        </p>

        <div className="flex justify-center">
          <IndiaMap
            onClick={handleClick}
            size="600px"
            mapColor="#e0f2fe"
            strokeColor="#0369a1"
            strokeWidth="1.5"
            hoverColor="#fbbf24"
          />
        </div>

        {selectedState && (
          <div className="mt-4 p-4 bg-blue-50 rounded-lg border-2 border-blue-200">
            <p className="text-sm font-semibold text-blue-900">
              Selected: <span className="text-lg">{selectedState}</span>
            </p>
          </div>
        )}
      </div>

      {/* Tooltip */}
      {tooltip && (
        <div
          className="fixed z-50 bg-gray-900 text-white rounded-lg shadow-2xl p-4 pointer-events-none transform -translate-x-1/2 -translate-y-full"
          style={{
            left: `${tooltip.x}px`,
            top: `${tooltip.y - 10}px`,
            minWidth: '280px'
          }}
        >
          <div className="font-bold text-lg mb-2 border-b border-gray-700 pb-2">
            {tooltip.name}
          </div>

          {tooltip.data ? (
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-300">Population:</span>
                <span className="font-semibold">{tooltip.data.population.toLocaleString('en-IN')}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-300">Vehicles:</span>
                <span className="font-semibold">{tooltip.data.vehicles.toLocaleString('en-IN')}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-300">Literacy:</span>
                <span className="font-semibold">{tooltip.data.literacy_rate}%</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-300">Congestion:</span>
                <span className="font-semibold text-red-400">{tooltip.data.congestion_level}%</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-300">Median Income:</span>
                <span className="font-semibold">₹{tooltip.data.median_income_inr.toLocaleString('en-IN')}</span>
              </div>
            </div>
          ) : (
            <div className="text-sm text-gray-400 animate-pulse">
              Loading data...
            </div>
          )}

          {/* Arrow */}
          <div className="absolute left-1/2 bottom-0 transform -translate-x-1/2 translate-y-full">
            <div className="w-0 h-0 border-l-8 border-r-8 border-t-8 border-transparent border-t-gray-900"></div>
          </div>
        </div>
      )}

      {/* Legend */}
      <div className="mt-4 bg-white rounded-lg shadow p-4 border border-gray-200">
        <div className="flex items-center justify-between text-sm">
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              <div className="w-4 h-4 bg-sky-200 border-2 border-sky-700 rounded"></div>
              <span className="text-gray-700">Default</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-4 h-4 bg-amber-400 border-2 border-sky-700 rounded"></div>
              <span className="text-gray-700">Hover</span>
            </div>
          </div>
          <div className="text-xs text-gray-500">
            Data: Census India • TomTom • RBI
          </div>
        </div>
      </div>
    </div>
  )
}
