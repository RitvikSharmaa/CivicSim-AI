"""
Policy Knowledge Base for Indian States
Comprehensive policy documents, schemes, and data for all 36 states/UTs
"""

from typing import Dict, List, Optional
from datetime import datetime

class PolicyKnowledgeBase:
    """
    Centralized knowledge base for Indian government policies
    Sources: NITI Aayog, Ministry websites, State government portals, Budget documents
    """
    
    def __init__(self):
        self.policies = self._initialize_policies()
        self.schemes = self._initialize_schemes()
        self.economic_data = self._initialize_economic_data()
    
    def _initialize_policies(self) -> Dict:
        """Initialize comprehensive policy database"""
        return {
            # National Level Policies
            "national": {
                "economic": {
                    "make_in_india": {
                        "name": "Make in India",
                        "ministry": "Ministry of Commerce and Industry",
                        "launched": "2014-09-25",
                        "objective": "Transform India into a global manufacturing hub",
                        "sectors": ["Manufacturing", "Infrastructure", "Services"],
                        "budget_allocation": "Multiple schemes",
                        "impact_areas": ["Employment", "GDP", "Exports", "FDI"]
                    },
                    "atmanirbhar_bharat": {
                        "name": "Atmanirbhar Bharat (Self-Reliant India)",
                        "ministry": "Prime Minister's Office",
                        "launched": "2020-05-12",
                        "objective": "Make India self-reliant in all sectors",
                        "total_package": 2000000000000,  # ₹20 lakh crore
                        "pillars": ["Economy", "Infrastructure", "Technology", "Demography", "Demand"],
                        "impact_areas": ["Manufacturing", "MSMEs", "Agriculture", "Defense"]
                    },
                    "digital_india": {
                        "name": "Digital India",
                        "ministry": "Ministry of Electronics and IT",
                        "launched": "2015-07-01",
                        "objective": "Transform India into digitally empowered society",
                        "components": ["Digital Infrastructure", "Digital Services", "Digital Literacy"],
                        "budget_allocation": 450000000000,  # ₹4,500 crore
                        "impact_areas": ["Internet penetration", "E-governance", "Digital payments"]
                    }
                },
                "social": {
                    "pm_jan_dhan_yojana": {
                        "name": "Pradhan Mantri Jan Dhan Yojana",
                        "ministry": "Ministry of Finance",
                        "launched": "2014-08-28",
                        "objective": "Financial inclusion for all households",
                        "accounts_opened": 500000000,  # 50 crore+
                        "benefits": ["Zero balance account", "RuPay debit card", "Insurance", "Overdraft"],
                        "impact_areas": ["Financial inclusion", "Direct benefit transfer", "Banking access"]
                    },
                    "ayushman_bharat": {
                        "name": "Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana",
                        "ministry": "Ministry of Health and Family Welfare",
                        "launched": "2018-09-23",
                        "objective": "Universal health coverage for poor families",
                        "coverage": 500000,  # ₹5 lakh per family per year
                        "beneficiaries": 500000000,  # 50 crore
                        "impact_areas": ["Healthcare access", "Out-of-pocket expenses", "Hospital admissions"]
                    },
                    "beti_bachao_beti_padhao": {
                        "name": "Beti Bachao Beti Padhao",
                        "ministry": "Ministry of Women and Child Development",
                        "launched": "2015-01-22",
                        "objective": "Address declining child sex ratio and empower girl child",
                        "budget_allocation": 20000000000,  # ₹200 crore
                        "impact_areas": ["Sex ratio", "Girls education", "Women empowerment"]
                    }
                },
                "infrastructure": {
                    "bharatmala_pariyojana": {
                        "name": "Bharatmala Pariyojana",
                        "ministry": "Ministry of Road Transport and Highways",
                        "launched": "2017-10-24",
                        "objective": "Develop national highway network",
                        "total_length": 83677,  # km
                        "budget": 540000000000,  # ₹5.40 lakh crore
                        "impact_areas": ["Connectivity", "Logistics cost", "Travel time"]
                    },
                    "sagarmala": {
                        "name": "Sagarmala Programme",
                        "ministry": "Ministry of Ports, Shipping and Waterways",
                        "launched": "2015-03-25",
                        "objective": "Port-led development and coastal connectivity",
                        "budget": 880000000000,  # ₹8.80 lakh crore
                        "impact_areas": ["Port capacity", "Coastal shipping", "Logistics"]
                    },
                    "smart_cities_mission": {
                        "name": "Smart Cities Mission",
                        "ministry": "Ministry of Housing and Urban Affairs",
                        "launched": "2015-06-25",
                        "objective": "Develop 100 smart cities",
                        "cities": 100,
                        "budget": 480000000000,  # ₹48,000 crore
                        "impact_areas": ["Urban infrastructure", "Quality of life", "Technology adoption"]
                    }
                },
                "agriculture": {
                    "pm_kisan": {
                        "name": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
                        "ministry": "Ministry of Agriculture and Farmers Welfare",
                        "launched": "2019-02-24",
                        "objective": "Income support to farmers",
                        "amount": 6000,  # ₹6,000 per year
                        "beneficiaries": 110000000,  # 11 crore farmers
                        "impact_areas": ["Farmer income", "Agricultural investment", "Rural economy"]
                    },
                    "pm_fasal_bima_yojana": {
                        "name": "Pradhan Mantri Fasal Bima Yojana",
                        "ministry": "Ministry of Agriculture and Farmers Welfare",
                        "launched": "2016-02-18",
                        "objective": "Crop insurance for farmers",
                        "premium_subsidy": "50-90%",
                        "coverage": "All food & oilseed crops",
                        "impact_areas": ["Risk mitigation", "Farmer income stability", "Agricultural credit"]
                    }
                },
                "education": {
                    "samagra_shiksha": {
                        "name": "Samagra Shiksha Abhiyan",
                        "ministry": "Ministry of Education",
                        "launched": "2018-05-24",
                        "objective": "Holistic education from pre-school to class 12",
                        "budget_allocation": 370000000000,  # ₹37,000 crore
                        "impact_areas": ["School enrollment", "Learning outcomes", "Infrastructure"]
                    },
                    "pm_poshan": {
                        "name": "PM POSHAN (Mid-Day Meal Scheme)",
                        "ministry": "Ministry of Education",
                        "launched": "1995-08-15",
                        "objective": "Nutritional support to school children",
                        "beneficiaries": 120000000,  # 12 crore children
                        "budget_allocation": 120000000000,  # ₹12,000 crore
                        "impact_areas": ["Nutrition", "School attendance", "Learning outcomes"]
                    }
                }
            },
            
            # State-Specific Policies
            "Karnataka": self._get_karnataka_policies(),
            "Maharashtra": self._get_maharashtra_policies(),
            "Tamil Nadu": self._get_tamil_nadu_policies(),
            "Delhi": self._get_delhi_policies(),
            "West Bengal": self._get_west_bengal_policies(),
            "Gujarat": self._get_gujarat_policies(),
            
            # Adding remaining 30 states/UTs
            "Uttar Pradesh": self._get_uttar_pradesh_policies(),
            "Rajasthan": self._get_rajasthan_policies(),
            "Madhya Pradesh": self._get_madhya_pradesh_policies(),
            "Andhra Pradesh": self._get_andhra_pradesh_policies(),
            "Telangana": self._get_telangana_policies(),
            "Kerala": self._get_kerala_policies(),
            "Punjab": self._get_punjab_policies(),
            "Haryana": self._get_haryana_policies(),
            "Bihar": self._get_bihar_policies(),
            "Odisha": self._get_odisha_policies(),
            "Jharkhand": self._get_jharkhand_policies(),
            "Chhattisgarh": self._get_chhattisgarh_policies(),
            "Assam": self._get_assam_policies(),
            "Uttarakhand": self._get_uttarakhand_policies(),
            "Himachal Pradesh": self._get_himachal_pradesh_policies(),
            "Goa": self._get_goa_policies(),
            "Jammu and Kashmir": self._get_jammu_kashmir_policies(),
            "Ladakh": self._get_ladakh_policies(),
            "Chandigarh": self._get_chandigarh_policies(),
            "Puducherry": self._get_puducherry_policies(),
            "Tripura": self._get_tripura_policies(),
            "Manipur": self._get_manipur_policies(),
            "Meghalaya": self._get_meghalaya_policies(),
            "Nagaland": self._get_nagaland_policies(),
            "Mizoram": self._get_mizoram_policies(),
            "Arunachal Pradesh": self._get_arunachal_pradesh_policies(),
            "Sikkim": self._get_sikkim_policies(),
            "Andaman and Nicobar Islands": self._get_andaman_nicobar_policies(),
            "Lakshadweep": self._get_lakshadweep_policies(),
            "Dadra and Nagar Haveli and Daman and Diu": self._get_dnh_dd_policies(),
            # Add more states...
        }
    
    def _get_karnataka_policies(self) -> Dict:
        """Karnataka-specific policies and schemes"""
        return {
            "economic": {
                "karnataka_startup_policy": {
                    "name": "Karnataka Startup Policy 2022-27",
                    "department": "Department of IT, BT and S&T",
                    "launched": "2022-01-01",
                    "objective": "Make Karnataka global startup hub",
                    "budget": 50000000000,  # ₹500 crore
                    "target": "Create 1 lakh jobs, support 10,000 startups",
                    "impact_areas": ["Startups", "Employment", "Innovation", "Investment"]
                },
                "karnataka_industrial_policy": {
                    "name": "Karnataka Industrial Policy 2020-25",
                    "department": "Department of Commerce and Industries",
                    "launched": "2020-04-01",
                    "objective": "Attract investment and create employment",
                    "investment_target": 5000000000000,  # ₹5 lakh crore
                    "employment_target": 2000000,  # 20 lakh jobs
                    "impact_areas": ["Manufacturing", "Services", "Employment", "GDP"]
                }
            },
            "social": {
                "gruha_jyothi": {
                    "name": "Gruha Jyothi (Free Electricity)",
                    "department": "Energy Department",
                    "launched": "2023-06-01",
                    "objective": "Provide 200 units free electricity to households",
                    "beneficiaries": 15000000,  # 1.5 crore households
                    "budget_allocation": 120000000000,  # ₹12,000 crore annually
                    "impact_areas": ["Household savings", "Energy access", "Quality of life"]
                },
                "gruha_lakshmi": {
                    "name": "Gruha Lakshmi",
                    "department": "Women and Child Development",
                    "launched": "2023-07-01",
                    "objective": "Financial assistance to women heads of families",
                    "amount": 2000,  # ₹2,000 per month
                    "beneficiaries": 13000000,  # 1.3 crore women
                    "budget_allocation": 312000000000,  # ₹31,200 crore annually
                    "impact_areas": ["Women empowerment", "Household income", "Financial independence"]
                },
                "anna_bhagya": {
                    "name": "Anna Bhagya",
                    "department": "Food and Civil Supplies",
                    "launched": "2023-08-01",
                    "objective": "Additional 5 kg rice per person per month",
                    "beneficiaries": 50000000,  # 5 crore people
                    "budget_allocation": 60000000000,  # ₹6,000 crore annually
                    "impact_areas": ["Food security", "Nutrition", "Poverty alleviation"]
                }
            },
            "infrastructure": {
                "bengaluru_metro_expansion": {
                    "name": "Namma Metro Phase 2 & 3",
                    "department": "Bangalore Metro Rail Corporation",
                    "launched": "2017-06-17",
                    "objective": "Expand metro network to 320 km",
                    "total_length": 320,  # km
                    "budget": 500000000000,  # ₹50,000 crore
                    "impact_areas": ["Urban mobility", "Traffic congestion", "Air quality"]
                }
            },
            "budget_2025_26": {
                "total_outlay": 408647000000,  # ₹4.09 lakh crore
                "gsdp_projection": 3070103000000,  # ₹30.70 lakh crore
                "gsdp_growth": 7.0,  # 7%
                "key_allocations": {
                    "guarantee_schemes": 560000000000,  # ₹56,000 crore
                    "infrastructure": 800000000000,  # ₹80,000 crore
                    "education": 450000000000,  # ₹45,000 crore
                    "health": 350000000000,  # ₹35,000 crore
                    "agriculture": 250000000000  # ₹25,000 crore
                }
            }
        }
    
    def _get_maharashtra_policies(self) -> Dict:
        """Maharashtra-specific policies"""
        return {
            "economic": {
                "maharashtra_industrial_policy": {
                    "name": "Maharashtra Industrial Policy 2019",
                    "department": "Industries Department",
                    "launched": "2019-04-01",
                    "objective": "Achieve $1 trillion economy by 2025",
                    "investment_target": 10000000000000,  # ₹10 lakh crore
                    "employment_target": 5000000,  # 50 lakh jobs
                    "impact_areas": ["Manufacturing", "Services", "Employment", "GDP"]
                },
                "maha_it_policy": {
                    "name": "Maharashtra IT/ITeS Policy 2023",
                    "department": "IT Department",
                    "launched": "2023-01-01",
                    "objective": "Make Maharashtra IT powerhouse",
                    "target_revenue": 5000000000000,  # ₹5 lakh crore by 2028
                    "employment_target": 1000000,  # 10 lakh jobs
                    "impact_areas": ["IT sector", "Employment", "Innovation"]
                }
            },
            "social": {
                "mahatma_jyotiba_phule_jan_arogya_yojana": {
                    "name": "Mahatma Jyotiba Phule Jan Arogya Yojana",
                    "department": "Public Health Department",
                    "launched": "2017-04-01",
                    "objective": "Universal health coverage",
                    "coverage": 150000,  # ₹1.5 lakh per family
                    "beneficiaries": 60000000,  # 6 crore people
                    "impact_areas": ["Healthcare access", "Financial protection"]
                }
            },
            "infrastructure": {
                "mumbai_metro": {
                    "name": "Mumbai Metro Rail Project",
                    "department": "Mumbai Metropolitan Region Development Authority",
                    "launched": "2014-06-08",
                    "objective": "Develop comprehensive metro network",
                    "total_length": 337,  # km planned
                    "budget": 1200000000000,  # ₹1.2 lakh crore
                    "impact_areas": ["Urban mobility", "Traffic congestion", "Air quality"]
                }
            }
        }
    
    def _get_tamil_nadu_policies(self) -> Dict:
        """Tamil Nadu-specific policies"""
        return {
            "economic": {
                "tamil_nadu_industrial_policy": {
                    "name": "Tamil Nadu Industrial Policy 2021",
                    "department": "Industries Department",
                    "launched": "2021-09-01",
                    "objective": "Achieve $1 trillion economy",
                    "investment_target": 10000000000000,  # ₹10 lakh crore
                    "employment_target": 3500000,  # 35 lakh jobs
                    "impact_areas": ["Manufacturing", "Services", "Employment"]
                }
            },
            "social": {
                "kalaignar_magalir_urimai_thogai": {
                    "name": "Kalaignar Magalir Urimai Thogai",
                    "department": "Social Welfare Department",
                    "launched": "2024-09-15",
                    "objective": "Financial assistance to women",
                    "amount": 1000,  # ₹1,000 per month
                    "beneficiaries": 10000000,  # 1 crore women
                    "budget_allocation": 120000000000,  # ₹12,000 crore annually
                    "impact_areas": ["Women empowerment", "Financial independence"]
                },
                "free_bus_travel_women": {
                    "name": "Free Bus Travel for Women",
                    "department": "Transport Department",
                    "launched": "2023-06-01",
                    "objective": "Free travel in government buses for women",
                    "beneficiaries": 15000000,  # 1.5 crore women daily
                    "budget_allocation": 20000000000,  # ₹2,000 crore annually
                    "impact_areas": ["Women mobility", "Employment", "Education"]
                }
            }
        }
    
    def _get_delhi_policies(self) -> Dict:
        """Delhi-specific policies"""
        return {
            "social": {
                "delhi_free_electricity": {
                    "name": "Delhi Free Electricity Scheme",
                    "department": "Power Department",
                    "launched": "2019-07-01",
                    "objective": "Provide 200 units free electricity",
                    "beneficiaries": 4500000,  # 45 lakh households
                    "budget_allocation": 30000000000,  # ₹3,000 crore annually
                    "impact_areas": ["Household savings", "Energy access"]
                },
                "delhi_free_water": {
                    "name": "Delhi Free Water Scheme",
                    "department": "Jal Board",
                    "launched": "2015-02-01",
                    "objective": "Provide 20,000 liters free water per month",
                    "beneficiaries": 4000000,  # 40 lakh households
                    "budget_allocation": 10000000000,  # ₹1,000 crore annually
                    "impact_areas": ["Water access", "Household savings"]
                },
                "mohalla_clinics": {
                    "name": "Mohalla Clinics",
                    "department": "Health Department",
                    "launched": "2015-07-19",
                    "objective": "Primary healthcare at doorstep",
                    "clinics": 500,  # Target
                    "budget_allocation": 5000000000,  # ₹500 crore
                    "impact_areas": ["Healthcare access", "Primary care", "Preventive health"]
                }
            },
            "education": {
                "delhi_education_revolution": {
                    "name": "Delhi Education Model",
                    "department": "Education Department",
                    "launched": "2015-02-01",
                    "objective": "Transform government schools",
                    "budget_allocation": 160000000000,  # ₹16,000 crore (26% of budget)
                    "impact_areas": ["Learning outcomes", "Infrastructure", "Teacher training"]
                }
            }
        }
    
    def _get_west_bengal_policies(self) -> Dict:
        """West Bengal-specific policies"""
        return {
            "social": {
                "lakshmir_bhandar": {
                    "name": "Lakshmir Bhandar",
                    "department": "Women and Child Development",
                    "launched": "2021-09-16",
                    "objective": "Financial assistance to women",
                    "amount_general": 1000,  # ₹1,000 per month
                    "amount_sc_st": 1200,  # ₹1,200 per month
                    "beneficiaries": 20000000,  # 2 crore women
                    "budget_allocation": 240000000000,  # ₹24,000 crore annually
                    "impact_areas": ["Women empowerment", "Poverty alleviation"]
                },
                "kanyashree_prakalpa": {
                    "name": "Kanyashree Prakalpa",
                    "department": "Women and Child Development",
                    "launched": "2013-10-01",
                    "objective": "Improve status of girls through education",
                    "beneficiaries": 7500000,  # 75 lakh girls
                    "budget_allocation": 15000000000,  # ₹1,500 crore
                    "impact_areas": ["Girls education", "Child marriage prevention"]
                }
            }
        }
    
    def _get_gujarat_policies(self) -> Dict:
        """Gujarat-specific policies"""
        return {
            "economic": {
                "vibrant_gujarat": {
                    "name": "Vibrant Gujarat Summit",
                    "department": "Industries Department",
                    "launched": "2003-01-01",
                    "objective": "Attract investment to Gujarat",
                    "investment_attracted": 50000000000000,  # ₹50 lakh crore (cumulative)
                    "frequency": "Biennial",
                    "impact_areas": ["Investment", "Employment", "Industrial growth"]
                }
            },
            "infrastructure": {
                "gift_city": {
                    "name": "Gujarat International Finance Tec-City (GIFT)",
                    "department": "Finance Department",
                    "launched": "2015-04-01",
                    "objective": "Create international financial services center",
                    "area": 886,  # acres
                    "budget": 780000000000,  # ₹78,000 crore
                    "impact_areas": ["Financial services", "Employment", "FDI"]
                }
            }
        }
    
    # NEW STATES - Adding all remaining 30 states/UTs
    
    def _get_uttar_pradesh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_uttar_pradesh_policies
        return get_uttar_pradesh_policies()
    
    def _get_rajasthan_policies(self) -> Dict:
        from app.knowledge.additional_states import get_rajasthan_policies
        return get_rajasthan_policies()
    
    def _get_madhya_pradesh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_madhya_pradesh_policies
        return get_madhya_pradesh_policies()
    
    def _get_andhra_pradesh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_andhra_pradesh_policies
        return get_andhra_pradesh_policies()
    
    def _get_telangana_policies(self) -> Dict:
        from app.knowledge.additional_states import get_telangana_policies
        return get_telangana_policies()
    
    def _get_kerala_policies(self) -> Dict:
        from app.knowledge.additional_states import get_kerala_policies
        return get_kerala_policies()
    
    def _get_punjab_policies(self) -> Dict:
        from app.knowledge.additional_states import get_punjab_policies
        return get_punjab_policies()
    
    def _get_haryana_policies(self) -> Dict:
        from app.knowledge.additional_states import get_haryana_policies
        return get_haryana_policies()
    
    def _get_bihar_policies(self) -> Dict:
        from app.knowledge.additional_states import get_bihar_policies
        return get_bihar_policies()
    
    def _get_odisha_policies(self) -> Dict:
        from app.knowledge.additional_states import get_odisha_policies
        return get_odisha_policies()
    
    def _get_jharkhand_policies(self) -> Dict:
        from app.knowledge.additional_states import get_jharkhand_policies
        return get_jharkhand_policies()
    
    def _get_chhattisgarh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_chhattisgarh_policies
        return get_chhattisgarh_policies()
    
    def _get_assam_policies(self) -> Dict:
        from app.knowledge.additional_states import get_assam_policies
        return get_assam_policies()
    
    def _get_uttarakhand_policies(self) -> Dict:
        from app.knowledge.additional_states import get_uttarakhand_policies
        return get_uttarakhand_policies()
    
    def _get_himachal_pradesh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_himachal_pradesh_policies
        return get_himachal_pradesh_policies()
    
    def _get_goa_policies(self) -> Dict:
        from app.knowledge.additional_states import get_goa_policies
        return get_goa_policies()
    
    def _get_jammu_kashmir_policies(self) -> Dict:
        from app.knowledge.additional_states import get_jammu_kashmir_policies
        return get_jammu_kashmir_policies()
    
    def _get_ladakh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_ladakh_policies
        return get_ladakh_policies()
    
    def _get_chandigarh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_chandigarh_policies
        return get_chandigarh_policies()
    
    def _get_puducherry_policies(self) -> Dict:
        from app.knowledge.additional_states import get_puducherry_policies
        return get_puducherry_policies()
    
    def _get_tripura_policies(self) -> Dict:
        from app.knowledge.additional_states import get_tripura_policies
        return get_tripura_policies()
    
    def _get_manipur_policies(self) -> Dict:
        from app.knowledge.additional_states import get_manipur_policies
        return get_manipur_policies()
    
    def _get_meghalaya_policies(self) -> Dict:
        from app.knowledge.additional_states import get_meghalaya_policies
        return get_meghalaya_policies()
    
    def _get_nagaland_policies(self) -> Dict:
        from app.knowledge.additional_states import get_nagaland_policies
        return get_nagaland_policies()
    
    def _get_mizoram_policies(self) -> Dict:
        from app.knowledge.additional_states import get_mizoram_policies
        return get_mizoram_policies()
    
    def _get_arunachal_pradesh_policies(self) -> Dict:
        from app.knowledge.additional_states import get_arunachal_pradesh_policies
        return get_arunachal_pradesh_policies()
    
    def _get_sikkim_policies(self) -> Dict:
        from app.knowledge.additional_states import get_sikkim_policies
        return get_sikkim_policies()
    
    def _get_andaman_nicobar_policies(self) -> Dict:
        from app.knowledge.additional_states import get_andaman_nicobar_policies
        return get_andaman_nicobar_policies()
    
    def _get_lakshadweep_policies(self) -> Dict:
        from app.knowledge.additional_states import get_lakshadweep_policies
        return get_lakshadweep_policies()
    
    def _get_dnh_dd_policies(self) -> Dict:
        from app.knowledge.additional_states import get_dnh_dd_policies
        return get_dnh_dd_policies()
    
    def _initialize_schemes(self) -> Dict:
        """Initialize government schemes database"""
        return {
            "central_sector": [
                "PM-KISAN", "Ayushman Bharat", "PM Jan Dhan Yojana",
                "Digital India", "Make in India", "Skill India",
                "Swachh Bharat Mission", "PM Awas Yojana"
            ],
            "centrally_sponsored": [
                "MGNREGA", "National Health Mission", "Samagra Shiksha",
                "PM Poshan", "Jal Jeevan Mission"
            ],
            "state_schemes": {
                "Karnataka": ["Gruha Jyothi", "Gruha Lakshmi", "Anna Bhagya", "Yuva Nidhi", "Shakti"],
                "Maharashtra": ["Mahatma Jyotiba Phule Jan Arogya Yojana", "Lek Ladki Yojana"],
                "Tamil Nadu": ["Kalaignar Magalir Urimai Thogai", "Free Bus Travel for Women"],
                "Delhi": ["Free Electricity", "Free Water", "Mohalla Clinics"],
                "West Bengal": ["Lakshmir Bhandar", "Kanyashree Prakalpa", "Rupashree Prakalpa"]
            }
        }
    
    def _initialize_economic_data(self) -> Dict:
        """Initialize economic indicators and data"""
        return {
            "national": {
                "gdp_growth": 7.3,  # %
                "inflation_rate": 5.2,  # %
                "unemployment_rate": 7.8,  # %
                "fiscal_deficit": 5.9,  # % of GDP
                "current_account_deficit": 1.2  # % of GDP
            },
            "state_wise": {
                "Karnataka": {
                    "gsdp": 3070103000000,  # ₹30.70 lakh crore
                    "gsdp_growth": 7.0,  # %
                    "per_capita_income": 364000,  # ₹3.64 lakh
                    "unemployment_rate": 2.9  # %
                },
                "Maharashtra": {
                    "gsdp": 4000000000000,  # ₹40 lakh crore (approx)
                    "gsdp_growth": 7.5,  # %
                    "per_capita_income": 350000,  # ₹3.50 lakh
                    "unemployment_rate": 4.2  # %
                }
            }
        }
    
    def get_policy(self, state: str, category: str, policy_name: str) -> Optional[Dict]:
        """Retrieve specific policy details"""
        try:
            if state == "national":
                return self.policies["national"].get(category, {}).get(policy_name)
            return self.policies.get(state, {}).get(category, {}).get(policy_name)
        except Exception:
            return None
    
    def get_all_policies_for_state(self, state: str) -> Dict:
        """Get all policies for a specific state"""
        return self.policies.get(state, {})
    
    def get_related_policies(self, policy_type: str, state: str = None) -> List[Dict]:
        """Get policies related to a specific type (e.g., 'tax', 'subsidy', 'infrastructure')"""
        related = []
        
        # Search in national policies
        for category, policies in self.policies.get("national", {}).items():
            for policy_name, policy_data in policies.items():
                if policy_type.lower() in str(policy_data).lower():
                    related.append({
                        "level": "national",
                        "category": category,
                        "name": policy_name,
                        "data": policy_data
                    })
        
        # Search in state policies if specified
        if state and state in self.policies:
            for category, policies in self.policies[state].items():
                if category == "budget_2025_26":
                    continue
                for policy_name, policy_data in policies.items():
                    if policy_type.lower() in str(policy_data).lower():
                        related.append({
                            "level": "state",
                            "state": state,
                            "category": category,
                            "name": policy_name,
                            "data": policy_data
                        })
        
        return related
    
    def get_budget_data(self, state: str, year: str = "2025_26") -> Optional[Dict]:
        """Get budget data for a state"""
        budget_key = f"budget_{year}"
        return self.policies.get(state, {}).get(budget_key)
    
    def search_policies(self, query: str) -> List[Dict]:
        """Search policies by keyword"""
        results = []
        query_lower = query.lower()
        
        # Search all policies
        for state, state_data in self.policies.items():
            if state == "national":
                for category, policies in state_data.items():
                    for policy_name, policy_data in policies.items():
                        if query_lower in str(policy_data).lower():
                            results.append({
                                "state": "National",
                                "category": category,
                                "policy": policy_name,
                                "data": policy_data
                            })
            else:
                for category, policies in state_data.items():
                    if category.startswith("budget_"):
                        continue
                    if isinstance(policies, dict):
                        for policy_name, policy_data in policies.items():
                            if query_lower in str(policy_data).lower():
                                results.append({
                                    "state": state,
                                    "category": category,
                                    "policy": policy_name,
                                    "data": policy_data
                                })
        
        return results

# Singleton instance
policy_kb = PolicyKnowledgeBase()
