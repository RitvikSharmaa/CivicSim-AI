'use client';

import Image from 'next/image';
import { useState } from 'react';

interface HeaderProps {
  onNavigate?: (view: 'home' | 'simulator' | 'documentation') => void;
  currentView?: 'home' | 'simulator' | 'documentation';
}

export default function Header({ onNavigate, currentView = 'home' }: HeaderProps) {
  const [showMenu, setShowMenu] = useState(false);

  const handleNavClick = (view: 'home' | 'simulator' | 'documentation') => {
    if (onNavigate) {
      onNavigate(view);
    }
    setShowMenu(false);
  };

  return (
    <header className="bg-gradient-to-r from-blue-900 via-blue-800 to-blue-900 text-white shadow-2xl sticky top-0 z-50 border-b-4 border-orange-500">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          {/* Logo and Title */}
          <button 
            onClick={() => handleNavClick('home')}
            className="flex items-center space-x-4 hover:opacity-80 transition-opacity"
          >
            <div className="relative w-12 h-12 bg-white rounded-full p-1 shadow-lg">
              <svg viewBox="0 0 200 200" className="w-full h-full">
                <circle cx="100" cy="100" r="95" fill="#FF9933" opacity="0.1"/>
                <path d="M100 20 L160 50 L160 120 Q160 150 100 180 Q40 150 40 120 L40 50 Z" fill="url(#gradient1)" stroke="#138808" strokeWidth="3"/>
                <path d="M100 35 L150 60 L150 115 Q150 140 100 165 Q50 140 50 115 L50 60 Z" fill="white" opacity="0.9"/>
                <circle cx="100" cy="90" r="25" fill="none" stroke="#000080" strokeWidth="2"/>
                <circle cx="100" cy="90" r="20" fill="none" stroke="#FF9933" strokeWidth="1.5"/>
                <circle cx="100" cy="90" r="15" fill="none" stroke="#138808" strokeWidth="1.5"/>
                <circle cx="100" cy="90" r="5" fill="#000080"/>
                <circle cx="85" cy="75" r="3" fill="#FF9933"/>
                <circle cx="115" cy="75" r="3" fill="#FF9933"/>
                <circle cx="85" cy="105" r="3" fill="#138808"/>
                <circle cx="115" cy="105" r="3" fill="#138808"/>
                <line x1="100" y1="90" x2="85" y2="75" stroke="#000080" strokeWidth="1.5"/>
                <line x1="100" y1="90" x2="115" y2="75" stroke="#000080" strokeWidth="1.5"/>
                <line x1="100" y1="90" x2="85" y2="105" stroke="#000080" strokeWidth="1.5"/>
                <line x1="100" y1="90" x2="115" y2="105" stroke="#000080" strokeWidth="1.5"/>
                <defs>
                  <linearGradient id="gradient1" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" style={{stopColor:'#FF9933', stopOpacity:0.3}} />
                    <stop offset="50%" style={{stopColor:'#FFFFFF', stopOpacity:0.3}} />
                    <stop offset="100%" style={{stopColor:'#138808', stopOpacity:0.3}} />
                  </linearGradient>
                </defs>
              </svg>
            </div>
            <div className="text-left">
              <h1 className="text-2xl font-bold tracking-tight">
                CivicSim AI
              </h1>
              <p className="text-xs text-orange-300 font-medium">
                Government of India • AI Policy Sandbox
              </p>
            </div>
          </button>

          {/* Navigation */}
          <nav className="hidden md:flex items-center space-x-6">
            <button 
              onClick={() => handleNavClick('home')}
              className={`hover:text-orange-300 transition-colors font-medium ${
                currentView === 'home' ? 'text-orange-300 border-b-2 border-orange-300 pb-1' : ''
              }`}
            >
              Dashboard
            </button>
            <button 
              onClick={() => handleNavClick('simulator')}
              className={`hover:text-orange-300 transition-colors font-medium ${
                currentView === 'simulator' ? 'text-orange-300 border-b-2 border-orange-300 pb-1' : ''
              }`}
            >
              Simulate
            </button>
            <button 
              onClick={() => handleNavClick('documentation')}
              className={`hover:text-orange-300 transition-colors font-medium ${
                currentView === 'documentation' ? 'text-orange-300 border-b-2 border-orange-300 pb-1' : ''
              }`}
            >
              Documentation
            </button>
          </nav>

          {/* Status Badge */}
          <div className="hidden lg:flex items-center space-x-4">
            <div className="flex items-center space-x-2 bg-green-500 bg-opacity-20 px-4 py-2 rounded-full border border-green-400">
              <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
              <span className="text-sm font-medium text-green-300">System Active</span>
            </div>
            <div className="text-right">
              <div className="text-xs text-gray-300">Version</div>
              <div className="text-sm font-bold text-orange-300">2.0-Optimized</div>
            </div>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setShowMenu(!showMenu)}
            className="md:hidden p-2 rounded-lg hover:bg-blue-700 transition-colors"
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              {showMenu ? (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {showMenu && (
          <div className="md:hidden mt-4 pb-4 space-y-2 border-t border-blue-700 pt-4">
            <button 
              onClick={() => handleNavClick('home')}
              className={`block w-full text-left py-2 px-4 hover:bg-blue-700 rounded-lg transition-colors ${
                currentView === 'home' ? 'bg-blue-700' : ''
              }`}
            >
              Dashboard
            </button>
            <button 
              onClick={() => handleNavClick('simulator')}
              className={`block w-full text-left py-2 px-4 hover:bg-blue-700 rounded-lg transition-colors ${
                currentView === 'simulator' ? 'bg-blue-700' : ''
              }`}
            >
              Simulate
            </button>
            <button 
              onClick={() => handleNavClick('documentation')}
              className={`block w-full text-left py-2 px-4 hover:bg-blue-700 rounded-lg transition-colors ${
                currentView === 'documentation' ? 'bg-blue-700' : ''
              }`}
            >
              Documentation
            </button>
          </div>
        )}
      </div>

      {/* Indian Flag Stripe */}
      <div className="h-1 bg-gradient-to-r from-orange-500 via-white to-green-600"></div>
    </header>
  );
}
