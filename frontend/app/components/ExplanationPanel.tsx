interface ExplanationPanelProps {
  explanation: any
}

export default function ExplanationPanel({ explanation }: ExplanationPanelProps) {
  if (!explanation) return null

  const { shap_values, feature_importance, narrative_summary, recommendations } = explanation

  // Parse the comprehensive report sections
  const parseReport = (text: string) => {
    if (!text) return []
    
    const sections: any[] = []
    const lines = text.split('\n')
    let currentSection: any = null
    
    for (const line of lines) {
      // Section headers (with emoji or special markers)
      if (line.match(/^[📋🏛️🚦💰👥📊🔧🎯⚠️💡📚]/)) {
        if (currentSection) sections.push(currentSection)
        currentSection = {
          title: line.trim(),
          content: []
        }
      } else if (line.match(/^={3,}/)) {
        // Separator line - skip
        continue
      } else if (line.trim() && currentSection) {
        currentSection.content.push(line.trim())
      }
    }
    
    if (currentSection) sections.push(currentSection)
    return sections
  }

  const sections = parseReport(narrative_summary)

  return (
    <div className="bg-white rounded-lg shadow-lg">
      <div className="bg-gradient-to-r from-blue-900 to-indigo-900 text-white p-6 rounded-t-lg">
        <h3 className="text-2xl font-bold">Comprehensive Policy Analysis</h3>
        <p className="text-blue-200 text-sm mt-1">AI-Powered Impact Assessment & Recommendations</p>
      </div>
      
      <div className="p-6 space-y-6">
        {/* Render parsed sections */}
        {sections.map((section, idx) => (
          <div key={idx} className="border-l-4 border-blue-500 pl-4 py-2">
            <h4 className="text-lg font-bold text-gray-900 mb-3">{section.title}</h4>
            <div className="space-y-2">
              {section.content.map((line: string, lineIdx: number) => {
                // Check if it's a bullet point
                if (line.startsWith('•') || line.startsWith('-')) {
                  return (
                    <div key={lineIdx} className="flex items-start ml-4">
                      <span className="text-blue-600 mr-2">•</span>
                      <p className="text-sm text-gray-700 flex-1">{line.replace(/^[•\-]\s*/, '')}</p>
                    </div>
                  )
                }
                // Check if it's a key-value pair (contains :)
                else if (line.includes(':') && line.split(':')[0].length < 50) {
                  const [key, ...valueParts] = line.split(':')
                  const value = valueParts.join(':').trim()
                  return (
                    <div key={lineIdx} className="flex items-start">
                      <span className="text-sm font-semibold text-gray-800 min-w-[150px]">{key}:</span>
                      <span className="text-sm text-gray-700 flex-1">{value}</span>
                    </div>
                  )
                }
                // Regular paragraph
                else if (line.trim()) {
                  return (
                    <p key={lineIdx} className="text-sm text-gray-700 leading-relaxed">
                      {line}
                    </p>
                  )
                }
                return null
              })}
            </div>
          </div>
        ))}

        {/* Feature Importance */}
        {feature_importance && Object.keys(feature_importance).length > 0 && (
          <div className="border-l-4 border-orange-500 pl-4 py-2">
            <h4 className="text-lg font-bold text-gray-900 mb-3">🎯 Key Impact Drivers</h4>
            <div className="space-y-2">
              {Object.entries(feature_importance).slice(0, 5).map(([feature, importance]: [string, any]) => (
                <div key={feature} className="flex items-center">
                  <span className="text-sm text-gray-700 w-48 font-medium">
                    {feature.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
                  </span>
                  <div className="flex-1 bg-gray-200 rounded-full h-3">
                    <div
                      className="bg-gradient-to-r from-blue-500 to-blue-600 h-3 rounded-full transition-all duration-500"
                      style={{ width: `${importance * 100}%` }}
                    />
                  </div>
                  <span className="text-sm text-gray-700 ml-3 w-12 text-right font-semibold">
                    {(importance * 100).toFixed(0)}%
                  </span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Recommendations */}
        {recommendations && Array.isArray(recommendations) && recommendations.length > 0 && (
          <div className="border-l-4 border-green-500 pl-4 py-2">
            <h4 className="text-lg font-bold text-gray-900 mb-3">💡 Strategic Recommendations</h4>
            <div className="space-y-4">
              {recommendations.map((rec: any, idx: number) => (
                <div key={idx} className="bg-gray-50 rounded-lg p-4">
                  {typeof rec === 'string' ? (
                    <p className="text-sm text-gray-700">{rec}</p>
                  ) : typeof rec === 'object' && rec !== null ? (
                    <>
                      <div className="flex items-center gap-2 mb-2">
                        {rec.priority && (
                          <span className={`text-xs px-2 py-1 rounded font-semibold ${
                            rec.priority === 'High' ? 'bg-red-100 text-red-700' :
                            rec.priority === 'Medium' ? 'bg-yellow-100 text-yellow-700' :
                            'bg-green-100 text-green-700'
                          }`}>
                            {rec.priority} Priority
                          </span>
                        )}
                        {rec.category && (
                          <span className="text-xs px-2 py-1 rounded bg-blue-100 text-blue-700 font-semibold">
                            {rec.category}
                          </span>
                        )}
                      </div>
                      <p className="text-base font-semibold text-gray-900 mb-2">
                        {rec.recommendation || rec.title || `Recommendation ${idx + 1}`}
                      </p>
                      {rec.rationale && (
                        <p className="text-sm text-gray-600 mb-2 italic">
                          {rec.rationale}
                        </p>
                      )}
                      {rec.action_items && Array.isArray(rec.action_items) && rec.action_items.length > 0 && (
                        <div className="mt-2">
                          <p className="text-xs font-semibold text-gray-700 mb-1">Action Items:</p>
                          <ul className="text-sm text-gray-600 ml-4 space-y-1">
                            {rec.action_items.map((item: string, i: number) => (
                              <li key={i} className="flex items-start">
                                <span className="text-blue-600 mr-2">→</span>
                                <span>{item}</span>
                              </li>
                            ))}
                          </ul>
                        </div>
                      )}
                    </>
                  ) : null}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
