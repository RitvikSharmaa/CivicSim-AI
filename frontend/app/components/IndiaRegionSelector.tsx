'use client'

import { useState, useEffect } from 'react'

interface Region {
  state: string
}

interface RegionSelectorProps {
  onRegionChange: (region: Region) => void
}

// ALL 28 STATES + 8 UTs - COMPLETE COVERAGE
const INDIAN_STATES = [
  // States (28)
  "Andhra Pradesh",
  "Arunachal Pradesh",
  "Assam",
  "Bihar",
  "Chhattisgarh",
  "Goa",
  "Gujarat",
  "Haryana",
  "Himachal Pradesh",
  "Jharkhand",
  "Karnataka",
  "Kerala",
  "Madhya Pradesh",
  "Maharashtra",
  "Manipur",
  "Meghalaya",
  "Mizoram",
  "Nagaland",
  "Odisha",
  "Punjab",
  "Rajasthan",
  "Sikkim",
  "Tamil Nadu",
  "Telangana",
  "Tripura",
  "Uttar Pradesh",
  "Uttarakhand",
  "West Bengal",
  
  // Union Territories (8)
  "Andaman and Nicobar Islands",
  "Chandigarh",
  "Dadra and Nagar Haveli and Daman and Diu",
  "Delhi",
  "Jammu and Kashmir",
  "Ladakh",
  "Lakshadweep",
  "Puducherry"
]

