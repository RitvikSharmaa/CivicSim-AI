'use client'

import { useState, useEffect } from 'react'

interface PolicyDoc {
  state: string
  category: string
  policy: string
  data: any
}

export default function PolicyDocumentation() {
  const [activeTab, setActiveTab] = useState<'national' | 'state' | 'search'>('national')
  const [selectedState, setSelectedState] = useState('Karnataka')
  const [selectedCategory, setSelectedCategory] = useState('economic')
  const [searchQuery, setSearchQuery] = useState('')
  const [searchResults, setSearchResults] = useState<PolicyDoc[]>([])
  const [nationalPolicies, setNationalPolicies] = useState<any>(null)
  const [statePolicies, setStatePolicies] = useState<any>(null)
  const [loading, setLoading] = useState(false)
  const [availableStates, setAvailableStates] = useState<string[]>([])

  const categories = [
    { id: 'economic', name: 'Economic', icon: '💼' },
    { id: 'social', name: 'Social Welfare', icon: '🤝' },
    { id: 'infrastructure', name: 'Infrastructure', icon: '🏗️' },
    { id: 'agriculture', name: 'Agriculture', icon: '🌾' },
    { id: 'education', name: 'Education', icon: '📚' }
  ]

  useEffect(() => {
    fetchAvailableStates()
    // Load initial national policies
    fetchNationalPolicies('economic')
  }, [])

  useEffect(() => {
    if (activeTab === 'national') {
      fetchNationalPolicies(selectedCategory)
    } else if (activeTab === 'state') {
      fetchStatePolicies(selectedState)
    }
  }, [activeTab, selectedCategory, selectedState])

  const fetchAvailableStates = async () => {
    try {
      const response = await fetch('http://localhost:8000/knowledge/states')
      const data = await response.json()
      setAvailableStates(data.states.map((s: any) => s.state))
    } catch (error) {
      console.error('Error fetching states:', error)
    }
  }

  const fetchNationalPolicies = async (category: string) => {
    setLoading(true)
    try {
      console.log('Fetching national policies for category:', category)
      const response = await fetch(`http://localhost:8000/knowledge/national/${category}`)
      const data = await response.json()
      console.log('National policies data:', data)
      setNationalPolicies(data)
    } catch (error) {
      console.error('Error fetching national policies:', error)
      setNationalPolicies(null)
    } finally {
      setLoading(false)
    }
  }

  const fetchStatePolicies = async (state: string) => {
    setLoading(true)
    try {
      const response = await fetch(`http://localhost:8000/knowledge/state/${state}`)
      const data = await response.json()
      setStatePolicies(data)
    } catch (error) {
      console.error('Error fetching state policies:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSearch = async () => {
    if (!searchQuery.trim()) return
    
    setLoading(true)
    try {
      const response = await fetch(`http://localhost:8000/knowledge/search?q=${encodeURIComponent(searchQuery)}`)
      const data = await response.json()
      setSearchResults(data.results || [])
    } catch (error) {
      console.error('Error searching policies:', error)
    } finally {
      setLoading(false)
    }
  }

  const formatCurrency = (amount: number) => {
    if (amount >= 10000000) {
      return `₹${(amount / 10000000).toFixed(2)} crore`
    } else if (amount >= 100000) {
      return `₹${(amount / 100000).toFixed(2)} lakh`
    }
    return `₹${amount.toLocaleString('en-IN')}`
  }

  return (
    <div className="bg-white rounded-xl shadow-lg">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-900 to-indigo-900 text-white p-6 rounded-t-xl">
        <h2 className="text-2xl font-bold mb-2">📚 Policy Documentation & Research</h2>
        <p className="text-gray-300">
          Explore 60+ government policies, schemes, and budget documents from across India
        </p>
      </div>

      {/* Tabs */}
      <div className="border-b border-gray-200">
        <div className="flex space-x-1 p-2">
          <button
            onClick={() => setActiveTab('national')}
            className={`flex-1 py-3 px-4 rounded-lg font-semibold transition-all ${
              activeTab === 'national'
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            🇮🇳 National Policies
          </button>
          <button
            onClick={() => setActiveTab('state')}
            className={`flex-1 py-3 px-4 rounded-lg font-semibold transition-all ${
              activeTab === 'state'
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            🏛️ State Policies
          </button>
          <button
            onClick={() => setActiveTab('search')}
            className={`flex-1 py-3 px-4 rounded-lg font-semibold transition-all ${
              activeTab === 'search'
                ? 'bg-blue-600 text-white shadow-md'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            🔍 Search
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="p-6">
        {/* National Policies Tab */}
        {activeTab === 'national' && (
          <div>
            {/* Category Selector */}
            <div className="mb-6">
              <label className="block text-sm font-semibold text-gray-700 mb-3">
                Select Category
              </label>
              <div className="grid grid-cols-5 gap-3">
                {categories.map((cat) => (
                  <button
                    key={cat.id}
                    onClick={() => setSelectedCategory(cat.id)}
                    className={`p-4 rounded-lg border-2 transition-all ${
                      selectedCategory === cat.id
                        ? 'border-blue-600 bg-blue-50 shadow-md'
                        : 'border-gray-200 hover:border-blue-300'
                    }`}
                  >
                    <div className="text-3xl mb-2">{cat.icon}</div>
                    <div className="text-sm font-semibold text-gray-900">{cat.name}</div>
                  </button>
                ))}
              </div>
            </div>

            {/* Policies Display */}
            {loading ? (
              <div className="text-center py-12">
                <div className="relative w-16 h-16 mx-auto mb-4">
                  <div className="absolute inset-0 border-4 border-blue-200 rounded-full"></div>
                  <div className="absolute inset-0 border-4 border-blue-600 rounded-full border-t-transparent animate-spin"></div>
                </div>
                <p className="text-gray-600">Loading policies...</p>
              </div>
            ) : nationalPolicies && nationalPolicies.policies && Object.keys(nationalPolicies.policies).length > 0 ? (
              <div className="space-y-4">
                {Object.entries(nationalPolicies.policies).map(([key, policy]: [string, any]) => (
                  <div key={key} className="border-2 border-gray-200 rounded-lg p-5 hover:border-blue-300 transition-all">
                    <div className="flex items-start justify-between mb-3">
                      <h3 className="text-lg font-bold text-gray-900">{policy.name}</h3>
                      <span className="px-3 py-1 bg-blue-100 text-blue-700 text-xs font-semibold rounded-full">
                        National
                      </span>
                    </div>
                    
                    <div className="grid grid-cols-2 gap-4 mb-3">
                      <div>
                        <span className="text-xs text-gray-500 font-medium">Ministry</span>
                        <p className="text-sm text-gray-900">{policy.ministry}</p>
                      </div>
                      <div>
                        <span className="text-xs text-gray-500 font-medium">Launched</span>
                        <p className="text-sm text-gray-900">{policy.launched}</p>
                      </div>
                    </div>

                    <p className="text-sm text-gray-700 mb-3">{policy.objective}</p>

                    {policy.budget_allocation && (
                      <div className="bg-green-50 border border-green-200 rounded-lg p-3 mb-3">
                        <span className="text-xs text-green-700 font-medium">Budget Allocation</span>
                        <p className="text-lg font-bold text-green-900">
                          {formatCurrency(policy.budget_allocation)}
                        </p>
                      </div>
                    )}

                    {policy.total_package && (
                      <div className="bg-green-50 border border-green-200 rounded-lg p-3 mb-3">
                        <span className="text-xs text-green-700 font-medium">Total Package</span>
                        <p className="text-lg font-bold text-green-900">
                          {formatCurrency(policy.total_package)}
                        </p>
                      </div>
                    )}

                    {policy.impact_areas && (
                      <div>
                        <span className="text-xs text-gray-500 font-medium">Impact Areas</span>
                        <div className="flex flex-wrap gap-2 mt-2">
                          {policy.impact_areas.map((area: string, idx: number) => (
                            <span key={idx} className="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded">
                              {area}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-12">
                <div className="text-gray-500 mb-4">
                  {nationalPolicies ? (
                    <>
                      <p>No policies found for this category</p>
                      <p className="text-xs mt-2">Debug: {JSON.stringify(nationalPolicies)}</p>
                    </>
                  ) : (
                    <p>Failed to load policies. Please try again.</p>
                  )}
                </div>
              </div>
            )}
          </div>
        )}

        {/* State Policies Tab */}
        {activeTab === 'state' && (
          <div>
            {/* State Selector */}
            <div className="mb-6">
              <label className="block text-sm font-semibold text-gray-700 mb-3">
                Select State / UT
              </label>
              <select
                value={selectedState}
                onChange={(e) => setSelectedState(e.target.value)}
                className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:border-blue-500 font-medium"
              >
                {availableStates.map((state) => (
                  <option key={state} value={state}>{state}</option>
                ))}
              </select>
            </div>

            {/* State Policies Display */}
            {loading ? (
              <div className="text-center py-12">
                <div className="relative w-16 h-16 mx-auto mb-4">
                  <div className="absolute inset-0 border-4 border-blue-200 rounded-full"></div>
                  <div className="absolute inset-0 border-4 border-blue-600 rounded-full border-t-transparent animate-spin"></div>
                </div>
                <p className="text-gray-600">Loading state policies...</p>
              </div>
            ) : statePolicies && statePolicies.policies ? (
              <div className="space-y-6">
                {Object.entries(statePolicies.policies).map(([category, policies]: [string, any]) => {
                  if (category === 'budget_2025_26') {
                    return (
                      <div key={category} className="border-2 border-orange-200 rounded-lg p-5 bg-orange-50">
                        <h3 className="text-xl font-bold text-gray-900 mb-4">
                          💰 Budget 2025-26
                        </h3>
                        <div className="grid grid-cols-3 gap-4">
                          <div className="bg-white rounded-lg p-4">
                            <span className="text-xs text-gray-500 font-medium">Total Outlay</span>
                            <p className="text-xl font-bold text-gray-900">
                              {formatCurrency(policies.total_outlay)}
                            </p>
                          </div>
                          <div className="bg-white rounded-lg p-4">
                            <span className="text-xs text-gray-500 font-medium">GSDP Projection</span>
                            <p className="text-xl font-bold text-gray-900">
                              {formatCurrency(policies.gsdp_projection)}
                            </p>
                          </div>
                          <div className="bg-white rounded-lg p-4">
                            <span className="text-xs text-gray-500 font-medium">GSDP Growth</span>
                            <p className="text-xl font-bold text-green-600">
                              {policies.gsdp_growth}%
                            </p>
                          </div>
                        </div>
                      </div>
                    )
                  }

                  return (
                    <div key={category}>
                      <h3 className="text-lg font-bold text-gray-900 mb-3 capitalize">
                        {category.replace('_', ' ')}
                      </h3>
                      <div className="space-y-3">
                        {Object.entries(policies).map(([key, policy]: [string, any]) => (
                          <div key={key} className="border-2 border-gray-200 rounded-lg p-4 hover:border-blue-300 transition-all">
                            <div className="flex items-start justify-between mb-2">
                              <h4 className="font-bold text-gray-900">{policy.name}</h4>
                              <span className="px-2 py-1 bg-orange-100 text-orange-700 text-xs font-semibold rounded-full">
                                {selectedState}
                              </span>
                            </div>
                            
                            <p className="text-sm text-gray-700 mb-2">{policy.objective}</p>

                            <div className="grid grid-cols-2 gap-3 text-sm">
                              {policy.budget_allocation && (
                                <div className="bg-green-50 rounded p-2">
                                  <span className="text-xs text-green-700">Budget</span>
                                  <p className="font-bold text-green-900">
                                    {formatCurrency(policy.budget_allocation)}
                                  </p>
                                </div>
                              )}
                              {policy.beneficiaries && (
                                <div className="bg-blue-50 rounded p-2">
                                  <span className="text-xs text-blue-700">Beneficiaries</span>
                                  <p className="font-bold text-blue-900">
                                    {policy.beneficiaries.toLocaleString('en-IN')}
                                  </p>
                                </div>
                              )}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )
                })}
              </div>
            ) : (
              <div className="text-center py-12 text-gray-500">
                No policies found for this state
              </div>
            )}
          </div>
        )}

        {/* Search Tab */}
        {activeTab === 'search' && (
          <div>
            {/* Search Bar */}
            <div className="mb-6">
              <label className="block text-sm font-semibold text-gray-700 mb-3">
                Search Policies
              </label>
              <div className="flex space-x-3">
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
                  placeholder="Search by keyword (e.g., electricity, metro, women, education)..."
                  className="flex-1 px-4 py-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:border-blue-500"
                />
                <button
                  onClick={handleSearch}
                  className="px-8 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Search
                </button>
              </div>
              <p className="text-xs text-gray-500 mt-2">
                Try: "electricity", "metro", "women", "education", "healthcare", "startup"
              </p>
            </div>

            {/* Search Results */}
            {loading ? (
              <div className="text-center py-12">
                <div className="relative w-16 h-16 mx-auto mb-4">
                  <div className="absolute inset-0 border-4 border-blue-200 rounded-full"></div>
                  <div className="absolute inset-0 border-4 border-blue-600 rounded-full border-t-transparent animate-spin"></div>
                </div>
                <p className="text-gray-600">Searching...</p>
              </div>
            ) : searchResults.length > 0 ? (
              <div>
                <p className="text-sm text-gray-600 mb-4">
                  Found {searchResults.length} result{searchResults.length !== 1 ? 's' : ''}
                </p>
                <div className="space-y-4">
                  {searchResults.map((result, idx) => (
                    <div key={idx} className="border-2 border-gray-200 rounded-lg p-5 hover:border-blue-300 transition-all">
                      <div className="flex items-start justify-between mb-3">
                        <h3 className="text-lg font-bold text-gray-900">{result.data.name}</h3>
                        <span className={`px-3 py-1 text-xs font-semibold rounded-full ${
                          result.state === 'National'
                            ? 'bg-blue-100 text-blue-700'
                            : 'bg-orange-100 text-orange-700'
                        }`}>
                          {result.state}
                        </span>
                      </div>
                      
                      <div className="mb-2">
                        <span className="text-xs text-gray-500 font-medium">Category: </span>
                        <span className="text-sm text-gray-900 capitalize">{result.category}</span>
                      </div>

                      <p className="text-sm text-gray-700 mb-3">{result.data.objective}</p>

                      {result.data.budget_allocation && (
                        <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                          <span className="text-xs text-green-700 font-medium">Budget</span>
                          <p className="text-lg font-bold text-green-900">
                            {formatCurrency(result.data.budget_allocation)}
                          </p>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ) : searchQuery ? (
              <div className="text-center py-12 text-gray-500">
                No results found for "{searchQuery}"
              </div>
            ) : (
              <div className="text-center py-12 text-gray-500">
                Enter a search term to find policies
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
