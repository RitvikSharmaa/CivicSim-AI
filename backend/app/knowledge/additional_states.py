"""
Additional state policies for remaining 30 states/UTs
To be integrated into policy_knowledge_base.py
"""

def get_uttar_pradesh_policies() -> dict:
    return {
        "economic": {
            "up_industrial_policy": {
                "name": "UP Industrial Investment & Employment Promotion Policy 2022",
                "department": "Industries Department",
                "launched": "2022-06-02",
                "objective": "Make UP $1 trillion economy",
                "investment_target": 10000000000000,  # ₹10 lakh crore
                "employment_target": 5000000,
                "impact_areas": ["Manufacturing", "Employment", "Investment"]
            }
        },
        "social": {
            "mukhyamantri_kanya_sumangala_yojana": {
                "name": "Mukhyamantri Kanya Sumangala Yojana",
                "department": "Women and Child Development",
                "launched": "2019-04-01",
                "objective": "Financial assistance for girl child education",
                "amount": 15000,  # ₹15,000 total
                "beneficiaries": 1000000,
                "impact_areas": ["Girls education", "Women empowerment"]
            }
        }
    }

def get_rajasthan_policies() -> dict:
    return {
        "economic": {
            "rajasthan_investment_promotion_scheme": {
                "name": "Rajasthan Investment Promotion Scheme 2019",
                "department": "Industries Department",
                "launched": "2019-12-09",
                "objective": "Attract investment and create employment",
                "budget_allocation": 50000000000,  # ₹500 crore
                "impact_areas": ["Investment", "Employment", "Industrial growth"]
            }
        },
        "social": {
            "indira_gandhi_matritva_poshan_yojana": {
                "name": "Indira Gandhi Matritva Poshan Yojana",
                "department": "Women and Child Development",
                "launched": "2022-11-19",
                "objective": "Nutritional support for pregnant women",
                "amount": 6000,  # ₹6,000 per beneficiary
                "beneficiaries": 350000,
                "impact_areas": ["Maternal health", "Nutrition"]
            }
        }
    }

