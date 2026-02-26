'use client';

import { useState } from 'react';

interface IndiaMapProps {
  onStateHover?: (stateName: string, event: React.MouseEvent) => void;
  onStateLeave?: () => void;
  onStateClick?: (stateName: string) => void;
}

export default function IndiaMapSVG({ onStateHover, onStateLeave, onStateClick }: IndiaMapProps) {
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

  const getStateColor = (stateName: string) => {
    if (hoveredState === stateName) {
      return '#f59e0b'; // Orange on hover
    }
    return '#3b82f6'; // Blue default
  };

  // Simplified but recognizable India map shape
  return (
    <svg
      viewBox="0 0 400 600"
      xmlns="http://www.w3.org/2000/svg"
      style={{ width: '100%', height: '100%', maxWidth: '500px', margin: '0 auto' }}
    >
      {/* Simplified India Map - Major States */}
      
      {/* Jammu & Kashmir */}
      <path
        d="M 200 50 L 250 40 L 280 60 L 270 90 L 240 100 L 210 80 Z"
        fill={getStateColor('Jammu and Kashmir')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Jammu and Kashmir', e)}
        onMouseMove={(e) => onStateHover?.('Jammu and Kashmir', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Jammu and Kashmir')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Ladakh */}
      <path
        d="M 280 60 L 320 50 L 340 70 L 320 90 L 280 85 Z"
        fill={getStateColor('Ladakh')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Ladakh', e)}
        onMouseMove={(e) => onStateHover?.('Ladakh', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Ladakh')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Himachal Pradesh */}
      <path
        d="M 240 100 L 270 90 L 290 110 L 270 130 L 240 125 Z"
        fill={getStateColor('Himachal Pradesh')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Himachal Pradesh', e)}
        onMouseMove={(e) => onStateHover?.('Himachal Pradesh', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Himachal Pradesh')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Punjab */}
      <path
        d="M 210 120 L 240 125 L 250 145 L 220 150 Z"
        fill={getStateColor('Punjab')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Punjab', e)}
        onMouseMove={(e) => onStateHover?.('Punjab', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Punjab')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Haryana & Delhi */}
      <path
        d="M 220 150 L 250 145 L 270 165 L 250 180 L 220 175 Z"
        fill={getStateColor('Haryana')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Haryana', e)}
        onMouseMove={(e) => onStateHover?.('Haryana', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Haryana')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Delhi (small circle) */}
      <circle
        cx="240"
        cy="165"
        r="8"
        fill={getStateColor('Delhi')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Delhi', e)}
        onMouseMove={(e) => onStateHover?.('Delhi', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Delhi')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Uttarakhand */}
      <path
        d="M 270 130 L 310 125 L 320 150 L 290 160 L 270 145 Z"
        fill={getStateColor('Uttarakhand')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Uttarakhand', e)}
        onMouseMove={(e) => onStateHover?.('Uttarakhand', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Uttarakhand')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Rajasthan */}
      <path
        d="M 150 180 L 220 175 L 250 220 L 200 260 L 140 240 Z"
        fill={getStateColor('Rajasthan')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Rajasthan', e)}
        onMouseMove={(e) => onStateHover?.('Rajasthan', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Rajasthan')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Uttar Pradesh */}
      <path
        d="M 250 180 L 320 175 L 380 200 L 370 240 L 300 250 L 250 220 Z"
        fill={getStateColor('Uttar Pradesh')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Uttar Pradesh', e)}
        onMouseMove={(e) => onStateHover?.('Uttar Pradesh', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Uttar Pradesh')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Gujarat */}
      <path
        d="M 100 260 L 140 240 L 180 280 L 160 340 L 100 320 Z"
        fill={getStateColor('Gujarat')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Gujarat', e)}
        onMouseMove={(e) => onStateHover?.('Gujarat', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Gujarat')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Madhya Pradesh */}
      <path
        d="M 200 260 L 300 250 L 350 290 L 320 350 L 240 360 L 180 320 Z"
        fill={getStateColor('Madhya Pradesh')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Madhya Pradesh', e)}
        onMouseMove={(e) => onStateHover?.('Madhya Pradesh', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Madhya Pradesh')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Maharashtra */}
      <path
        d="M 160 360 L 240 360 L 280 420 L 220 480 L 140 450 Z"
        fill={getStateColor('Maharashtra')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Maharashtra', e)}
        onMouseMove={(e) => onStateHover?.('Maharashtra', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Maharashtra')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Karnataka */}
      <path
        d="M 220 480 L 280 470 L 300 540 L 250 580 L 200 560 Z"
        fill={getStateColor('Karnataka')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Karnataka', e)}
        onMouseMove={(e) => onStateHover?.('Karnataka', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Karnataka')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Kerala */}
      <path
        d="M 200 560 L 250 580 L 240 650 L 190 640 Z"
        fill={getStateColor('Kerala')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Kerala', e)}
        onMouseMove={(e) => onStateHover?.('Kerala', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Kerala')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Tamil Nadu */}
      <path
        d="M 250 580 L 320 570 L 340 640 L 290 680 L 240 650 Z"
        fill={getStateColor('Tamil Nadu')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Tamil Nadu', e)}
        onMouseMove={(e) => onStateHover?.('Tamil Nadu', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Tamil Nadu')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Andhra Pradesh */}
      <path
        d="M 280 420 L 350 410 L 370 480 L 320 520 L 280 470 Z"
        fill={getStateColor('Andhra Pradesh')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Andhra Pradesh', e)}
        onMouseMove={(e) => onStateHover?.('Andhra Pradesh', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Andhra Pradesh')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Telangana */}
      <path
        d="M 320 380 L 360 370 L 370 420 L 340 440 L 310 420 Z"
        fill={getStateColor('Telangana')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Telangana', e)}
        onMouseMove={(e) => onStateHover?.('Telangana', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Telangana')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Odisha */}
      <path
        d="M 370 290 L 430 280 L 450 340 L 420 380 L 360 370 Z"
        fill={getStateColor('Odisha')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Odisha', e)}
        onMouseMove={(e) => onStateHover?.('Odisha', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Odisha')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Chhattisgarh */}
      <path
        d="M 320 280 L 370 270 L 390 320 L 360 350 L 320 340 Z"
        fill={getStateColor('Chhattisgarh')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Chhattisgarh', e)}
        onMouseMove={(e) => onStateHover?.('Chhattisgarh', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Chhattisgarh')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* West Bengal */}
      <path
        d="M 450 240 L 500 230 L 520 280 L 490 320 L 450 310 Z"
        fill={getStateColor('West Bengal')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('West Bengal', e)}
        onMouseMove={(e) => onStateHover?.('West Bengal', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('West Bengal')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Bihar */}
      <path
        d="M 370 200 L 430 190 L 450 230 L 420 250 L 370 240 Z"
        fill={getStateColor('Bihar')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Bihar', e)}
        onMouseMove={(e) => onStateHover?.('Bihar', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Bihar')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Jharkhand */}
      <path
        d="M 390 250 L 440 245 L 450 280 L 420 300 L 390 290 Z"
        fill={getStateColor('Jharkhand')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Jharkhand', e)}
        onMouseMove={(e) => onStateHover?.('Jharkhand', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Jharkhand')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Assam */}
      <path
        d="M 520 200 L 580 190 L 600 220 L 570 250 L 520 240 Z"
        fill={getStateColor('Assam')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Assam', e)}
        onMouseMove={(e) => onStateHover?.('Assam', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Assam')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Northeast States (simplified as one region) */}
      <path
        d="M 600 180 L 650 170 L 670 220 L 640 260 L 600 250 Z"
        fill={getStateColor('Arunachal Pradesh')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Arunachal Pradesh', e)}
        onMouseMove={(e) => onStateHover?.('Arunachal Pradesh', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Arunachal Pradesh')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
      
      {/* Goa (small) */}
      <path
        d="M 140 450 L 160 445 L 165 465 L 145 470 Z"
        fill={getStateColor('Goa')}
        stroke="#1e40af"
        strokeWidth="2"
        onMouseEnter={(e) => handleMouseEnter('Goa', e)}
        onMouseMove={(e) => onStateHover?.('Goa', e)}
        onMouseLeave={handleMouseLeave}
        onClick={() => handleClick('Goa')}
        style={{ cursor: 'pointer', transition: 'fill 0.2s' }}
      />
    </svg>
  );
}
