import uuid
from datetime import datetime


def generate_uuid():
    return str(uuid.uuid4())

def current_date():
    return datetime.now().strftime("%Y-%m-%d")


