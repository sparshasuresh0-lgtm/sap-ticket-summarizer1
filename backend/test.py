import asyncio
from app.services.summary_service import summarize_ticket

result = asyncio.run(
    summarize_ticket(
        "SAP production RFC timeout issue"
    )
)

print(result)