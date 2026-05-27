import requests

BASE_URL = "http://127.0.0.1:8000"

def fetch_ticket(ticket_id: str):

    response = requests.get(
        f"{BASE_URL}/tickets/{ticket_id}"
    )

    return response.json()