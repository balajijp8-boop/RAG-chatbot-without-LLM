def verify(chunk_text, claim_text):
    """
    Returns True if claim_text is in chunk_text
    """
    return claim_text.lower() in chunk_text.lower()
