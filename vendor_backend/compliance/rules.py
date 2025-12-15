from typing import Dict, List

POLICY_CATALOG: Dict[str, List[str]] = {
    # ---------------- UNIVERSAL ----------------
    "universal": [
        "vendor_master_form"
    ],

    # ---------------- ASIA PACIFIC ----------------
    "singapore": [
        "gst_registration_certificate",
        "acra_business_registration_certificate"
    ],
    "australia": [
        "abn_registration_certificate",
        "gst_registration_evidence"
    ],
    "india": [
        "gstin_registration_certificate",
        "pan_card_copy",
        "msme_registration_certificate"
    ],
    "japan": [
        "corporate_registration_certificate",
        "tax_identification_certificate"
    ],
    "china": [
        "business_license",
        "tax_registration_certificate",
        "organization_code_certificate"
    ],
    "malaysia": [
        "ssm_company_profile",
        "gst_registration_certificate"
    ],
    "philippines": [
        "bir_registration_certificate",
        "mayors_permit"
    ],
    "indonesia": [
        "npwp_tax_id",
        "business_license_siup"
    ],
    "thailand": [
        "vat_registration_certificate",
        "commercial_registration_certificate"
    ],
    "south_korea": [
        "business_registration_certificate",
        "corporate_seal_certificate"
    ],
    "vietnam": [
        "enterprise_registration_certificate",
        "tax_code_registration"
    ],

    # ---------------- EUROPE ----------------
    "united_kingdom": [
        "companies_house_registration_certificate",
        "vat_certificate"
    ],
    "germany": [
        "handelsregisterauszug_commercial_register_extract",
        "vat_registration_certificate"
    ],
    "france": [
        "kbis_extract",
        "siret_number_certificate"
    ],
    "italy": [
        "visura_camerale",
        "vat_registration_certificate"
    ],
    "spain": [
        "cif_tax_identification_number",
        "company_registration_certificate"
    ],
    "netherlands": [
        "kvk_registration_extract",
        "vat_registration_certificate"
    ],
    "switzerland": [
        "handelsregisterauszug_commercial_register",
        "vat_registration_certificate"
    ],
    "poland": [
        "national_court_register_extract",
        "vat_number_certificate"
    ],
    "ireland": [
        "company_registration_number_certificate",
        "tax_clearance_certificate"
    ],
    "sweden": [
        "bolagsverket_certificate",
        "vat_registration_certificate"
    ],

    # ---------------- AMERICAS ----------------
    "united_states": [
        "w9_form",
        "irs_ein_confirmation_letter"
    ],
    "canada": [
        "business_number_registration_certificate",
        "gst_hst_registration_certificate"
    ],
    "mexico": [
        "rfc_tax_id_certificate",
        "constancia_de_situacion_fiscal"
    ],
    "brazil": [
        "cnpj_registration_certificate",
        "state_tax_registration_certificate"
    ],
    "argentina": [
        "cuite_tax_identification",
        "afip_registration_certificate"
    ],
    "chile": [
        "rut_tax_id_certificate",
        "commercial_registry_extract"
    ],

    # ---------------- MIDDLE EAST & AFRICA ----------------
    "united_arab_emirates": [
        "trade_license",
        "vat_registration_certificate"
    ],
    "saudi_arabia": [
        "commercial_registration_certificate",
        "vat_certificate"
    ],
    "qatar": [
        "commercial_registration_certificate",
        "tax_card"
    ],
    "egypt": [
        "tax_card_certificate",
        "commercial_register_certificate"
    ],
    "south_africa": [
        "company_registration_certificate",
        "tax_clearance_certificate"
    ],
    "nigeria": [
        "cac_certificate_of_incorporation",
        "tin_tax_identification_number"
    ],
    "kenya": [
        "certificate_of_incorporation",
        "kra_pin_certificate"
    ],
    "ghana": [
        "business_registration_certificate",
        "tax_identification_certificate"
    ],
    "morocco": [
        "patente_certificate",
        "tax_identification_number_certificate"
    ],

    # ---------------- OTHER REGIONS ----------------
    "new_zealand": [
        "nzbn_registration_certificate",
        "gst_registration_certificate"
    ],
    "turkey": [
        "trade_registry_gazette",
        "tax_certificate"
    ],
    "pakistan": [
        "ntn_certificate",
        "sales_tax_registration_certificate"
    ],
    "bangladesh": [
        "trade_license",
        "vat_registration_certificate"
    ],
    "sri_lanka": [
        "brc_business_registration_certificate",
        "vat_registration_certificate"
    ],
    "nepal": [
        "pan_registration_certificate",
        "business_registration_certificate"
    ]
}

# ---------------- BASIC SANCTIONS SIMULATION ----------------
BASIC_SANCTIONS_LIST = {
    "North Korean Mining Co": "UN-designated entity",
    "ACME Terror Finance": "US OFAC SDN",
    "XYZ Importers Iran": "EU Sanctions Entity",
    "Pyongyang Industrial Metals": "UN Listed Entity",
    "Sudan Gold Traders": "OFAC Restricted Party",
    "Syrian Defense Export Ltd": "EU & UN Arms Embargo Entity"
}
