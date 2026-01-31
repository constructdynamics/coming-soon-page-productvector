import sqlite3
import os
from datetime import datetime
import secrets
import uuid

DB_API_PATH = os.path.join(os.path.dirname(__file__), "api_keys.db")

def api_key_generator():
	# Combine a UUID4 and a random hex string for high uniqueness
	unique_id = uuid.uuid4().hex
	random_part = secrets.token_hex(16)
	api_key = f"{unique_id}-{random_part}"
	return api_key

def init_api_db():
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	c.execute("""
		CREATE TABLE IF NOT EXISTS api_keys (
			api_key TEXT PRIMARY KEY,
			tokens INTEGER NOT NULL,
			last_paid_month TEXT NOT NULL,
			email TEXT
		)
	""")
	conn.commit()
	conn.close()

def create_api_key(api_key, tokens, email):
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	now_month = datetime.now().strftime("%Y-%m")
	c.execute("INSERT OR REPLACE INTO api_keys (api_key, tokens, last_paid_month, email) VALUES (?, ?, ?, ?)", (api_key, tokens, now_month, email))
	conn.commit()
	conn.close()

def get_api_key_info(api_key):
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	c.execute("SELECT tokens, last_paid_month FROM api_keys WHERE api_key=?", (api_key,))
	row = c.fetchone()
	conn.close()
	return row if row else None

def get_api_key_by_email(email):
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	c.execute("SELECT api_key, tokens, last_paid_month FROM api_keys WHERE email=?", (email,))
	row = c.fetchone()
	conn.close()
	return row if row else None

def update_api_key_tokens(api_key, tokens, last_paid_month):
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	c.execute("UPDATE api_keys SET tokens=?, last_paid_month=? WHERE api_key=?", (tokens, last_paid_month, api_key))
	conn.commit()
	conn.close()

def decrement_token(api_key):
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	c.execute("UPDATE api_keys SET tokens = tokens - 1 WHERE api_key=? AND tokens > 0", (api_key,))
	conn.commit()
	conn.close()


def reset_tokens(api_key):
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	c.execute("UPDATE api_keys SET tokens = 0 WHERE api_key=?", (api_key,))
	conn.commit()
	conn.close()

# Delete an API key by email
def delete_api_key_by_email(email):
	conn = sqlite3.connect(DB_API_PATH)
	c = conn.cursor()
	c.execute("DELETE FROM api_keys WHERE email = ?", (email,))
	conn.commit()
	conn.close()

# Utility: Create a test API key for manual testing
if __name__ == "__main__":
	test_key = "test-api-key-123"
	test_tokens = 5
	test_email = "test@example.com"
	create_api_key(test_key, test_tokens, test_email)
	print(f"Created test API key: {test_key} with {test_tokens} tokens.")

def is_valid_api_key(api_key):
    conn = sqlite3.connect(DB_API_PATH)
    c = conn.cursor()
    c.execute("SELECT api_key FROM api_keys WHERE api_key=?", (api_key,))
    row = c.fetchone()
    conn.close()
    return row is not None
