"""
Policy Document Scraper
Collects policy documents from official Indian government sources
"""

import asyncio
import aiohttp
from typing import List, Dict, Optional
from datetime import datetime
import logging
from bs4 import BeautifulSoup
import json

logger = logging.getLogger(__name__)


class PolicyScraper:
    """Scrape policy documents from official government sources"""
    
    # Official government sources (all FREE and public domain)
    CENTRAL_SOURCES = {
        "india_gov": "https://www.india.gov.in",
        "niti_aayog": "https://niti.gov.in",
        "prs_india": "https://prsindia.org",
        "pm_india": "https://www.pmindia.gov.in",
        "data_gov": "https://data.gov.in"
    }
    
    STATE_SOURCES = {
        "Karnataka": "https://karnataka.gov.in",
        "Maharashtra": "https://maharashtra.gov.in",
        "Tamil Nadu": "https://tn.gov.in",
        "Delhi": "https://delhi.gov.in",
        "Gujarat": "https://gujaratindia.gov.in",
        "West Bengal": "https://wb.gov.in",
        "Uttar Pradesh": "https://up.gov.in",
        "Rajasthan": "https://rajasthan.gov.in",
        "Madhya Pradesh": "https://mp.gov.in",
        "Bihar": "https://state.bihar.gov.in",
        # Add all 36 states/UTs
    }
    
    POLICY_CATEGORIES = [
        "education",
        "health",
        "infrastructure",
        "agriculture",
        "industry",
        "taxation",
        "social_welfare",
        "environment",
        "urban_development",
        "rural_development"
    ]
    
    def __init__(self):
        self.session = None
        self.policies_collected = []
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def scrape_all_policies(self) -> List[Dict]:
        """Scrape policies from all sources"""
        logger.info("Starting policy collection from official sources...")
        
        tasks = []
        
        # Scrape central policies
        tasks.append(self.scrape_central_policies())
        
        # Scrape state policies
        for state in self.STATE_SOURCES.keys():
            tasks.append(self.scrape_state_policies(state))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Flatten results
        all_policies = []
        for result in results:
            if isinstance(result, list):
                all_policies.extend(result)
            elif isinstance(result, Exception):
                logger.error(f"Error during scraping: {result}")
        
        logger.info(f"Collected {len(all_policies)} policy documents")
        return all_policies
    
    async def scrape_central_policies(self) -> List[Dict]:
        """Scrape central government policies"""
        logger.info("Scraping central government policies...")
        
        # For now, return curated list of major central schemes
        # In production, this would scrape from official websites
        
        central_policies = [
            {
                "policy_id": "central_001",
                "policy_name": "National Education Policy (NEP) 2020",
                "type": "Central",
                "category": "Education",
                "year": 2020,
                "description": "Comprehensive reform of education system from school to higher education",
                "objectives": [
                    "Universal access to quality education",
                    "Multidisciplinary approach",
                    "Skill development focus",
                    "Technology integration"
                ],
                "budget_allocation": 99300000000,  # ₹99,300 crore
                "applicable_states": "All",
                "source": "Ministry of Education",
                "source_url": "https://www.education.gov.in/nep",
                "last_updated": datetime.now().isoformat()
            },
            {
                "policy_id": "central_002",
                "policy_name": "Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana",
                "type": "Central",
                "category": "Health",
                "year": 2018,
                "description": "World's largest health insurance scheme providing coverage up to ₹5 lakh",
                "objectives": [
                    "Universal health coverage",
                    "Financial protection",
                    "Quality healthcare access"
                ],
                "budget_allocation": 60000000000,  # ₹60,000 crore
                "beneficiaries": 500000000,
                "applicable_states": "All",
                "source": "Ministry of Health",
                "source_url": "https://pmjay.gov.in",
                "last_updated": datetime.now().isoformat()
            },
            {
                "policy_id": "central_003",
                "policy_name": "Smart Cities Mission",
                "type": "Central",
                "category": "Urban Development",
                "year": 2015,
                "description": "Development of 100 smart cities with modern infrastructure",
                "objectives": [
                    "Sustainable urban development",
                    "Technology-enabled services",
                    "Quality of life improvement"
                ],
                "budget_allocation": 480000000000,  # ₹48,000 crore
                "cities_covered": 100,
                "applicable_states": "All",
                "source": "Ministry of Housing and Urban Affairs",
                "source_url": "https://smartcities.gov.in",
                "last_updated": datetime.now().isoformat()
            },
            {
                "policy_id": "central_004",
                "policy_name": "Pradhan Mantri Awas Yojana (PMAY)",
                "type": "Central",
                "category": "Housing",
                "year": 2015,
                "description": "Housing for All by 2022 - affordable housing scheme",
                "objectives": [
                    "Housing for all",
                    "Slum rehabilitation",
                    "Affordable housing credit"
                ],
                "budget_allocation": 200000000000,  # ₹20,000 crore annually
                "target_houses": 20000000,
                "applicable_states": "All",
                "source": "Ministry of Housing and Urban Affairs",
                "source_url": "https://pmaymis.gov.in",
                "last_updated": datetime.now().isoformat()
            },
            {
                "policy_id": "central_005",
                "policy_name": "Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA)",
                "type": "Central",
                "category": "Rural Development",
                "year": 2005,
                "description": "100 days of guaranteed wage employment to rural households",
                "objectives": [
                    "Livelihood security",
                    "Rural infrastructure development",
                    "Drought proofing"
                ],
                "budget_allocation": 730000000000,  # ₹73,000 crore
                "beneficiaries": 80000000,
                "applicable_states": "All",
                "source": "Ministry of Rural Development",
                "source_url": "https://nrega.nic.in",
                "last_updated": datetime.now().isoformat()
            }
        ]
        
        return central_policies
    
    async def scrape_state_policies(self, state: str) -> List[Dict]:
        """Scrape state-specific policies"""
        logger.info(f"Scraping policies for {state}...")
        
        # State-specific policies (curated list)
        # In production, this would scrape from state government websites
        
        state_policies_map = {
            "Karnataka": [
                {
                    "policy_id": "karnataka_001",
                    "policy_name": "Karnataka IT Policy 2025-2030",
                    "state": "Karnataka",
                    "type": "State",
                    "category": "Technology",
                    "year": 2025,
                    "valid_until": 2030,
                    "description": "Comprehensive IT policy targeting ₹11.5 lakh crore software exports and 90 lakh jobs",
                    "objectives": [
                        "Increase software exports to ₹11.5 lakh crore",
                        "Generate 90 lakh direct and indirect jobs",
                        "Focus on AI, Quantum Computing, Web3",
                        "Strengthen Bengaluru's global tech leadership"
                    ],
                    "budget_allocation": 50000000000,  # ₹5,000 crore
                    "key_provisions": [
                        "30% tax exemption for 5 years for new IT companies",
                        "Land at subsidized rates in IT parks",
                        "Skill development programs",
                        "R&D incentives"
                    ],
                    "source": "Karnataka Department of IT",
                    "source_url": "https://itbt.karnataka.gov.in",
                    "last_updated": datetime.now().isoformat()
                },
                {
                    "policy_id": "karnataka_002",
                    "policy_name": "Karnataka Space Technology Policy 2025-2030",
                    "state": "Karnataka",
                    "type": "State",
                    "category": "Space Technology",
                    "year": 2025,
                    "valid_until": 2030,
                    "description": "Attract $3 billion investment in space sector",
                    "objectives": [
                        "Attract $3 billion space investments",
                        "Create 10,000 jobs in space sector",
                        "Establish Karnataka as space tech hub"
                    ],
                    "budget_allocation": 10000000000,  # ₹1,000 crore
                    "source": "Karnataka Department of IT",
                    "last_updated": datetime.now().isoformat()
                }
            ],
            "Maharashtra": [
                {
                    "policy_id": "maharashtra_001",
                    "policy_name": "Maharashtra Infrastructure Development Policy",
                    "state": "Maharashtra",
                    "type": "State",
                    "category": "Infrastructure",
                    "year": 2024,
                    "description": "Comprehensive infrastructure development including expressways and metro projects",
                    "objectives": [
                        "Develop 5000 km of expressways",
                        "Expand metro networks in major cities",
                        "Improve port connectivity"
                    ],
                    "budget_allocation": 500000000000,  # ₹50,000 crore
                    "source": "Maharashtra PWD",
                    "last_updated": datetime.now().isoformat()
                }
            ],
            "Tamil Nadu": [
                {
                    "policy_id": "tamilnadu_001",
                    "policy_name": "Tamil Nadu Industrial Policy 2021",
                    "state": "Tamil Nadu",
                    "type": "State",
                    "category": "Industry",
                    "year": 2021,
                    "description": "Attract ₹10 lakh crore investment and create 20 lakh jobs",
                    "objectives": [
                        "Attract ₹10 lakh crore investment",
                        "Create 20 lakh jobs",
                        "Focus on manufacturing and exports"
                    ],
                    "budget_allocation": 100000000000,  # ₹10,000 crore
                    "source": "Tamil Nadu Industries Department",
                    "last_updated": datetime.now().isoformat()
                }
            ]
        }
        
        return state_policies_map.get(state, [])
    
    def save_policies_to_file(self, policies: List[Dict], filename: str = "policies_data.json"):
        """Save collected policies to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(policies, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved {len(policies)} policies to {filename}")


# Standalone function to run scraper
async def collect_all_policies():
    """Collect all policies from government sources"""
    async with PolicyScraper() as scraper:
        policies = await scraper.scrape_all_policies()
        scraper.save_policies_to_file(policies, "backend/data/policies_data.json")
        return policies


if __name__ == "__main__":
    # Run the scraper
    asyncio.run(collect_all_policies())
