# 📚 Indian Policy Knowledge Base - Implementation Plan

## 🎯 Objective
Build a comprehensive policy knowledge base covering all 36 states/UTs with real government policy documents to enable AI agents to make accurate predictions and provide relevant policy recommendations.

---

## 📊 Data Sources Identified

### 1. Central Government Sources (FREE)

#### A. Official Government Portals
- **India.gov.in** - National Portal of India
- **NITI Aayog** - Policy think tank, state development plans
- **PM India** - Prime Minister's Office schemes
- **Ministry Websites** - Sector-specific policies

#### B. Policy Repositories
- **PRS India** (prsindia.org) - Legislative research
- **Invest India** - Investment policies and schemes
- **Data.gov.in** - Open government data

#### C. Sector-Specific Sources
- **Ministry of Education** - Education policies (NEP 2020)
- **Ministry of Health** - Health schemes (Ayushman Bharat)
- **Ministry of Finance** - Economic policies, budgets
- **Ministry of Transport** - Infrastructure policies
- **Ministry of Agriculture** - Agricultural schemes
- **Ministry of Urban Development** - Smart Cities Mission

### 2. State Government Sources (FREE)

#### Major States Identified:
- **Karnataka**: IT Policy 2025-2030, Space Policy 2025-2030
- **Maharashtra**: Infrastructure policies, PWD documents
- **Tamil Nadu**: State acts, ordinances, department policies
- **Delhi**: Urban development, transport policies
- **Gujarat**: Industrial policies, investment schemes
- **West Bengal**: Social welfare schemes
- **Uttar Pradesh**: Development plans
- **Rajasthan**: Tourism, heritage policies

---

## 🗂️ Policy Categories to Cover

### 1. Economic Policies
- **Taxation**: GST, State taxes, exemptions
- **Investment**: FDI policies, state incentives
- **Industry**: Manufacturing, IT, services
- **Trade**: Export-import policies
- **Budget**: Annual budgets, allocations

### 2. Social Welfare Policies
- **Education**: 
  - Right to Education Act
  - National Education Policy 2020
  - State education schemes
  - Scholarship programs
- **Health**:
  - Ayushman Bharat
  - State health insurance schemes
  - Hospital infrastructure
  - Medical education
- **Employment**:
  - MGNREGA
  - Skill development programs
  - Unemployment benefits

### 3. Infrastructure Policies
- **Transportation**:
  - Metro rail projects
  - Highway development
  - Public transport schemes
- **Urban Development**:
  - Smart Cities Mission
  - AMRUT (water supply)
  - Housing for All
- **Energy**:
  - Renewable energy targets
  - Power distribution
  - Solar schemes

### 4. Agricultural Policies
- **Subsidies**: Fertilizer, seeds, equipment
- **MSP**: Minimum Support Prices
- **Irrigation**: Water management
- **Crop Insurance**: PM Fasal Bima Yojana

### 5. Environmental Policies
- **Pollution Control**: Air, water quality
- **Climate Action**: State action plans
- **Forest Conservation**: Green cover targets
- **Waste Management**: Swachh Bharat

---

## 🏗️ Implementation Architecture

### Phase 1: Data Collection & Storage (Week 1-2)

#### 1.1 Create Policy Database Schema
```python
# MongoDB Collections Structure

policies_collection = {
    "policy_id": "unique_id",
    "policy_name": "Karnataka IT Policy 2025-2030",
    "state": "Karnataka",
    "category": "Economic/Technology",
    "sub_category": "Information Technology",
    "year": 2025,
    "valid_until": 2030,
    "description": "Full policy description",
    "objectives": ["obj1", "obj2"],
    "budget_allocation": 50000000000,  # in INR
    "target_beneficiaries": "IT companies, startups",
    "key_provisions": [
        {
            "provision": "Tax incentives",
            "details": "30% tax exemption for 5 years"
        }
    ],
    "implementation_timeline": "2025-2030",
    "monitoring_authority": "Department of IT",
    "related_policies": ["policy_id_1", "policy_id_2"],
    "source_url": "official_url",
    "document_text": "Full policy text",
    "last_updated": "2026-02-26",
    "tags": ["IT", "technology", "investment", "jobs"]
}

state_schemes_collection = {
    "scheme_id": "unique_id",
    "scheme_name": "Ayushman Bharat",
    "type": "Central/State/Centrally Sponsored",
    "applicable_states": ["All"],
    "sector": "Health",
    "launch_date": "2018-09-23",
    "budget": 60000000000,
    "beneficiaries_count": 500000000,
    "eligibility_criteria": "Below poverty line families",
    "benefits": "Health insurance up to ₹5 lakh",
    "application_process": "Online/Offline",
    "documents_required": ["Aadhaar", "Ration card"],
    "official_website": "pmjay.gov.in",
    "helpline": "14555"
}

policy_impacts_collection = {
    "impact_id": "unique_id",
    "policy_id": "ref_policy_id",
    "state": "Karnataka",
    "year": 2025,
    "economic_impact": {
        "gdp_contribution": 2.5,  # percentage
        "jobs_created": 900000,
        "investment_attracted": 300000000000  # INR
    },
    "social_impact": {
        "beneficiaries": 5000000,
        "literacy_improvement": 2.3,  # percentage
        "health_coverage": 80  # percentage
    },
    "infrastructure_impact": {
        "projects_completed": 150,
        "roads_built_km": 5000,
        "hospitals_built": 50
    }
}
```

