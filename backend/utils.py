import uuid
from datetime import datetime

def generate_id(prefix):
    return f"{prefix}#{str(uuid.uuid4())}"

def current_time():
    return datetime.utcnow().isoformat()