CREATE TABLE IF NOT EXISTS vendors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_id TEXT UNIQUE,                      -- NEW: links back to Opus
    vendor_company_name TEXT NOT NULL,
    requestor_email TEXT NOT NULL,
    country TEXT,
    annual_spend REAL,
    payment_terms INTEGER,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS workflow_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_company_name TEXT,
    requestor_email TEXT,
    missing_fields TEXT,
    status TEXT,
    workflow_requestor_email TEXT,
    timestamp TEXT
);
