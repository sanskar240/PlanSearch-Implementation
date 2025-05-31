from utils.llm_client import call_llm

def execute_plans(topic: str, plans: list) -> list:
    jokes = []

    for plan in plans:
        prompt = f"Write a joke using this plan: '{plan}', about the topic: '{topic}'. Keep it short and punchy."
        joke = call_llm(prompt)
        jokes.append({"plan": plan, "joke": joke.strip()})

    return jokes
