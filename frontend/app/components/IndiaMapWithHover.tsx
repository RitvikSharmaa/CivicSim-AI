'use client';

import { useState, useEffect, useRef } from 'react';
import dynamic from 'next/dynamic';

// Dynamically import to avoid SSR issues
const IndiaMap = dynamic(() => import('react-svgmap-india'), { ssr: false });

interface IndiaMapWithHoverProps {
  onStateHover?: (stateName: string, x: number, y: number) => void;
  onStateLeave?: () => void;
}

// State ID to full name mapping from react-svgmap-india
const STATE_MAP: { [key: string]: string } = {
  'AN': 'Andaman and Nicobar Islands',
  'AP': 'Andhra Pradesh',
  'AR': 'Arunachal Pradesh',
  'AS': 'Assam',
  'BR': 'Bihar',
  'CH': 'Chandigarh',
  'CT': 'Chhattisgarh',
  'DD': 'Dadra and Nagar Haveli and Daman and Diu',
  'DL': 'Delhi',
  'DN': 'Daman and Diu',
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
};

export default function IndiaMapWithHover({ onStateHover, onStateLeave }: IndiaMapWithHoverProps) {
  const [mounted, setMounted] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const listenersAttached = useRef(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  useEffect(() => {
    if (!mounted || !containerRef.current || listenersAttached.current) return;

    const attachListeners = () => {
      const container = containerRef.current;
      if (!container) return;

      // Find SVG within container
      const svg = container.querySelector('svg');
      if (!svg) return;

      const paths = svg.querySelectorAll('path');
      if (paths.length === 0) return;

      // Attach listeners
      paths.forEach(path => {
        path.addEventListener('mouseenter', (e: Event) => {
          const mouseEvent = e as MouseEvent;
          const target = mouseEvent.target as SVGPathElement;
          const stateCode = target.id;
          const stateName = STATE_MAP[stateCode];
          
          if (stateName && onStateHover) {
            onStateHover(stateName, mouseEvent.clientX, mouseEvent.clientY);
          }
        });

        path.addEventListener('mousemove', (e: Event) => {
          const mouseEvent = e as MouseEvent;
          const target = mouseEvent.target as SVGPathElement;
          const stateCode = target.id;
          const stateName = STATE_MAP[stateCode];
          
          if (stateName && onStateHover) {
            onStateHover(stateName, mouseEvent.clientX, mouseEvent.clientY);
          }
        });

        path.addEventListener('mouseleave', () => {
          if (onStateLeave) {
            onStateLeave();
          }
        });
      });

      listenersAttached.current = true;
    };

    // Try multiple times with increasing delays
    const timers = [100, 300, 500, 1000].map(delay => 
      setTimeout(attachListeners, delay)
    );

    return () => {
      timers.forEach(timer => clearTimeout(timer));
    };
  }, [mounted, onStateHover, onStateLeave]);

  if (!mounted) {
    return (
      <div className="flex items-center justify-center h-[500px]">
        <div className="text-white">Loading map...</div>
      </div>
    );
  }

  return (
    <div ref={containerRef} className="india-map-wrapper">
      <IndiaMap
        onClick={(stateCode: string) => {
          const stateName = STATE_MAP[stateCode];
          if (stateName) {
            console.log('Clicked state:', stateName);
          }
        }}
        size="500px"
        mapColor="#3b82f6"
        strokeColor="#1e40af"
        strokeWidth="1.5"
        hoverColor="#f59e0b"
      />
    </div>
  );
}
