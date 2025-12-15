import sqlite3
from pathlib import Path

DB_FILE = Path("vendor_master.db")

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def _column_exists(conn: sqlite3.Connection, table: str, column: str) -> bool:
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    cols = [row[1] for row in cur.fetchall()]
    return column in cols

def _ensure_column(conn: sqlite3.Connection, table: str, column: str, col_type: str):
    if not _column_exists(conn, table, column):
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")

def init_db():
    with open("schema.sql", "r") as f:
        schema = f.read()

    conn = get_connection()
    conn.executescript(schema)
    conn.commit()

    # ---- Minimal migrations for existing DBs ----

    # vendors table drift fixes
    _ensure_column(conn, "vendors", "vendor_id", "TEXT")
    _ensure_column(conn, "vendors", "status", "TEXT")

    # add uniqueness for vendor_id (SQLite can't add UNIQUE via ALTER TABLE)
    conn.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_vendors_vendor_id ON vendors(vendor_id)")
    conn.commit()

    # workflow_logs upgrades for richer event logging
    _ensure_column(conn, "workflow_logs", "vendor_id", "TEXT")
    _ensure_column(conn, "workflow_logs", "details", "TEXT")
    conn.commit()

    conn.close()
