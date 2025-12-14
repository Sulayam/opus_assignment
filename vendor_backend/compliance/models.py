# compliance/models.py
from database import get_connection
import json

def insert_compliance_log(entry):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("""
        INSERT INTO compliance_logs (
            vendor_id,
            company_name,
            country,
            policy_code,
            passed,
            details,
            checked_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        entry["vendor_id"],
        entry["company_name"],
        entry["country"],
        entry["policy_code"],
        1 if entry["passed"] else 0,
        json.dumps(entry["details"]),
        entry["checked_at"]
    ))
    conn.commit()
    conn.close()
