import re

async def parse_document(text: str):

    cleaned_text = re.sub(
        r"\s+",
        " ",
        text
    )

    return {
        "cleaned_text": cleaned_text,
        "length": len(cleaned_text)
    }