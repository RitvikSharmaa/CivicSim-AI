"""
Comprehensive Policy Web Scraper
Scrapes policy data from official Indian government sources
"""

import asyncio
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

import httpx
from bs4 import BeautifulSoup
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_settings
from app.services.knowledge_base_service import KnowledgeBaseService
import logging
import re
from datetime import datetime
from typing import Dict, List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PolicyScraper:
    """Scrapes policy data from government websites"""
    
    def __init__(self, kb_service: KnowledgeBaseService):
        self.kb_service = kb_service
        self.client = httpx.AsyncClient(timeout=30.0, follow_redirects=True)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    async def close(self):
        await self.client.aclose()
    
    def extract_budget(self, text: str) -> Optional[float]:
        """Extract budget amount from text"""
        # Look for crore
        crore_match = re.search(r'₹?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*crore', text, re.IGNORECASE)
        if crore_match:
            amount = float(crore_match.group(1).replace(',', ''))
            return amount * 10000000
        
        # Look for lakh
        lakh_match = re.search(r'₹?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*lakh', text, re.IGNORECASE)
        if lakh_match:
            amount = float(lakh_match.group(1).replace(',', ''))
            return amount * 100000
        
        return None
    
    async def scrape_pib_releases(self, state: str = None) -> List[Dict]:
        """Scrape Press Information Bureau releases"""
        logger.info(f"📰 Scraping PIB releases for {state or 'all states'}...")
        policies = []
        
        try:
            # PIB search URL
            base_url = "https://pib.gov.in/allRel.aspx"
            
            response = await self.client.get(base_url, headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find press releases
                releases = soup.find_all('div', class_='content-area')[:20]  # Get latest 20
                
                for release in releases:
                    try:
                        title_elem = release.find('h3') or release.find('h2')
                        if not title_elem:
                            continue
                        
                        title = title_elem.get_text(strip=True)
                        
                        # Check if it's policy-related
                        policy_keywords = ['scheme', 'yojana', 'policy', 'mission', 'programme', 'initiative']
                        if any(keyword in title.lower() for keyword in policy_keywords):
                            content = release.get_text(strip=True)
                            
                            policy = {
                                "level": "national",
                                "state": "national",
                                "category": "social",  # Default
                                "policy_key": re.sub(r'[^a-z0-9]+', '_', title.lower())[:50],
                                "name": title,
                                "objective": content[:500],
                                "source": "PIB",
                                "scraped_at": datetime.utcnow().isoformat(),
                                "impact_areas": ["Government Initiative"]
                            }
                            
                            # Extract budget if present
                            budget = self.extract_budget(content)
                            if budget:
                                policy["budget_allocation"] = budget
                            
                            policies.append(policy)
                    except Exception as e:
                        logger.error(f"Error parsing release: {e}")
                        continue
                
                logger.info(f"   ✅ Found {len(policies)} policies from PIB")
        except Exception as e:
            logger.error(f"   ❌ PIB scraping failed: {e}")
        
        return policies
    
    async def scrape_niti_aayog(self) -> List[Dict]:
        """Scrape NITI Aayog initiatives"""
        logger.info("🏛️ Scraping NITI Aayog...")
        policies = []
        
        try:
            url = "https://www.niti.gov.in/verticals"
            response = await self.client.get(url, headers=self.headers)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find initiatives
                initiatives = soup.find_all('div', class_='views-row')[:15]
                
                for init in initiatives:
                    try:
                        title_elem = init.find('h3') or init.find('h2') or init.find('a')
                        if not title_elem:
                            continue
                        
                        title = title_elem.get_text(strip=True)
                        desc_elem = init.find('p') or init.find('div', class_='description')
                        description = desc_elem.get_text(strip=True) if desc_elem else ""
                        
                        policy = {
                            "level": "national",
                            "state": "national",
                            "category": "economic",
                            "policy_key": re.sub(r'[^a-z0-9]+', '_', title.lower())[:50],
                            "name": title,
                            "objective": description[:500],
                            "ministry": "NITI Aayog",
                            "source": "NITI Aayog",
                            "scraped_at": datetime.utcnow().isoformat(),
                            "impact_areas": ["Economic Development", "Policy Planning"]
                        }
                        
                        policies.append(policy)
                    except Exception as e:
                        logger.error(f"Error parsing initiative: {e}")
                        continue
                
                logger.info(f"   ✅ Found {len(policies)} policies from NITI Aayog")
        except Exception as e:
            logger.error(f"   ❌ NITI Aayog scraping failed: {e}")
        
        return policies
    
    async def scrape_state_portal(self, state: str, portal_url: str) -> List[Dict]:
        """Scrape state government portal"""
        logger.info(f"🏛️ Scraping {state} portal...")
        policies = []
        
        try:
            response = await self.client.get(portal_url, headers=self.headers)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Look for scheme/policy links
                links = soup.find_all('a', href=True)
                
                for link in links[:30]:  # Limit to 30 links
                    text = link.get_text(strip=True)
                    
                    # Check if it's a scheme/policy
                    if any(word in text.lower() for word in ['scheme', 'yojana', 'policy', 'programme']):
                        policy = {
                            "level": "state",
                            "state": state,
                            "category": "social",
                            "policy_key": re.sub(r'[^a-z0-9]+', '_', text.lower())[:50],
                            "name": text,
                            "objective": f"State scheme from {state}",
                            "source": portal_url,
                            "scraped_at": datetime.utcnow().isoformat(),
                            "impact_areas": ["State Initiative"]
                        }
                        
                        policies.append(policy)
                
                logger.info(f"   ✅ Found {len(policies)} policies from {state}")
        except Exception as e:
            logger.error(f"   ❌ {state} scraping failed: {e}")
        
        return policies
    
    async def scrape_all_sources(self) -> int:
        """Scrape all available sources"""
        logger.info("🌐 Starting comprehensive policy scraping...")
        
        all_policies = []
        
        # 1. PIB releases
        pib_policies = await self.scrape_pib_releases()
        all_policies.extend(pib_policies)
        
        # 2. NITI Aayog
        niti_policies = await self.scrape_niti_aayog()
        all_policies.extend(niti_policies)
        
        # 3. State portals (sample - add more as needed)
        state_portals = {
            "Karnataka": "https://karnataka.gov.in",
            "Maharashtra": "https://maharashtra.gov.in",
            "Tamil Nadu": "https://tn.gov.in",
            "Delhi": "https://delhi.gov.in",
            "Gujarat": "https://gujaratindia.gov.in",
            "Uttar Pradesh": "https://up.gov.in",
            "Rajasthan": "https://rajasthan.gov.in",
            "West Bengal": "https://wb.gov.in",
            "Telangana": "https://telangana.gov.in",
            "Kerala": "https://kerala.gov.in"
        }
        
        for state, url in state_portals.items():
            state_policies = await self.scrape_state_portal(state, url)
            all_policies.extend(state_policies)
            await asyncio.sleep(2)  # Be respectful to servers
        
        # 4. Insert into MongoDB
        if all_policies:
            logger.info(f"\n💾 Inserting {len(all_policies)} policies into MongoDB...")
            inserted = await self.kb_service.bulk_insert_policies(all_policies)
            logger.info(f"   ✅ Successfully inserted {inserted} new policies")
            return inserted
        
        return 0

async def main():
    """Main scraping function"""
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongodb_url)
    kb_service = KnowledgeBaseService(client, settings.database_name)
    
    scraper = PolicyScraper(kb_service)
    
    try:
        # Get initial count
        initial_stats = await kb_service.get_statistics()
        initial_count = initial_stats.get("total_policies", 0)
        logger.info(f"📊 Initial policy count: {initial_count}")
        
        # Scrape all sources
        new_policies = await scraper.scrape_all_sources()
        
        # Get final count
        final_stats = await kb_service.get_statistics()
        final_count = final_stats.get("total_policies", 0)
        
        logger.info(f"\n✅ Scraping complete!")
        logger.info(f"   Initial: {initial_count} policies")
        logger.info(f"   Added: {new_policies} policies")
        logger.info(f"   Final: {final_count} policies")
        
    except Exception as e:
        logger.error(f"❌ Scraping failed: {e}")
        raise
    finally:
        await scraper.close()
        client.close()

if __name__ == "__main__":
    asyncio.run(main())
