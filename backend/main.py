from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="SAP Ticket Summarizer"
)


class TicketRequest(BaseModel):
    ticket: str


@app.get("/")
def home():
    return {
        "message": "SAP Ticket Summarizer Running"
    }


@app.post("/summarize")
async def summarize_ticket(data: TicketRequest):

    return {
        "summary": f"SAP issue detected for: {data.ticket}",
        "priority": "HIGH",
        "root_cause": "RFC timeout",
        "actions": [
            "Restart SAP Gateway",
            "Check SAP network connectivity"
        ]
    }