# app/competitions.py
from app.openai_client import get_chat_completion

def run_competition(prompt: str, variations: list[str]) -> dict:
    """
    Run multiple completions with different system prompts (or styles).
    Return a dict of variation → output.
    """
    results = {}
    for style in variations:
        output = get_chat_completion(prompt, system_prompt=style)
        results[style] = output.strip()
    return results
