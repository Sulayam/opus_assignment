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

CREATE TABLE IF NOT EXISTS document_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_id TEXT,
    vendor_company_name TEXT,
    requestor_email TEXT,
    doc_contact_email TEXT,
    issue_type TEXT,              -- e.g. "missing_documents", "invalid_format", "incomplete_upload"
    issue_details TEXT,           -- free-form JSON
    status TEXT,                  -- e.g. "rejected", "pending_reupload"
    logged_at TEXT
);

CREATE TABLE IF NOT EXISTS document_file_storage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    documents_complete BOOLEAN,
    missing_documents TEXT, -- JSON-encoded list
    document_reviewer_notes TEXT,
    submitted_documents_file_out TEXT,
    document_reviewed_at TEXT -- ISO 8601 date format
);