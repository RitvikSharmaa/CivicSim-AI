'use client';

import dynamic from 'next/dynamic';
import { Suspense } from 'react';

// Lazy load the map component for better performance
const IndiaInteractiveMap = dynamic(
  () => import('./IndiaInteractiveMap'),
  {
    ssr: false, // Disable server-side rendering for Leaflet
    loading: () => (
      <div className="w-full h-96 bg-gray-100 rounded-lg flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading interactive map...</p>
        </div>
      </div>
    ),
  }
);

export default function LazyMap(props: any) {
  return (
    <Suspense fallback={
      <div className="w-full h-96 bg-gray-100 rounded-lg flex items-center justify-center">
        <p className="text-gray-600">Loading map...</p>
      </div>
    }>
      <IndiaInteractiveMap {...props} />
    </Suspense>
  );
}
