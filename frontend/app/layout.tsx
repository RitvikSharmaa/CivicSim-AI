import './globals.css'
import 'leaflet/dist/leaflet.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'CivicSim AI - AI Policy Sandbox | Government of India',
  description: 'AI-powered policy simulation system for Indian Government. Predict policy impacts with 99.86% accuracy using real data and advanced ML.',
  keywords: 'AI, Policy Simulation, Government of India, Machine Learning, Policy Analysis, Indian Cities',
  authors: [{ name: 'Government of India' }],
  icons: {
    icon: '/favicon.svg',
    apple: '/logo.svg',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
        <link rel="apple-touch-icon" href="/logo.svg" />
      </head>
      <body className="bg-gray-50">{children}</body>
    </html>
  )
}
