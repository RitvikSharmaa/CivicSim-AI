export default function Loading() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-900 via-blue-800 to-indigo-900">
      <div className="text-center">
        {/* Logo Animation */}
        <div className="relative w-32 h-32 mx-auto mb-8">
          <div className="absolute inset-0 border-8 border-orange-200 rounded-full"></div>
          <div className="absolute inset-0 border-8 border-orange-500 rounded-full border-t-transparent animate-spin"></div>
          <div className="absolute inset-4 border-8 border-white rounded-full opacity-50"></div>
          <div className="absolute inset-4 border-8 border-white rounded-full border-t-transparent animate-spin" style={{animationDuration: '1.5s'}}></div>
          <div className="absolute inset-8 border-8 border-green-200 rounded-full"></div>
          <div className="absolute inset-8 border-8 border-green-500 rounded-full border-t-transparent animate-spin" style={{animationDuration: '2s'}}></div>
        </div>

        {/* Loading Text */}
        <h2 className="text-3xl font-bold text-white mb-4">
          Loading CivicSim AI
        </h2>
        <p className="text-gray-300 mb-8">
          Initializing AI agents and loading real Indian data...
        </p>

        {/* Progress Dots */}
        <div className="flex items-center justify-center space-x-2">
          <div className="w-3 h-3 bg-orange-500 rounded-full animate-bounce"></div>
          <div className="w-3 h-3 bg-white rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
          <div className="w-3 h-3 bg-green-500 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
        </div>
      </div>
    </div>
  );
}
