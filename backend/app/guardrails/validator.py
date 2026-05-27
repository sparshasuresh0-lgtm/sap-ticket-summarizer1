BLOCKED_WORDS = [
    "password",
    "secret",
    "token",
    "private key"
]

def validate_ticket(text: str):

    for word in BLOCKED_WORDS:

        if word.lower() in text.lower():

            raise Exception(
                "Sensitive information detected"
            )

    return True