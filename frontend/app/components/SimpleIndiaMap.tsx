'use client';

import { useState } from 'react';

interface SimpleIndiaMapProps {
  onStateHover?: (stateName: string, x: number, y: number) => void;
  onStateLeave?: () => void;
}

const STATES = [
  { name: 'Jammu and Kashmir', x: 200, y: 100, width: 80, height: 60 },
  { name: 'Ladakh', x: 290, y: 80, width: 70, height: 50 },
  { name: 'Himachal Pradesh', x: 220, y: 170, width: 60, height: 40 },
  { name: 'Punjab', x: 200, y: 220, width: 50, height: 40 },
  { name: 'Chandigarh', x: 230, y: 230, width: 15, height: 15 },
  { name: 'Haryana', x: 250, y: 220, width: 50, height: 50 },
  { name: 'Delhi', x: 270, y: 240, width: 15, height: 15 },
  { name: 'Uttarakhand', x: 300, y: 200, width: 60, height: 50 },
  { name: 'Uttar Pradesh', x: 310, y: 260, width: 120, height: 80 },
  { name: 'Rajasthan', x: 150, y: 270, width: 140, height: 120 },
  { name: 'Gujarat', x: 100, y: 400, width: 100, height: 100 },
  { name: 'Madhya Pradesh', x: 250, y: 380, width: 140, height: 100 },
  { name: 'Maharashtra', x: 180, y: 500, width: 140, height: 100 },
  { name: 'Goa', x: 180, y: 610, width: 30, height: 30 },
  { name: 'Karnataka', x: 200, y: 650, width: 100, height: 100 },
  { name: 'Kerala', x: 200, y: 760, width: 60, height: 80 },
  { name: 'Tamil Nadu', x: 270, y: 750, width: 90, height: 100 },
  { name: 'Andhra Pradesh', x: 300, y: 650, width: 100, height: 90 },
  { name: 'Telangana', x: 320, y: 600, width: 80, height: 70 },
  { name: 'Odisha', x: 430, y: 500, width: 80, height: 100 },
  { name: 'Chhattisgarh', x: 390, y: 450, width: 80, height: 80 },
  { name: 'Jharkhand', x: 470, y: 400, width: 70, height: 60 },
  { name: 'Bihar', x: 450, y: 330, width: 90, height: 60 },
  { name: 'West Bengal', x: 520, y: 380, width: 70, height: 100 },
  { name: 'Sikkim', x: 540, y: 320, width: 30, height: 30 },
  { name: 'Assam', x: 580, y: 340, width: 100, height: 60 },
  { name: 'Arunachal Pradesh', x: 620, y: 280, width: 100, height: 60 },
  { name: 'Nagaland', x: 690, y: 350, width: 50, height: 40 },
  { name: 'Manipur', x: 690, y: 400, width: 50, height: 40 },
  { name: 'Mizoram', x: 680, y: 450, width: 50, height: 50 },
  { name: 'Tripura', x: 630, y: 450, width: 40, height: 40 },
  { name: 'Meghalaya', x: 600, y: 410, width: 60, height: 40 },
  { name: 'Andaman and Nicobar Islands', x: 700, y: 700, width: 30, height: 80 },
  { name: 'Lakshadweep', x: 50, y: 750, width: 30, height: 40 },
  { name: 'Puducherry', x: 320, y: 800, width: 20, height: 20 },
  { name: 'Dadra and Nagar Haveli and Daman and Diu', x: 130, y: 450, width: 30, height: 30 },
];

export default function SimpleIndiaMap({ onStateHover, onStateLeave }: SimpleIndiaMapProps) {
  const [hoveredState, setHoveredState] = useState<string | null>(null);

  const handleMouseEnter = (stateName: string, event: React.MouseEvent<SVGRectElement>) => {
    console.log('SIMPLE MAP: Mouse enter', stateName);
    setHoveredState(stateName);
    if (onStateHover) {
      onStateHover(stateName, event.clientX, event.clientY);
    }
  };

  const handleMouseMove = (stateName: string, event: React.MouseEvent<SVGRectElement>) => {
    if (onStateHover) {
      onStateHover(stateName, event.clientX, event.clientY);
    }
  };

  const handleMouseLeave = () => {
    console.log('SIMPLE MAP: Mouse leave');
    setHoveredState(null);
    if (onStateLeave) {
      onStateLeave();
    }
  };

  return (
    <div className="w-full mx-auto" style={{ maxWidth: '800px' }}>
      <svg viewBox="0 0 800 900" className="w-full h-auto">
        {/* Background */}
        <rect x="0" y="0" width="800" height="900" fill="#1e3a8a" opacity="0.1" />
        
        {/* States */}
        {STATES.map((state) => (
          <rect
            key={state.name}
            x={state.x}
            y={state.y}
            width={state.width}
            height={state.height}
            fill={hoveredState === state.name ? '#f59e0b' : '#3b82f6'}
            stroke="#1e40af"
            strokeWidth="2"
            onMouseEnter={(e) => handleMouseEnter(state.name, e)}
            onMouseMove={(e) => handleMouseMove(state.name, e)}
            onMouseLeave={handleMouseLeave}
            style={{
              cursor: 'pointer',
              transition: 'fill 0.2s ease',
            }}
          />
        ))}
        
        {/* State Labels */}
        {STATES.map((state) => (
          <text
            key={`label-${state.name}`}
            x={state.x + state.width / 2}
            y={state.y + state.height / 2}
            textAnchor="middle"
            dominantBaseline="middle"
            fill="white"
            fontSize="10"
            pointerEvents="none"
            style={{ userSelect: 'none' }}
          >
            {state.name.length > 15 ? state.name.substring(0, 12) + '...' : state.name}
          </text>
        ))}
      </svg>
    </div>
  );
}
