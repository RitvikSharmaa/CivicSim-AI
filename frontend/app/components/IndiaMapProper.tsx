'use client';

import { useState } from 'react';
// @ts-ignore
import India from '@svg-maps/india';

interface IndiaMapProperProps {
  onStateHover?: (stateName: string, event: React.MouseEvent) => void;
  onStateLeave?: () => void;
  onStateClick?: (stateName: string) => void;
}

// State code to full name mapping
const STATE_NAMES: Record<string, string> = {
  'INAN': 'Andaman and Nicobar Islands',
  'INAP': 'Andhra Pradesh',
  'INAR': 'Arunachal Pradesh',
  'INAS': 'Assam',
  'INBR': 'Bihar',
  'INCH': 'Chandigarh',
  'INCT': 'Chhattisgarh',
  'INDH': 'Dadra and Nagar Haveli and Daman and Diu',
  'INDL': 'Delhi',
  'INGA': 'Goa',
  'INGJ': 'Gujarat',
  'INHP': 'Himachal Pradesh',
  'INHR': 'Haryana',
  'INJH': 'Jharkhand',
  'INJK': 'Jammu and Kashmir',
  'INKA': 'Karnataka',
  'INKL': 'Kerala',
  'INLA': 'Ladakh',
  'INLD': 'Lakshadweep',
  'INMH': 'Maharashtra',
  'INML': 'Meghalaya',
  'INMN': 'Manipur',
  'INMP': 'Madhya Pradesh',
  'INMZ': 'Mizoram',
  'INNL': 'Nagaland',
  'INOR': 'Odisha',
  'INPB': 'Punjab',
  'INPY': 'Puducherry',
  'INRJ': 'Rajasthan',
  'INSK': 'Sikkim',
  'INTG': 'Telangana',
  'INTN': 'Tamil Nadu',
  'INTR': 'Tripura',
  'INUP': 'Uttar Pradesh',
  'INUT': 'Uttarakhand',
  'INWB': 'West Bengal'
};

export default function IndiaMapProper({ onStateHover, onStateLeave, onStateClick }: IndiaMapProperProps) {
  const [hoveredLocation, setHoveredLocation] = useState<string | null>(null);

  console.log('India map data:', India);
  console.log('Number of locations:', India.locations?.length);

  const handleLocationMouseEnter = (event: React.MouseEvent<SVGPathElement>, locationId: string) => {
    const stateName = STATE_NAMES[locationId];
    console.log('Mouse enter:', locationId, stateName);
    if (stateName) {
      setHoveredLocation(locationId);
      onStateHover?.(stateName, event);
    }
  };

  const handleLocationMouseMove = (event: React.MouseEvent<SVGPathElement>, locationId: string) => {
    const stateName = STATE_NAMES[locationId];
    if (stateName) {
      onStateHover?.(stateName, event);
    }
  };

  const handleLocationMouseLeave = () => {
    setHoveredLocation(null);
    onStateLeave?.();
  };

  const handleLocationClick = (locationId: string) => {
    const stateName = STATE_NAMES[locationId];
    if (stateName) {
      onStateClick?.(stateName);
    }
  };

  return (
    <div className="w-full max-w-3xl mx-auto bg-white bg-opacity-5 rounded-lg p-4">
      <svg
        viewBox={India.viewBox}
        xmlns="http://www.w3.org/2000/svg"
        className="w-full h-auto"
        style={{ maxHeight: '600px', background: 'rgba(255,255,255,0.05)' }}
      >
        {India.locations.map((location: any) => (
          <path
            key={location.id}
            id={location.id}
            name={location.name}
            d={location.path}
            fill={hoveredLocation === location.id ? '#f59e0b' : '#3b82f6'}
            stroke="#1e40af"
            strokeWidth="1.5"
            onMouseEnter={(e) => handleLocationMouseEnter(e, location.id)}
            onMouseMove={(e) => handleLocationMouseMove(e, location.id)}
            onMouseLeave={handleLocationMouseLeave}
            onClick={() => handleLocationClick(location.id)}
            style={{
              cursor: 'pointer',
              transition: 'fill 0.2s ease',
            }}
          />
        ))}
      </svg>
    </div>
  );
}