#### 1.2 Web Scraping Scripts
```python
# backend/app/services/policy_scraper.py

import requests
from bs4 import BeautifulSoup
import asyncio
from typing import List, Dict

class PolicyScraper:
    """Scrape policy documents from official sources"""
    
    SOURCES = {
        "central": [
            "https://www.india.gov.in",
            "https://niti.gov.in",
            "https://prsindia.org"
        ],
        "states": {
            "Karnataka": "https://karnataka.gov.in",
            "Maharashtra": "https://maharashtra.gov.in",
            "Tamil Nadu": "https://tn.gov.in",
            # ... all 36 states
        }
    }
    
    async def scrape_central_policies(self):
        """Scrape central government policies"""
        pass
    
    async def scrape_state_policies(self, state: str):
        """Scrape state-specific policies"""
        pass
    
    async def extract_policy_text(self, url: str):
        """Extract policy text from PDF/HTML"""
        pass
```

### Phase 2: Policy Processing & Indexing (Week 3-4)

#### 2.1 Text Processing Pipeline
```python
# backend/app/services/policy_processor.py

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

class PolicyProcessor:
    """Process and index policy documents"""
    
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    
    def process_policy_document(self, policy_text: str):
        """Split and embed policy text"""
        chunks = self.text_splitter.split_text(policy_text)
        return chunks
    
    def create_vector_store(self, documents: List[str]):
        """Create FAISS vector store for semantic search"""
        vectorstore = FAISS.from_texts(
            documents,
            self.embeddings
        )
        return vectorstore
    
    def extract_key_information(self, policy_text: str):
        """Extract structured information using LLM"""
        # Use LangChain to extract:
        # - Objectives
        # - Budget
        # - Timeline
        # - Beneficiaries
        # - Key provisions
        pass
```

#### 2.2 Policy Search & Retrieval
```python
# backend/app/services/policy_search.py

class PolicySearchEngine:
    """Semantic search over policy documents"""
    
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore
    
    def search_relevant_policies(
        self,
        query: str,
        state: str = None,
        category: str = None,
        top_k: int = 5
    ):
        """Search for relevant policies"""
        results = self.vectorstore.similarity_search(
            query,
            k=top_k,
            filter={"state": state, "category": category}
        )
        return results
    
    def get_policy_by_sector(self, sector: str, state: str):
        """Get all policies for a sector in a state"""
        pass
```

### Phase 3: Agent Integration (Week 5-6)

#### 3.1 Enhanced Policy Agent
```python
# backend/app/agents/enhanced_policy_agent.py

from langchain.agents import AgentExecutor
from langchain.tools import Tool

class EnhancedPolicyAgent:
    """Policy agent with knowledge base access"""
    
    def __init__(self, policy_search_engine):
        self.search_engine = policy_search_engine
        self.tools = self._create_tools()
    
    def _create_tools(self):
        return [
            Tool(
                name="SearchPolicies",
                func=self.search_engine.search_relevant_policies,
                description="Search for relevant policies"
            ),
            Tool(
                name="GetPolicyDetails",
                func=self._get_policy_details,
                description="Get detailed policy information"
            ),
            Tool(
                name="ComparePolicies",
                func=self._compare_policies,
                description="Compare policies across states"
            )
        ]
    
    async def analyze_policy_impact(
        self,
        policy_description: str,
        state: str,
        city: str
    ):
        """Analyze policy with knowledge base context"""
        
        # 1. Search for similar existing policies
        similar_policies = self.search_engine.search_relevant_policies(
            query=policy_description,
            state=state,
            top_k=5
        )
        
        # 2. Get state-specific context
        state_policies = self.search_engine.get_policy_by_sector(
            sector=self._extract_sector(policy_description),
            state=state
        )
        
        # 3. Analyze with context
        analysis = await self._analyze_with_context(
            policy_description,
            similar_policies,
            state_policies
        )
        
        return analysis
```

