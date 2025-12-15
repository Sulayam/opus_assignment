# documents/service.py
from documents.matrix import DOCUMENT_REQUIREMENTS

def get_required_documents(country: str) -> list[str]:
    """
    Returns the list of required documents for a given country.
    Universal documents always apply.
    Case-insensitive and defaults safely to universal set.
    """
    if not country:
        country_key = ""
    else:
        country_key = country.strip().upper()

    required = []

    # Always include universal docs
    required.extend(DOCUMENT_REQUIREMENTS.get("UNIVERSAL", []))

    # Add country-specific docs if available
    if country_key in DOCUMENT_REQUIREMENTS:
        required.extend(DOCUMENT_REQUIREMENTS[country_key])

    return required
