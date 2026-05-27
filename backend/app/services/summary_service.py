from dotenv import load_dotenv
import os

load_dotenv()


async def summarize_ticket(ticket: str):

    return {
        "summary": f"SAP issue detected for: {ticket}",
        "priority": "HIGH",
        "root_cause": "RFC timeout",
        "actions": [
            "Restart SAP Gateway",
            "Check SAP network connectivity",
            "Validate RFC destination"
        ]
    }