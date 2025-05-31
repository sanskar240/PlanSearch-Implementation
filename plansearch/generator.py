from plansearch.prompts import PLAN_PROMPT
from utils.llm_client import call_llm

def generate_plans(topic: str, n: int = 15) -> list:
    prompt = PLAN_PROMPT.format(topic=topic, n=n)
    raw_text = call_llm(prompt)

    lines = raw_text.strip().split("\n")
    plans = [line.lstrip("-•1234567890. ").strip() for line in lines if len(line.strip()) > 0]

    return plans
