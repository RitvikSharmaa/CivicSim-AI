'use client';

import { useState, useEffect } from 'react';

interface State {
  name: string;
  capital: string;
  type: 'state' | 'ut';
  region: string;
}

interface StatesShowcaseProps {
  onStartSimulation?: () => void;
}

export default function StatesShowcase({ onStartSimulation }: StatesShowcaseProps) {
  const [selectedRegion, setSelectedRegion] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [cityData, setCityData] = useState<Record<string, any>>({});
  const [expandedState, setExpandedState] = useState<string | null>(null);

  const states: State[] = [
    // North
    { name: 'Delhi', capital: 'New Delhi', type: 'ut', region: 'North' },
    { name: 'Haryana', capital: 'Chandigarh', type: 'state', region: 'North' },
    { name: 'Himachal Pradesh', capital: 'Shimla', type: 'state', region: 'North' },
    { name: 'Jammu and Kashmir', capital: 'Srinagar', type: 'ut', region: 'North' },
    { name: 'Ladakh', capital: 'Leh', type: 'ut', region: 'North' },
    { name: 'Punjab', capital: 'Chandigarh', type: 'state', region: 'North' },
    { name: 'Chandigarh', capital: 'Chandigarh', type: 'ut', region: 'North' },
    { name: 'Uttarakhand', capital: 'Dehradun', type: 'state', region: 'North' },
    
    // South
    { name: 'Andhra Pradesh', capital: 'Amaravati', type: 'state', region: 'South' },
    { name: 'Karnataka', capital: 'Bengaluru', type: 'state', region: 'South' },
    { name: 'Kerala', capital: 'Thiruvananthapuram', type: 'state', region: 'South' },
    { name: 'Tamil Nadu', capital: 'Chennai', type: 'state', region: 'South' },
    { name: 'Telangana', capital: 'Hyderabad', type: 'state', region: 'South' },
    { name: 'Puducherry', capital: 'Puducherry', type: 'ut', region: 'South' },
    { name: 'Lakshadweep', capital: 'Kavaratti', type: 'ut', region: 'South' },
    { name: 'Andaman and Nicobar Islands', capital: 'Port Blair', type: 'ut', region: 'South' },
    
    // East
    { name: 'Bihar', capital: 'Patna', type: 'state', region: 'East' },
    { name: 'Jharkhand', capital: 'Ranchi', type: 'state', region: 'East' },
    { name: 'Odisha', capital: 'Bhubaneswar', type: 'state', region: 'East' },
    { name: 'West Bengal', capital: 'Kolkata', type: 'state', region: 'East' },
    
    // West
    { name: 'Goa', capital: 'Panaji', type: 'state', region: 'West' },
    { name: 'Gujarat', capital: 'Gandhinagar', type: 'state', region: 'West' },
    { name: 'Maharashtra', capital: 'Mumbai', type: 'state', region: 'West' },
    { name: 'Rajasthan', capital: 'Jaipur', type: 'state', region: 'West' },
    { name: 'Dadra and Nagar Haveli and Daman and Diu', capital: 'Daman', type: 'ut', region: 'West' },
    
    // Central
    { name: 'Chhattisgarh', capital: 'Raipur', type: 'state', region: 'Central' },
    { name: 'Madhya Pradesh', capital: 'Bhopal', type: 'state', region: 'Central' },
    { name: 'Uttar Pradesh', capital: 'Lucknow', type: 'state', region: 'Central' },
    
    // Northeast
    { name: 'Arunachal Pradesh', capital: 'Itanagar', type: 'state', region: 'Northeast' },
    { name: 'Assam', capital: 'Dispur', type: 'state', region: 'Northeast' },
    { name: 'Manipur', capital: 'Imphal', type: 'state', region: 'Northeast' },
    { name: 'Meghalaya', capital: 'Shillong', type: 'state', region: 'Northeast' },
    { name: 'Mizoram', capital: 'Aizawl', type: 'state', region: 'Northeast' },
    { name: 'Nagaland', capital: 'Kohima', type: 'state', region: 'Northeast' },
    { name: 'Sikkim', capital: 'Gangtok', type: 'state', region: 'Northeast' },
    { name: 'Tripura', capital: 'Agartala', type: 'state', region: 'Northeast' },
  ];

  const regions = ['all', 'North', 'South', 'East', 'West', 'Central', 'Northeast'];

  const filteredStates = states.filter(state => {
    const matchesRegion = selectedRegion === 'all' || state.region === selectedRegion;
    const matchesSearch = state.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         state.capital.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesRegion && matchesSearch;
  });

  const stateCount = filteredStates.filter(s => s.type === 'state').length;
  const utCount = filteredStates.filter(s => s.type === 'ut').length;

  // Fetch city data when component mounts
  useEffect(() => {
    const fetchCityData = async () => {
      try {
        const response = await fetch('http://localhost:8000/india/cities');
        const data = await response.json();
        
        // Create a map of state -> city data
        const dataMap: Record<string, any> = {};
        data.cities.forEach((city: any) => {
          dataMap[city.state] = city;
        });
        setCityData(dataMap);
      } catch (error) {
        console.error('Error fetching city data:', error);
      }
    };
    
    fetchCityData();
  }, []);

  const handleViewData = (state: State) => {
    // Toggle expanded state
    if (expandedState === state.name) {
      setExpandedState(null);
    } else {
      setExpandedState(state.name);
    }
  };

  const handleStartSimulation = () => {
    if (onStartSimulation) {
      onStartSimulation();
    }
  };

  return (
    <section id="states-showcase" className="py-20 bg-gradient-to-b from-white to-gray-50">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="text-center mb-12">
          <div className="inline-flex items-center space-x-2 bg-orange-100 px-4 py-2 rounded-full mb-4">
            <svg className="w-5 h-5 text-orange-600" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M3 6a3 3 0 013-3h10a1 1 0 01.8 1.6L14.25 8l2.55 3.4A1 1 0 0116 13H6a1 1 0 00-1 1v3a1 1 0 11-2 0V6z" clipRule="evenodd" />
            </svg>
            <span className="text-sm font-semibold text-orange-600">Complete Coverage</span>
          </div>
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            All <span className="text-orange-500">28 States</span> + <span className="text-green-600">8 UTs</span>
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Comprehensive policy simulation for every corner of India with real government data
          </p>
        </div>

        {/* Filters */}
        <div className="mb-8 space-y-4">
          {/* Search */}
          <div className="max-w-md mx-auto">
            <div className="relative">
              <input
                type="text"
                placeholder="Search states or capitals..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full px-4 py-3 pl-12 rounded-lg border-2 border-gray-200 focus:border-orange-500 focus:outline-none transition-colors"
              />
              <svg className="w-5 h-5 text-gray-400 absolute left-4 top-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
          </div>

          {/* Region Filters */}
          <div className="flex flex-wrap justify-center gap-2">
            {regions.map((region) => (
              <button
                key={region}
                onClick={() => setSelectedRegion(region)}
                className={`px-6 py-2 rounded-full font-medium transition-all duration-200 ${
                  selectedRegion === region
                    ? 'bg-gradient-to-r from-orange-500 to-orange-600 text-white shadow-lg'
                    : 'bg-white text-gray-700 hover:bg-gray-100 border border-gray-200'
                }`}
              >
                {region === 'all' ? 'All Regions' : region}
              </button>
            ))}
          </div>

          {/* Stats */}
          <div className="flex justify-center gap-6 text-sm">
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
              <span className="text-gray-600">{stateCount} States</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-green-500 rounded-full"></div>
              <span className="text-gray-600">{utCount} Union Territories</span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-orange-500 rounded-full"></div>
              <span className="text-gray-600">{filteredStates.length} Total</span>
            </div>
          </div>
        </div>

        {/* States Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          {filteredStates.map((state, index) => {
            const isExpanded = expandedState === state.name;
            const data = cityData[state.name];
            
            return (
              <div
                key={index}
                className={`group bg-white rounded-xl shadow-md hover:shadow-xl transition-all duration-300 border-2 ${
                  isExpanded ? 'border-orange-400 ring-2 ring-orange-200' : 'border-gray-100 hover:border-orange-300'
                }`}
              >
                <div className="p-6">
                  {/* State Badge */}
                  <div className="flex items-center justify-between mb-3">
                    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                      state.type === 'state'
                        ? 'bg-blue-100 text-blue-700'
                        : 'bg-green-100 text-green-700'
                    }`}>
                      {state.type === 'state' ? 'State' : 'UT'}
                    </span>
                    <span className="text-xs text-gray-500 font-medium">{state.region}</span>
                  </div>

                  {/* State Name */}
                  <h3 className={`text-lg font-bold mb-2 transition-colors ${
                    isExpanded ? 'text-orange-600' : 'text-gray-900 group-hover:text-orange-600'
                  }`}>
                    {state.name}
                  </h3>

                  {/* Capital */}
                  <div className="flex items-center space-x-2 text-gray-600 mb-3">
                    <svg className="w-4 h-4 text-orange-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clipRule="evenodd" />
                    </svg>
                    <span className="text-sm font-medium">{state.capital}</span>
                  </div>

                  {/* Compact Data Preview */}
                  {data && !isExpanded && (
                    <div className="mb-3 p-3 bg-gray-50 rounded-lg space-y-1">
                      <div className="flex justify-between text-xs">
                        <span className="text-gray-600">Population:</span>
                        <span className="font-semibold text-gray-900">{data.population.toLocaleString()}</span>
                      </div>
                      <div className="flex justify-between text-xs">
                        <span className="text-gray-600">Literacy:</span>
                        <span className="font-semibold text-gray-900">{data.literacy_rate}%</span>
                      </div>
                    </div>
                  )}

                  {/* Expanded Data View */}
                  {isExpanded && data && (
                    <div className="mb-4 p-4 bg-gradient-to-br from-orange-50 to-orange-100 rounded-lg border border-orange-200 space-y-3">
                      <div className="flex items-center justify-between pb-2 border-b border-orange-200">
                        <span className="text-xs font-semibold text-orange-700 uppercase">Detailed Information</span>
                      </div>
                      
                      <div className="space-y-2">
                        <div className="flex justify-between items-center">
                          <div className="flex items-center space-x-2">
                            <svg className="w-4 h-4 text-orange-600" fill="currentColor" viewBox="0 0 20 20">
                              <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
                            </svg>
                            <span className="text-sm text-gray-700">Population</span>
                          </div>
                          <span className="text-sm font-bold text-gray-900">{data.population.toLocaleString()}</span>
                        </div>

                        <div className="flex justify-between items-center">
                          <div className="flex items-center space-x-2">
                            <svg className="w-4 h-4 text-orange-600" fill="currentColor" viewBox="0 0 20 20">
                              <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z" />
                            </svg>
                            <span className="text-sm text-gray-700">Literacy Rate</span>
                          </div>
                          <span className="text-sm font-bold text-gray-900">{data.literacy_rate}%</span>
                        </div>

                        <div className="flex justify-between items-center">
                          <div className="flex items-center space-x-2">
                            <svg className="w-4 h-4 text-orange-600" fill="currentColor" viewBox="0 0 20 20">
                              <path fillRule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clipRule="evenodd" />
                            </svg>
                            <span className="text-sm text-gray-700">Region</span>
                          </div>
                          <span className="text-sm font-bold text-gray-900">{data.region}</span>
                        </div>
                      </div>

                      {/* Quick Action in Expanded View */}
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          handleStartSimulation();
                        }}
                        className="w-full mt-2 py-2 bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white text-sm font-semibold rounded-lg transition-all duration-200 flex items-center justify-center space-x-2"
                      >
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                        </svg>
                        <span>Simulate for {state.name}</span>
                      </button>
                    </div>
                  )}

                  {/* Action Button */}
                  <button 
                    onClick={() => handleViewData(state)}
                    className={`w-full py-2 font-semibold rounded-lg transition-all duration-200 text-sm flex items-center justify-center space-x-2 ${
                      isExpanded
                        ? 'bg-gray-100 hover:bg-gray-200 text-gray-700'
                        : 'bg-gradient-to-r from-orange-50 to-orange-100 hover:from-orange-100 hover:to-orange-200 text-orange-600'
                    }`}
                  >
                    {isExpanded ? (
                      <>
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 15l7-7 7 7" />
                        </svg>
                        <span>Show Less</span>
                      </>
                    ) : (
                      <>
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                        </svg>
                        <span>View Details</span>
                      </>
                    )}
                  </button>
                </div>
              </div>
            );
          })}
        </div>

        {/* No Results */}
        {filteredStates.length === 0 && (
          <div className="text-center py-12">
            <svg className="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p className="text-gray-600 text-lg">No states found matching your search</p>
          </div>
        )}

        {/* Bottom CTA */}
        <div className="mt-16 text-center">
          <div className="inline-flex flex-col items-center space-y-4 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-2xl p-8 border-2 border-blue-200">
            <h3 className="text-2xl font-bold text-gray-900">
              Ready to simulate for your state?
            </h3>
            <p className="text-gray-600">
              Select any state or UT to run AI-powered policy simulations
            </p>
            <button 
              onClick={handleStartSimulation}
              className="px-8 py-4 bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white font-semibold rounded-lg shadow-lg transform hover:scale-105 transition-all duration-200"
            >
              Start Simulation
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}
