from database import get_connection
import json

def insert_log(log_entry: dict):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO workflow_logs (
            vendor_company_name,
            requestor_email,
            missing_fields,
            status,
            workflow_requestor_email,
            timestamp
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        log_entry.get("vendor_company_name"),
        log_entry.get("requestor_email"),
        json.dumps(log_entry.get("missing_fields", [])),
        log_entry.get("status"),
        log_entry.get("workflow_requestor_email"),
        log_entry.get("timestamp")
    ))

    conn.commit()
    conn.close()


def insert_vendor(vendor: dict):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO vendors (
            vendor_id,
            vendor_company_name,
            requestor_email,
            country,
            annual_spend,
            payment_terms,
            created_at,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        vendor.get("vendor_id"),
        vendor.get("vendor_company_name"),
        vendor.get("requestor_email"),
        vendor.get("country"),
        vendor.get("annual_spend"),
        vendor.get("payment_terms"),
        vendor.get("created_at"),
        vendor.get("status")
    ))

    conn.commit()
    conn.close()


def find_vendor_by_name(name: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM vendors
        WHERE LOWER(vendor_company_name) = LOWER(?)
    """, (name,))

    row = cur.fetchone()
    conn.close()
    return row
