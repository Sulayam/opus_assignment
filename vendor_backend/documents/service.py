# documents/service.py

from documents.matrix import DOCUMENT_REQUIREMENTS

def get_required_documents(country: str) -> list[str]:
    """
    Returns the list of required documents for a given country.
    Universal documents always apply.
    """
    if not country:
        country = ""

    country_key = country.strip().upper()

    required = []

    # Always include universal docs
    required.extend(DOCUMENT_REQUIREMENTS.get("UNIVERSAL", []))

    # Add country-specific docs if present
    required.extend(DOCUMENT_REQUIREMENTS.get(country_key, []))

    return required
