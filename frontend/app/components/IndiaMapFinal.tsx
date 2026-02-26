'use client';

import { useState } from 'react';
// @ts-ignore
import India from '@svg-maps/india';

interface IndiaMapFinalProps {
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

export default function IndiaMapFinal({ onStateHover, onStateLeave, onStateClick }: IndiaMapFinalProps) {
  const [hoveredState, setHoveredState] = useState<string | null>(null);

  const handleStateHover = (event: React.MouseEvent<SVGPathElement>, locationId: string) => {
    const stateName = STATE_NAMES[locationId];
    console.log('=== HOVER EVENT ===');
    console.log('Location ID:', locationId);
    console.log('State Name:', stateName);
    console.log('Mouse X:', event.clientX, 'Y:', event.clientY);
    
    if (stateName && onStateHover) {
      setHoveredState(locationId);
      onStateHover(stateName, event);
    }
  };

  const handleStateLeave = () => {
    console.log('State leave');
    setHoveredState(null);
    if (onStateLeave) {
      onStateLeave();
    }
  };

  return (
    <div className="w-full mx-auto" style={{ maxWidth: '600px', maxHeight: '700px' }}>
      <svg
        viewBox={India.viewBox}
        xmlns="http://www.w3.org/2000/svg"
        className="w-full h-auto"
      >
        {India.locations.map((location: any) => (
          <path
            key={location.id}
            id={location.id}
            name={location.name}
            d={location.path}
            fill={hoveredState === location.id ? '#f59e0b' : '#3b82f6'}
            stroke="#1e40af"
            strokeWidth="1.5"
            onMouseEnter={(e) => handleStateHover(e, location.id)}
            onMouseMove={(e) => handleStateHover(e, location.id)}
            onMouseLeave={handleStateLeave}
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
