# compliance/engine.py
from datetime import datetime
from slugify import slugify
from typing import Dict, Any
from .rules import POLICY_CATALOG, BASIC_SANCTIONS_LIST
from .models import insert_compliance_log

def normalize_country(country: str) -> str:
    """Lowercase + slugified for consistent lookup."""
    return slugify(country or "")

def required_docs_for_country(country: str) -> Dict[str, Any]:
    key = normalize_country(country)
    return {
        "country": country,
        "required_documents": POLICY_CATALOG.get(key, []) + POLICY_CATALOG["universal"]
    }

def basic_sanctions_check(company_name: str) -> Dict[str, Any]:
    if company_name in BASIC_SANCTIONS_LIST:
        return {
            "passed": False,
            "reason": BASIC_SANCTIONS_LIST[company_name]
        }
    return {"passed": True}

def run_compliance(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    payload = {
        "vendor_id": "...",
        "company_name": "...",
        "country": "...",
        "check_type": "basic_sanctions",
        "requested_at": "ISO-timestamp"
    }
    """
    company = payload["company_name"]
    country = payload["country"]
    policy = payload.get("check_type", "basic_sanctions")

    sanctions_result = basic_sanctions_check(company)
    docs_required = required_docs_for_country(country)

    final_result = {
        "vendor_id": payload["vendor_id"],
        "company_name": company,
        "country": country,
        "policy_code": policy,
        "passed": sanctions_result["passed"],
        "details": {
            "sanctions": sanctions_result,
            "documents": docs_required
        },
        "checked_at": datetime.utcnow().isoformat()
    }

    # Persist log
    insert_compliance_log(final_result)
    return final_result
