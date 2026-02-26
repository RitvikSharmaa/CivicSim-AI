'use client'

import { useEffect, useRef, useState } from 'react'
import dynamic from 'next/dynamic'

// Dynamically import to avoid SSR issues
const MapContainer = dynamic(
  () => import('react-leaflet').then((mod) => mod.MapContainer),
  { ssr: false }
)
const TileLayer = dynamic(
  () => import('react-leaflet').then((mod) => mod.TileLayer),
  { ssr: false }
)
const Marker = dynamic(
  () => import('react-leaflet').then((mod) => mod.Marker),
  { ssr: false }
)
const Popup = dynamic(
  () => import('react-leaflet').then((mod) => mod.Popup),
  { ssr: false }
)
const Circle = dynamic(
  () => import('react-leaflet').then((mod) => mod.Circle),
  { ssr: false }
)

interface MapProps {
  city: string
  state: string
  simulationData?: any
}

// Indian city coordinates
const CITY_COORDS: Record<string, [number, number]> = {
  'Bengaluru': [12.9716, 77.5946],
  'Mumbai': [19.0760, 72.8777],
  'New Delhi': [28.6139, 77.2090],
  'Pune': [18.5204, 73.8567],
  'Chennai': [13.0827, 80.2707],
  'Kolkata': [22.5726, 88.3639]
}

export default function IndiaInteractiveMap({ city, state, simulationData }: MapProps) {
  const [isClient, setIsClient] = useState(false)
  const mapRef = useRef<any>(null)

  useEffect(() => {
    setIsClient(true)
  }, [])

  if (!isClient) {
    return (
      <div className="w-full h-96 bg-gray-100 rounded-lg flex items-center justify-center">
        <p className="text-gray-500">Loading map...</p>
      </div>
    )
  }

  const center = CITY_COORDS[city] || [20.5937, 78.9629] // India center as fallback
  const congestionLevel = simulationData?.traffic?.congestion_level || 50

  // Calculate impact zones based on simulation
  const impactRadius = simulationData ? 5000 : 3000 // meters
  const congestionColor = congestionLevel > 70 ? '#ef4444' : 
                         congestionLevel > 50 ? '#f59e0b' : '#10b981'

  return (
    <div className="w-full h-96 rounded-lg overflow-hidden shadow-lg">
      <MapContainer
        center={center}
        zoom={12}
        style={{ height: '100%', width: '100%' }}
        ref={mapRef}
      >
        {/* FREE OpenStreetMap tiles */}
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {/* City center marker */}
        <Marker position={center}>
          <Popup>
            <div className="text-sm">
              <h3 className="font-bold">{city}, {state}</h3>
              {simulationData && (
                <>
                  <p>Population: {simulationData.demographics?.population?.toLocaleString('en-IN')}</p>
                  <p>Congestion: {congestionLevel}%</p>
                  <p>Vehicles: {simulationData.demographics?.vehicles?.toLocaleString('en-IN')}</p>
                </>
              )}
            </div>
          </Popup>
        </Marker>

        {/* Congestion impact zone */}
        {simulationData && (
          <Circle
            center={center}
            radius={impactRadius}
            pathOptions={{
              color: congestionColor,
              fillColor: congestionColor,
              fillOpacity: 0.2
            }}
          >
            <Popup>
              <div className="text-sm">
                <h4 className="font-bold">Policy Impact Zone</h4>
                <p>Congestion: {congestionLevel}%</p>
                <p>Radius: {(impactRadius / 1000).toFixed(1)} km</p>
              </div>
            </Popup>
          </Circle>
        )}

        {/* Additional impact zones for simulation results */}
        {simulationData?.real_india_impact && (
          <>
            {/* High impact zone */}
            <Circle
              center={[center[0] + 0.02, center[1] + 0.02]}
              radius={2000}
              pathOptions={{
                color: '#10b981',
                fillColor: '#10b981',
                fillOpacity: 0.3
              }}
            >
              <Popup>
                <div className="text-sm">
                  <h4 className="font-bold">High Impact Zone</h4>
                  <p>Congestion Reduction: {simulationData.real_india_impact.congestion_reduction_percent}%</p>
                  <p>Time Saved: {simulationData.real_india_impact.estimated_time_saved_minutes} min</p>
                </div>
              </Popup>
            </Circle>

            {/* Medium impact zone */}
            <Circle
              center={[center[0] - 0.02, center[1] - 0.02]}
              radius={2000}
              pathOptions={{
                color: '#f59e0b',
                fillColor: '#f59e0b',
                fillOpacity: 0.3
              }}
            >
              <Popup>
                <div className="text-sm">
                  <h4 className="font-bold">Medium Impact Zone</h4>
                  <p>Affected Population: {simulationData.real_india_impact.affected_population?.toLocaleString('en-IN')}</p>
                </div>
              </Popup>
            </Circle>
          </>
        )}
      </MapContainer>

      {/* Map legend */}
      <div className="absolute bottom-4 right-4 bg-white p-3 rounded-lg shadow-lg text-xs z-[1000]">
        <h4 className="font-bold mb-2">Legend</h4>
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded-full bg-red-500"></div>
            <span>High Congestion (&gt;70%)</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded-full bg-yellow-500"></div>
            <span>Medium Congestion (50-70%)</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded-full bg-green-500"></div>
            <span>Low Congestion (&lt;50%)</span>
          </div>
        </div>
        <p className="mt-2 text-gray-500">FREE OpenStreetMap</p>
      </div>
    </div>
  )
}
