import base64
import json


def encode_cursor(updated_at, id):
    payload = {
        "updated_at": updated_at.isoformat(),
        "id": id
    }
    return base64.b64encode(json.dumps(payload).encode()).decode()


def decode_cursor(cursor):
    if not cursor:
        return None

    return json.loads(base64.b64decode(cursor.encode()).decode())