def get_madhya_pradesh_policies() -> dict:
    return {
        "economic": {
            "mp_industrial_promotion_policy": {
                "name": "MP Industrial Promotion Policy 2023",
                "department": "Industries Department",
                "launched": "2023-01-01",
                "objective": "Promote industrial development",
                "investment_target": 5000000000000,  # ₹5 lakh crore
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "ladli_laxmi_yojana": {
                "name": "Ladli Laxmi Yojana",
                "department": "Women and Child Development",
                "launched": "2007-04-01",
                "objective": "Financial security for girl child",
                "amount": 118000,  # ₹1.18 lakh total
                "beneficiaries": 4500000,
                "impact_areas": ["Girls education", "Women empowerment"]
            }
        }
    }

def get_andhra_pradesh_policies() -> dict:
    return {
        "economic": {
            "ap_industrial_development_policy": {
                "name": "AP Industrial Development Policy 2020-23",
                "department": "Industries Department",
                "launched": "2020-07-01",
                "objective": "Promote industrial growth",
                "investment_target": 5000000000000,
                "impact_areas": ["Manufacturing", "Employment", "Investment"]
            }
        },
        "social": {
            "amma_vodi": {
                "name": "Amma Vodi",
                "department": "Education Department",
                "launched": "2020-01-09",
                "objective": "Financial assistance for mothers to send children to school",
                "amount": 15000,  # ₹15,000 per year
                "beneficiaries": 4300000,
                "budget_allocation": 64500000000,  # ₹6,450 crore
                "impact_areas": ["Education", "School enrollment"]
            }
        }
    }

def get_telangana_policies() -> dict:
    return {
        "economic": {
            "ts_industrial_project_approval": {
                "name": "TS-iPASS (Industrial Project Approval)",
                "department": "Industries Department",
                "launched": "2014-06-02",
                "objective": "Single window clearance for industries",
                "impact_areas": ["Ease of business", "Investment", "Employment"]
            }
        },
        "social": {
            "rythu_bandhu": {
                "name": "Rythu Bandhu",
                "department": "Agriculture Department",
                "launched": "2018-05-10",
                "objective": "Investment support for farmers",
                "amount": 10000,  # ₹10,000 per acre per year
                "beneficiaries": 5800000,
                "budget_allocation": 120000000000,  # ₹12,000 crore
                "impact_areas": ["Farmer income", "Agricultural investment"]
            }
        }
    }

def get_kerala_policies() -> dict:
    return {
        "economic": {
            "kerala_startup_mission": {
                "name": "Kerala Startup Mission",
                "department": "IT Department",
                "launched": "2006-01-01",
                "objective": "Promote entrepreneurship and startups",
                "budget_allocation": 10000000000,  # ₹100 crore
                "impact_areas": ["Startups", "Innovation", "Employment"]
            }
        },
        "social": {
            "life_mission": {
                "name": "LIFE Mission (Housing for All)",
                "department": "Housing Department",
                "launched": "2016-11-25",
                "objective": "Provide housing for homeless",
                "target_houses": 400000,
                "budget_allocation": 250000000000,  # ₹25,000 crore
                "impact_areas": ["Housing", "Quality of life"]
            }
        }
    }

def get_punjab_policies() -> dict:
    return {
        "economic": {
            "punjab_industrial_policy": {
                "name": "Punjab Industrial & Business Development Policy 2017",
                "department": "Industries Department",
                "launched": "2017-02-23",
                "objective": "Promote industrial development",
                "investment_target": 1000000000000,  # ₹1 lakh crore
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "shagun_scheme": {
                "name": "Shagun Scheme",
                "department": "Social Justice Department",
                "launched": "2018-01-01",
                "objective": "Financial assistance for SC girls marriage",
                "amount": 21000,  # ₹21,000
                "beneficiaries": 50000,
                "impact_areas": ["Social welfare", "SC empowerment"]
            }
        }
    }

def get_haryana_policies() -> dict:
    return {
        "economic": {
            "haryana_enterprise_promotion_policy": {
                "name": "Haryana Enterprise & Employment Policy 2020",
                "department": "Industries Department",
                "launched": "2020-03-01",
                "objective": "Promote enterprises and employment",
                "employment_target": 500000,
                "impact_areas": ["Employment", "MSMEs", "Investment"]
            }
        },
        "social": {
            "kanyadan_yojana": {
                "name": "Kanyadan Yojana",
                "department": "Women and Child Development",
                "launched": "2015-01-01",
                "objective": "Financial assistance for girls marriage",
                "amount": 51000,  # ₹51,000
                "beneficiaries": 30000,
                "impact_areas": ["Social welfare", "Women empowerment"]
            }
        }
    }

def get_bihar_policies() -> dict:
    return {
        "economic": {
            "bihar_industrial_investment_promotion_policy": {
                "name": "Bihar Industrial Investment Promotion Policy 2016",
                "department": "Industries Department",
                "launched": "2016-07-01",
                "objective": "Promote industrial investment",
                "investment_target": 1000000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "mukhyamantri_kanya_utthan_yojana": {
                "name": "Mukhyamantri Kanya Utthan Yojana",
                "department": "Education Department",
                "launched": "2018-04-01",
                "objective": "Financial assistance for girls education",
                "amount": 54100,  # ₹54,100 total
                "beneficiaries": 1500000,
                "impact_areas": ["Girls education", "Women empowerment"]
            }
        }
    }

def get_odisha_policies() -> dict:
    return {
        "economic": {
            "odisha_industrial_policy": {
                "name": "Odisha Industrial Policy Resolution 2022",
                "department": "Industries Department",
                "launched": "2022-01-01",
                "objective": "Promote industrial development",
                "investment_target": 5000000000000,
                "impact_areas": ["Manufacturing", "Employment", "Investment"]
            }
        },
        "social": {
            "biju_swasthya_kalyan_yojana": {
                "name": "Biju Swasthya Kalyan Yojana",
                "department": "Health Department",
                "launched": "2018-08-15",
                "objective": "Free healthcare for all",
                "coverage": 1000000,  # ₹10 lakh per family
                "beneficiaries": 35000000,
                "impact_areas": ["Healthcare access", "Financial protection"]
            }
        }
    }

def get_jharkhand_policies() -> dict:
    return {
        "economic": {
            "jharkhand_industrial_policy": {
                "name": "Jharkhand Industrial & Investment Promotion Policy 2016",
                "department": "Industries Department",
                "launched": "2016-04-01",
                "objective": "Promote industrial investment",
                "investment_target": 500000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "savitribai_phule_kishori_samridhi_yojana": {
                "name": "Savitribai Phule Kishori Samridhi Yojana",
                "department": "Women and Child Development",
                "launched": "2019-08-15",
                "objective": "Financial assistance for girl child",
                "amount": 40000,  # ₹40,000 total
                "beneficiaries": 500000,
                "impact_areas": ["Girls education", "Women empowerment"]
            }
        }
    }

def get_chhattisgarh_policies() -> dict:
    return {
        "economic": {
            "chhattisgarh_industrial_policy": {
                "name": "Chhattisgarh Industrial Policy 2019-24",
                "department": "Industries Department",
                "launched": "2019-01-01",
                "objective": "Promote industrial development",
                "investment_target": 1000000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "kaushalya_matritva_yojana": {
                "name": "Kaushalya Matritva Yojana",
                "department": "Women and Child Development",
                "launched": "2022-03-08",
                "objective": "Nutritional support for pregnant women",
                "amount": 5000,  # ₹5,000
                "beneficiaries": 300000,
                "impact_areas": ["Maternal health", "Nutrition"]
            }
        }
    }

def get_assam_policies() -> dict:
    return {
        "economic": {
            "assam_industrial_policy": {
                "name": "Assam Industrial & Investment Policy 2022",
                "department": "Industries Department",
                "launched": "2022-01-01",
                "objective": "Promote industrial development",
                "investment_target": 500000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "orunodoi_scheme": {
                "name": "Orunodoi Scheme",
                "department": "Social Welfare Department",
                "launched": "2020-10-02",
                "objective": "Financial assistance to poor families",
                "amount": 1250,  # ₹1,250 per month
                "beneficiaries": 2200000,
                "budget_allocation": 33000000000,  # ₹3,300 crore
                "impact_areas": ["Poverty alleviation", "Social welfare"]
            }
        }
    }

def get_uttarakhand_policies() -> dict:
    return {
        "economic": {
            "uttarakhand_industrial_policy": {
                "name": "Uttarakhand Industrial Development Policy 2022",
                "department": "Industries Department",
                "launched": "2022-01-01",
                "objective": "Promote industrial development",
                "investment_target": 250000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "atal_ayushman_yojana": {
                "name": "Atal Ayushman Uttarakhand Yojana",
                "department": "Health Department",
                "launched": "2018-09-23",
                "objective": "Free healthcare coverage",
                "coverage": 500000,  # ₹5 lakh per family
                "beneficiaries": 2500000,
                "impact_areas": ["Healthcare access", "Financial protection"]
            }
        }
    }

def get_himachal_pradesh_policies() -> dict:
    return {
        "economic": {
            "hp_industrial_policy": {
                "name": "HP Industrial Investment Policy 2019",
                "department": "Industries Department",
                "launched": "2019-01-01",
                "objective": "Promote industrial investment",
                "investment_target": 100000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "him_care_scheme": {
                "name": "Him Care Scheme",
                "department": "Health Department",
                "launched": "2019-01-01",
                "objective": "Health insurance for all",
                "coverage": 500000,  # ₹5 lakh per family
                "beneficiaries": 1800000,
                "impact_areas": ["Healthcare access", "Financial protection"]
            }
        }
    }

def get_goa_policies() -> dict:
    return {
        "economic": {
            "goa_startup_policy": {
                "name": "Goa Startup Policy 2017",
                "department": "IT Department",
                "launched": "2017-01-01",
                "objective": "Promote startups and entrepreneurship",
                "budget_allocation": 5000000000,  # ₹50 crore
                "impact_areas": ["Startups", "Innovation", "Employment"]
            }
        },
        "social": {
            "laadli_laxmi_scheme": {
                "name": "Laadli Laxmi Scheme",
                "department": "Women and Child Development",
                "launched": "2008-01-01",
                "objective": "Financial assistance for girl child",
                "amount": 100000,  # ₹1 lakh
                "beneficiaries": 50000,
                "impact_areas": ["Girls education", "Women empowerment"]
            }
        }
    }

# Union Territories
def get_jammu_kashmir_policies() -> dict:
    return {
        "economic": {
            "jk_industrial_development_scheme": {
                "name": "J&K Industrial Development Scheme",
                "department": "Industries Department",
                "launched": "2021-02-19",
                "objective": "Promote industrial development",
                "budget_allocation": 280000000000,  # ₹28,400 crore
                "impact_areas": ["Manufacturing", "Employment", "Investment"]
            }
        },
        "social": {
            "sehat_scheme": {
                "name": "Ayushman Bharat PMJAY SEHAT",
                "department": "Health Department",
                "launched": "2020-12-26",
                "objective": "Universal health coverage",
                "coverage": 500000,  # ₹5 lakh per family
                "beneficiaries": 6000000,
                "impact_areas": ["Healthcare access", "Financial protection"]
            }
        }
    }

def get_ladakh_policies() -> dict:
    return {
        "economic": {
            "ladakh_tourism_policy": {
                "name": "Ladakh Tourism Policy",
                "department": "Tourism Department",
                "launched": "2020-01-01",
                "objective": "Promote sustainable tourism",
                "budget_allocation": 5000000000,  # ₹50 crore
                "impact_areas": ["Tourism", "Employment", "Economy"]
            }
        },
        "social": {
            "ladakh_health_scheme": {
                "name": "Ladakh Health Insurance Scheme",
                "department": "Health Department",
                "launched": "2020-01-01",
                "objective": "Health coverage for all residents",
                "coverage": 500000,
                "beneficiaries": 300000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_chandigarh_policies() -> dict:
    return {
        "economic": {
            "chandigarh_startup_policy": {
                "name": "Chandigarh Startup Policy",
                "department": "IT Department",
                "launched": "2018-01-01",
                "objective": "Promote startups",
                "budget_allocation": 2000000000,  # ₹20 crore
                "impact_areas": ["Startups", "Innovation"]
            }
        },
        "social": {
            "chandigarh_health_scheme": {
                "name": "Chandigarh Health Scheme",
                "department": "Health Department",
                "launched": "2019-01-01",
                "objective": "Healthcare for all",
                "coverage": 500000,
                "beneficiaries": 1100000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_puducherry_policies() -> dict:
    return {
        "economic": {
            "puducherry_industrial_policy": {
                "name": "Puducherry Industrial Policy",
                "department": "Industries Department",
                "launched": "2016-01-01",
                "objective": "Promote industrial development",
                "investment_target": 50000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "puducherry_health_scheme": {
                "name": "Chief Minister's Comprehensive Health Insurance Scheme",
                "department": "Health Department",
                "launched": "2013-01-01",
                "objective": "Health insurance for all",
                "coverage": 400000,  # ₹4 lakh
                "beneficiaries": 1000000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

# Northeastern States
def get_tripura_policies() -> dict:
    return {
        "economic": {
            "tripura_industrial_policy": {
                "name": "Tripura Industrial Policy 2022",
                "department": "Industries Department",
                "launched": "2022-01-01",
                "objective": "Promote industrial development",
                "investment_target": 50000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "tripura_health_scheme": {
                "name": "Tripura Health Insurance Scheme",
                "department": "Health Department",
                "launched": "2019-01-01",
                "objective": "Health coverage",
                "coverage": 500000,
                "beneficiaries": 1500000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_manipur_policies() -> dict:
    return {
        "economic": {
            "manipur_industrial_policy": {
                "name": "Manipur Industrial Policy 2022",
                "department": "Industries Department",
                "launched": "2022-01-01",
                "objective": "Promote industrial development",
                "investment_target": 50000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "cm_gi_scheme": {
                "name": "CM-GI (Chief Minister-Gi Kayathang)",
                "department": "Health Department",
                "launched": "2018-01-01",
                "objective": "Universal health coverage",
                "coverage": 500000,
                "beneficiaries": 1200000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_meghalaya_policies() -> dict:
    return {
        "economic": {
            "meghalaya_industrial_policy": {
                "name": "Meghalaya Industrial & Investment Promotion Policy 2020",
                "department": "Industries Department",
                "launched": "2020-01-01",
                "objective": "Promote industrial development",
                "investment_target": 50000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "megha_health_insurance_scheme": {
                "name": "Megha Health Insurance Scheme",
                "department": "Health Department",
                "launched": "2012-01-01",
                "objective": "Health insurance",
                "coverage": 500000,
                "beneficiaries": 1000000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_nagaland_policies() -> dict:
    return {
        "economic": {
            "nagaland_industrial_policy": {
                "name": "Nagaland Industrial Policy 2021",
                "department": "Industries Department",
                "launched": "2021-01-01",
                "objective": "Promote industrial development",
                "investment_target": 30000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "nagaland_health_insurance_scheme": {
                "name": "Nagaland Health Insurance Scheme",
                "department": "Health Department",
                "launched": "2016-01-01",
                "objective": "Health coverage",
                "coverage": 500000,
                "beneficiaries": 800000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_mizoram_policies() -> dict:
    return {
        "economic": {
            "mizoram_industrial_policy": {
                "name": "Mizoram Industrial Policy 2021",
                "department": "Industries Department",
                "launched": "2021-01-01",
                "objective": "Promote industrial development",
                "investment_target": 30000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "mizoram_health_scheme": {
                "name": "Mizoram State Health Care Scheme",
                "department": "Health Department",
                "launched": "2015-01-01",
                "objective": "Health coverage",
                "coverage": 500000,
                "beneficiaries": 600000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_arunachal_pradesh_policies() -> dict:
    return {
        "economic": {
            "arunachal_industrial_policy": {
                "name": "Arunachal Pradesh Industrial Policy 2022",
                "department": "Industries Department",
                "launched": "2022-01-01",
                "objective": "Promote industrial development",
                "investment_target": 50000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "cm_arogya_arunachal_yojana": {
                "name": "CM Arogya Arunachal Yojana",
                "department": "Health Department",
                "launched": "2018-01-01",
                "objective": "Health insurance",
                "coverage": 500000,
                "beneficiaries": 700000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_sikkim_policies() -> dict:
    return {
        "economic": {
            "sikkim_industrial_policy": {
                "name": "Sikkim Industrial Policy 2022",
                "department": "Industries Department",
                "launched": "2022-01-01",
                "objective": "Promote industrial development",
                "investment_target": 30000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "mukh_mantri_swasthya_bima_yojana": {
                "name": "Mukhya Mantri Swasthya Bima Yojana",
                "department": "Health Department",
                "launched": "2018-01-01",
                "objective": "Health insurance",
                "coverage": 500000,
                "beneficiaries": 400000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_andaman_nicobar_policies() -> dict:
    return {
        "economic": {
            "andaman_tourism_policy": {
                "name": "Andaman & Nicobar Tourism Policy",
                "department": "Tourism Department",
                "launched": "2019-01-01",
                "objective": "Promote sustainable tourism",
                "budget_allocation": 5000000000,
                "impact_areas": ["Tourism", "Employment"]
            }
        },
        "social": {
            "andaman_health_scheme": {
                "name": "Andaman Health Insurance Scheme",
                "department": "Health Department",
                "launched": "2019-01-01",
                "objective": "Health coverage",
                "coverage": 500000,
                "beneficiaries": 400000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_lakshadweep_policies() -> dict:
    return {
        "economic": {
            "lakshadweep_tourism_policy": {
                "name": "Lakshadweep Tourism Policy",
                "department": "Tourism Department",
                "launched": "2020-01-01",
                "objective": "Promote eco-tourism",
                "budget_allocation": 2000000000,
                "impact_areas": ["Tourism", "Employment"]
            }
        },
        "social": {
            "lakshadweep_health_scheme": {
                "name": "Lakshadweep Health Scheme",
                "department": "Health Department",
                "launched": "2019-01-01",
                "objective": "Health coverage",
                "coverage": 500000,
                "beneficiaries": 70000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }

def get_dnh_dd_policies() -> dict:
    return {
        "economic": {
            "dnh_dd_industrial_policy": {
                "name": "DNH & DD Industrial Policy",
                "department": "Industries Department",
                "launched": "2020-01-01",
                "objective": "Promote industrial development",
                "investment_target": 20000000000,
                "impact_areas": ["Manufacturing", "Employment"]
            }
        },
        "social": {
            "dnh_dd_health_scheme": {
                "name": "DNH & DD Health Scheme",
                "department": "Health Department",
                "launched": "2020-01-01",
                "objective": "Health coverage",
                "coverage": 500000,
                "beneficiaries": 600000,
                "impact_areas": ["Healthcare access"]
            }
        }
    }
