from fastapi import APIRouter

router = APIRouter()

FAKE_TICKETS = {

    "INC001": {
        "title": "RFC Connection Timeout",
        "description": "Production SAP system unable to connect to RFC destination.",
        "priority": "HIGH"
    },

    "INC002": {
        "title": "Invoice Posting Failure",
        "description": "Users unable to post invoices in SAP FICO module.",
        "priority": "MEDIUM"
    },

    "INC003": {
        "title": "SAP Background Job Failure",
        "description": "Nightly background job failed during execution.",
        "priority": "HIGH"
    }
}

@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: str):

    return FAKE_TICKETS.get(
        ticket_id,
        {
            "error": "Ticket not found"
        }
    )