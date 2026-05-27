from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

import asyncio

router = APIRouter()

async def event_generator():

    messages = [
        "Analyzing SAP ticket...",
        "Checking issue severity...",
        "Generating AI summary...",
        "Preparing final response..."
    ]

    for message in messages:

        yield {
            "event": "message",
            "data": message
        }

        await asyncio.sleep(1)

@router.get("/stream")
async def stream():

    return EventSourceResponse(
        event_generator()
    )