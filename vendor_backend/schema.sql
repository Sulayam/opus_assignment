CREATE TABLE IF NOT EXISTS vendors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_id TEXT UNIQUE,
    vendor_company_name TEXT NOT NULL,
    requestor_email TEXT NOT NULL,
    country TEXT,
    annual_spend REAL,
    payment_terms INTEGER,
    created_at TEXT,
    status TEXT
);


CREATE TABLE IF NOT EXISTS workflow_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_id TEXT,
    vendor_company_name TEXT,
    requestor_email TEXT,
    missing_fields TEXT,
    status TEXT,
    workflow_requestor_email TEXT,
    timestamp TEXT,
    details TEXT
);


CREATE TABLE IF NOT EXISTS compliance_logs (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_id         TEXT,
    company_name      TEXT,
    country           TEXT,
    policy_code       TEXT,      -- e.g. "basic_sanctions"
    passed            INTEGER,   -- 1 = pass, 0 = fail
    details           TEXT,      -- free-form JSON blob
    checked_at        TEXT
);