---

## 📥 Data Collection Strategy

### Automated Collection (70%)
```python
# Scrape from official sources
sources = [
    "india.gov.in",
    "niti.gov.in",
    "prsindia.org",
    "state government websites"
]

# Use APIs where available
apis = [
    "data.gov.in API",
    "RBI API",
    "Census API"
]
```

### Manual Curation (30%)
- Download official PDF documents
- Extract text using OCR if needed
- Verify accuracy
- Add metadata

---

## 🗄️ Storage Structure

### File System
```
backend/
├── data/
│   ├── policies/
│   │   ├── central/
│   │   │   ├── education/
│   │   │   ├── health/
│   │   │   ├── infrastructure/
│   │   │   └── ...
│   │   └── states/
│   │       ├── Karnataka/
│   │       │   ├── IT_Policy_2025.json
│   │       │   ├── Space_Policy_2025.json
│   │       │   └── ...
│   │       ├── Maharashtra/
│   │       └── ...
│   ├── schemes/
│   │   ├── central_schemes.json
│   │   └── state_schemes.json
│   └── embeddings/
│       └── policy_vectors.faiss
```

### MongoDB Collections
- `policies` - Full policy documents
- `schemes` - Government schemes
- `policy_impacts` - Historical impact data
- `policy_metadata` - Searchable metadata

---

## 🔍 Search & Retrieval Features

### 1. Semantic Search
- Find policies by natural language query
- "Show me education policies in Karnataka"
- "What are the tax incentives for IT companies?"

### 2. Filtered Search
- By state
- By category
- By year
- By budget range

### 3. Comparison
- Compare policies across states
- Compare similar policies over time
- Benchmark against national averages

---

## 🤖 AI Agent Enhancements

### 1. Policy Agent
- Access to full policy knowledge base
- Can cite specific policies
- Provides policy recommendations
- Compares with existing policies

### 2. Impact Agent
- Uses historical policy impact data
- Predicts based on similar policies
- Considers state-specific context

### 3. Explainability Agent
- References actual policy documents
- Cites government sources
- Provides policy numbers and dates

---

## 📊 Expected Coverage

### Central Policies (100+)
- Major schemes: 50+
- Sector policies: 30+
- Economic policies: 20+

### State Policies (1000+)
- Per state: 25-30 policies
- 36 states × 28 avg = 1008 policies

### Total Documents: 1100+

---

## 🚀 Implementation Timeline

### Week 1-2: Data Collection
- Set up scraping infrastructure
- Collect central government policies
- Collect major state policies
- Store in MongoDB

### Week 3-4: Processing & Indexing
- Process all documents
- Create embeddings
- Build vector store
- Test search functionality

### Week 5-6: Agent Integration
- Enhance all 6 agents
- Add policy search tools
- Test with real queries
- Validate accuracy

### Week 7-8: Testing & Refinement
- End-to-end testing
- Accuracy validation
- Performance optimization
- Documentation

---

## 💰 Cost: ₹0 (100% FREE)

### Free Resources:
- ✅ Official government websites (public domain)
- ✅ Open-source embeddings (HuggingFace)
- ✅ FAISS vector store (free)
- ✅ MongoDB Atlas (free tier)
- ✅ Python libraries (open source)

---

## 📈 Success Metrics

### Coverage
- ✅ 100% of central major schemes
- ✅ 80%+ of state policies
- ✅ All 36 states covered

### Accuracy
- ✅ 95%+ policy retrieval accuracy
- ✅ 90%+ prediction accuracy with context
- ✅ Verified against official sources

### Performance
- ✅ <2s policy search response time
- ✅ <5s simulation with policy context
- ✅ Efficient vector search

---

## 🔄 Maintenance Plan

### Monthly Updates
- Check for new policies
- Update existing policies
- Add new schemes
- Refresh embeddings

### Quarterly Reviews
- Validate accuracy
- Update impact data
- Refine search algorithms
- User feedback integration

---

## 📝 Next Steps

1. **Approve this plan**
2. **Start data collection** (automated scripts)
3. **Build processing pipeline**
4. **Integrate with agents**
5. **Test and validate**
6. **Deploy enhanced system**

---

**This will make CivicSim AI the most comprehensive policy simulation platform with real government policy knowledge!** 🇮🇳

---

**Status**: 📋 PLAN READY  
**Cost**: ₹0 (100% FREE)  
**Timeline**: 8 weeks  
**Coverage**: 1100+ policy documents
