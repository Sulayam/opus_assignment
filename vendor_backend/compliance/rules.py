# compliance/rules.py
from typing import Dict, List

POLICY_CATALOG: Dict[str, List[str]] = {
    "universal": [
        "vendor_master_form"
    ],
    "singapore": [
        "gst_registration_certificate",
        "acra_business_registration_certificate"
    ],
    "australia": [
        "abn_registration_certificate",
        "gst_registration_evidence"
    ],
    # add more countries here…
}

BASIC_SANCTIONS_LIST = {
    "North Korean Mining Co": "UN-designated entity",
    "ACME Terror Finance": "US OFAC SDN"
}
