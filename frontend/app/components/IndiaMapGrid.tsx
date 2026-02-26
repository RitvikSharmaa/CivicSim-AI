'use client';

import { useState } from 'react';

interface IndiaMapGridProps {
  onStateHover?: (stateName: string, event: React.MouseEvent) => void;
  onStateLeave?: () => void;
  onStateClick?: (stateName: string) => void;
}

const STATES = [
  { name: 'Jammu and Kashmir', region: 'North', color: '#3b82f6' },
  { name: 'Ladakh', region: 'North', color: '#3b82f6' },
  { name: 'Himachal Pradesh', region: 'North', color: '#3b82f6' },
  { name: 'Punjab', region: 'North', color: '#3b82f6' },
  { name: 'Chandigarh', region: 'North', color: '#3b82f6' },
  { name: 'Uttarakhand', region: 'North', color: '#3b82f6' },
  { name: 'Haryana', region: 'North', color: '#3b82f6' },
  { name: 'Delhi', region: 'North', color: '#3b82f6' },
  { name: 'Rajasthan', region: 'West', color: '#8b5cf6' },
  { name: 'Uttar Pradesh', region: 'Central', color: '#10b981' },
  { name: 'Bihar', region: 'East', color: '#f59e0b' },
  { name: 'Sikkim', region: 'Northeast', color: '#ec4899' },
  { name: 'Arunachal Pradesh', region: 'Northeast', color: '#ec4899' },
  { name: 'Nagaland', region: 'Northeast', color: '#ec4899' },
  { name: 'Manipur', region: 'Northeast', color: '#ec4899' },
  { name: 'Mizoram', region: 'Northeast', color: '#ec4899' },
  { name: 'Tripura', region: 'Northeast', color: '#ec4899' },
  { name: 'Meghalaya', region: 'Northeast', color: '#ec4899' },
  { name: 'Assam', region: 'Northeast', color: '#ec4899' },
  { name: 'West Bengal', region: 'East', color: '#f59e0b' },
  { name: 'Jharkhand', region: 'East', color: '#f59e0b' },
  { name: 'Odisha', region: 'East', color: '#f59e0b' },
  { name: 'Chhattisgarh', region: 'Central', color: '#10b981' },
  { name: 'Madhya Pradesh', region: 'Central', color: '#10b981' },
  { name: 'Gujarat', region: 'West', color: '#8b5cf6' },
  { name: 'Dadra and Nagar Haveli and Daman and Diu', region: 'West', color: '#8b5cf6' },
  { name: 'Maharashtra', region: 'West', color: '#8b5cf6' },
  { name: 'Goa', region: 'West', color: '#8b5cf6' },
  { name: 'Telangana', region: 'South', color: '#ef4444' },
  { name: 'Andhra Pradesh', region: 'South', color: '#ef4444' },
  { name: 'Karnataka', region: 'South', color: '#ef4444' },
  { name: 'Kerala', region: 'South', color: '#ef4444' },
  { name: 'Tamil Nadu', region: 'South', color: '#ef4444' },
  { name: 'Puducherry', region: 'South', color: '#ef4444' },
  { name: 'Andaman and Nicobar Islands', region: 'South', color: '#ef4444' },
  { name: 'Lakshadweep', region: 'South', color: '#ef4444' },
];

export default function IndiaMapGrid({ onStateHover, onStateLeave, onStateClick }: IndiaMapGridProps) {
  const [hoveredState, setHoveredState] = useState<string | null>(null);

  const handleMouseEnter = (stateName: string, event: React.MouseEvent) => {
    setHoveredState(stateName);
    onStateHover?.(stateName, event);
  };

  const handleMouseLeave = () => {
    setHoveredState(null);
    onStateLeave?.();
  };

  const handleClick = (stateName: string) => {
    onStateClick?.(stateName);
  };

  const getStateColor = (state: typeof STATES[0]) => {
    if (hoveredState === state.name) {
      return '#f59e0b'; // Orange on hover
    }
    return state.color;
  };

  // Group states by region
  const regions = {
    'North': STATES.filter(s => s.region === 'North'),
    'Northeast': STATES.filter(s => s.region === 'Northeast'),
    'East': STATES.filter(s => s.region === 'East'),
    'Central': STATES.filter(s => s.region === 'Central'),
    'West': STATES.filter(s => s.region === 'West'),
    'South': STATES.filter(s => s.region === 'South'),
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-6">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {Object.entries(regions).map(([regionName, states]) => (
          <div key={regionName} className="bg-white bg-opacity-10 rounded-lg p-4">
            <h3 className="text-lg font-bold text-white mb-3 border-b border-white border-opacity-30 pb-2">
              {regionName}
            </h3>
            <div className="space-y-2">
              {states.map((state) => (
                <div
                  key={state.name}
                  className="px-3 py-2 rounded cursor-pointer transition-all duration-200 text-sm"
                  style={{
                    backgroundColor: getStateColor(state),
                    transform: hoveredState === state.name ? 'scale(1.05)' : 'scale(1)',
                  }}
                  onMouseEnter={(e) => handleMouseEnter(state.name, e)}
                  onMouseMove={(e) => onStateHover?.(state.name, e)}
                  onMouseLeave={handleMouseLeave}
                  onClick={() => handleClick(state.name)}
                >
                  <span className="text-white font-medium">{state.name}</span>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
      
      {/* Legend */}
      <div className="mt-6 flex flex-wrap justify-center gap-4 text-sm">
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 rounded" style={{ backgroundColor: '#3b82f6' }}></div>
          <span className="text-white">North</span>
        </div>
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 rounded" style={{ backgroundColor: '#ec4899' }}></div>
          <span className="text-white">Northeast</span>
        </div>
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 rounded" style={{ backgroundColor: '#f59e0b' }}></div>
          <span className="text-white">East</span>
        </div>
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 rounded" style={{ backgroundColor: '#10b981' }}></div>
          <span className="text-white">Central</span>
        </div>
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 rounded" style={{ backgroundColor: '#8b5cf6' }}></div>
          <span className="text-white">West</span>
        </div>
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 rounded" style={{ backgroundColor: '#ef4444' }}></div>
          <span className="text-white">South</span>
        </div>
      </div>
    </div>
  );
}