export default function IndiaRegionSelector({ onRegionChange }: RegionSelectorProps) {
  const [state, setState] = useState("Karnataka")
  const [stateData, setStateData] = useState<any>(null)
  const [loading, setLoading] = useState(false)
  const [searchQuery, setSearchQuery] = useState("")

  useEffect(() => {
    fetchStateData(state)
  }, [state])

  const fetchStateData = async (selectedState: string) => {
    setLoading(true)
    try {
      // Fetch aggregated state data
      const response = await fetch(`http://localhost:8000/india/state-data/${selectedState}`)
      const data = await response.json()
      setStateData(data)
      onRegionChange({ state: selectedState })
    } catch (error) {
      console.error('Error fetching state data:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleStateChange = (newState: string) => {
    setState(newState)
  }

  // Filter states based on search
  const filteredStates = INDIAN_STATES.filter(s =>
    s.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const stateCount = INDIAN_STATES.length

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 mb-6 border-2 border-gray-100">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-900 flex items-center space-x-2">
            <span>🇮🇳</span>
            <span>Select State/UT</span>
          </h2>
          <p className="text-sm text-gray-600 mt-1">
            {stateCount} States & Union Territories
          </p>
        </div>
        <div className="text-right">
          <div className="text-xs text-gray-500">Coverage</div>
          <div className="text-lg font-bold text-green-600">100%</div>
        </div>
      </div>

      {/* Search */}
      <div className="mb-4">
        <div className="relative">
          <input
            type="text"
            placeholder="Search states/UTs..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full px-4 py-2 pl-10 border-2 border-gray-200 rounded-lg focus:border-orange-500 focus:outline-none transition-colors"
          />
          <svg className="w-5 h-5 text-gray-400 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
      </div>
      
      {/* State Selector */}
      <div className="mb-4">
        <label className="block text-sm font-semibold text-gray-700 mb-2">
          State / Union Territory
        </label>
        <select
          value={state}
          onChange={(e) => handleStateChange(e.target.value)}
          className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:border-orange-500 transition-colors font-medium text-lg"
        >
          {filteredStates.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
      </div>

      {/* Loading State */}
      {loading && (
        <div className="text-center py-8">
          <div className="relative w-16 h-16 mx-auto mb-4">
            <div className="absolute inset-0 border-4 border-orange-200 rounded-full"></div>
            <div className="absolute inset-0 border-4 border-orange-500 rounded-full border-t-transparent animate-spin"></div>
          </div>
          <p className="text-gray-600">Loading real data...</p>
        </div>
      )}

      {/* State Data Display */}
      {stateData && !loading && (
        <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-6 mt-4 border-2 border-blue-200">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-bold text-gray-900">
              Real Data for {state}
            </h3>
            <span className="px-3 py-1 bg-green-500 text-white text-xs font-semibold rounded-full">
              LIVE DATA
            </span>
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            {/* Population */}
            <div className="bg-white rounded-lg p-4 shadow-sm">
              <div className="flex items-center space-x-2 mb-2">
                <svg className="w-5 h-5 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
                </svg>
                <span className="text-xs text-gray-600 font-medium">Population</span>
              </div>
              <div className="text-xl font-bold text-gray-900">
                {stateData.demographics.population.toLocaleString('en-IN')}
              </div>
            </div>

            {/* Vehicles */}
            <div className="bg-white rounded-lg p-4 shadow-sm">
              <div className="flex items-center space-x-2 mb-2">
                <svg className="w-5 h-5 text-purple-500" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M8 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM15 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z" />
                  <path d="M3 4a1 1 0 00-1 1v10a1 1 0 001 1h1.05a2.5 2.5 0 014.9 0H10a1 1 0 001-1V5a1 1 0 00-1-1H3zM14 7a1 1 0 00-1 1v6.05A2.5 2.5 0 0115.95 16H17a1 1 0 001-1v-5a1 1 0 00-.293-.707l-2-2A1 1 0 0015 7h-1z" />
                </svg>
                <span className="text-xs text-gray-600 font-medium">Vehicles</span>
              </div>
              <div className="text-xl font-bold text-gray-900">
                {stateData.demographics.vehicles.toLocaleString('en-IN')}
              </div>
            </div>

            {/* Congestion */}
            <div className="bg-white rounded-lg p-4 shadow-sm">
              <div className="flex items-center space-x-2 mb-2">
                <svg className="w-5 h-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                </svg>
                <span className="text-xs text-gray-600 font-medium">Congestion</span>
              </div>
              <div className="text-xl font-bold text-red-600">
                {stateData.traffic.congestion_level}%
              </div>
            </div>

            {/* Speed */}
            <div className="bg-white rounded-lg p-4 shadow-sm">
              <div className="flex items-center space-x-2 mb-2">
                <svg className="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
                </svg>
                <span className="text-xs text-gray-600 font-medium">Avg Speed</span>
              </div>
              <div className="text-xl font-bold text-gray-900">
                {stateData.traffic.avg_speed_kmph} km/h
              </div>
            </div>

            {/* Literacy */}
            <div className="bg-white rounded-lg p-4 shadow-sm">
              <div className="flex items-center space-x-2 mb-2">
                <svg className="w-5 h-5 text-indigo-500" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z" />
                </svg>
                <span className="text-xs text-gray-600 font-medium">Literacy</span>
              </div>
              <div className="text-xl font-bold text-gray-900">
                {stateData.demographics.literacy_rate}%
              </div>
            </div>

            {/* Income */}
            <div className="bg-white rounded-lg p-4 shadow-sm">
              <div className="flex items-center space-x-2 mb-2">
                <svg className="w-5 h-5 text-yellow-500" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M8.433 7.418c.155-.103.346-.196.567-.267v1.698a2.305 2.305 0 01-.567-.267C8.07 8.34 8 8.114 8 8c0-.114.07-.34.433-.582zM11 12.849v-1.698c.22.071.412.164.567.267.364.243.433.468.433.582 0 .114-.07.34-.433.582a2.305 2.305 0 01-.567.267z" />
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-13a1 1 0 10-2 0v.092a4.535 4.535 0 00-1.676.662C6.602 6.234 6 7.009 6 8c0 .99.602 1.765 1.324 2.246.48.32 1.054.545 1.676.662v1.941c-.391-.127-.68-.317-.843-.504a1 1 0 10-1.51 1.31c.562.649 1.413 1.076 2.353 1.253V15a1 1 0 102 0v-.092a4.535 4.535 0 001.676-.662C13.398 13.766 14 12.991 14 12c0-.99-.602-1.765-1.324-2.246A4.535 4.535 0 0011 9.092V7.151c.391.127.68.317.843.504a1 1 0 101.511-1.31c-.563-.649-1.413-1.076-2.354-1.253V5z" clipRule="evenodd" />
                </svg>
                <span className="text-xs text-gray-600 font-medium">Median Income</span>
              </div>
              <div className="text-xl font-bold text-gray-900">
                ₹{stateData.demographics.median_income_inr.toLocaleString('en-IN')}
              </div>
            </div>
          </div>

          {/* Cities Count */}
          {stateData.demographics.cities_count && (
            <div className="mt-4 bg-white rounded-lg p-3">
              <div className="text-sm text-gray-600">
                <span className="font-semibold">Cities covered:</span> {stateData.demographics.cities_count}
              </div>
            </div>
          )}

          {/* Data Source Badge */}
          <div className="mt-4 flex items-center justify-between text-xs">
            <div className="flex items-center space-x-2 text-green-600">
              <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              <span className="font-semibold">100% FREE Data</span>
            </div>
            <span className="text-gray-500">
              Census India • TomTom • RBI
            </span>
          </div>
        </div>
      )}
    </div>
  )
}
