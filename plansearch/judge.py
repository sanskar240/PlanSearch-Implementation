from utils.llm_client import call_llm
from plansearch.prompts import JUDGE_PROMPT

def score_jokes(jokes: list) -> list:
    scored = []

    for item in jokes:
        prompt = JUDGE_PROMPT.format(joke=item["joke"])
        raw = call_llm(prompt)  # default model

        score = extract_score_from_text(raw)
        item["score"] = score
        scored.append(item)

    return sorted(scored, key=lambda x: -x["score"])

def extract_score_from_text(text: str) -> int:
    for word in text.split():
        if word.strip().isdigit():
            val = int(word.strip())
            if 1 <= val <= 10:
                return val
    return 0
