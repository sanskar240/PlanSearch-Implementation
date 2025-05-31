import os, time, requests, json
from dotenv import load_dotenv
load_dotenv()

GROQ_URL   = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
    "Content-Type": "application/json"
}

def call_llm(prompt: str,
             model: str = GROQ_MODEL,
             temperature: float = 0.9,
             max_retries: int = 3) -> str:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    for attempt in range(max_retries):
        resp = requests.post(GROQ_URL, headers=HEADERS, json=payload)
        if resp.status_code == 200:
            return resp.json()["choices"][0]["message"]["content"].strip()

        # If rate-limited, Groq returns 429 with “Try again in … s”
        if resp.status_code == 429 or "rate_limit" in resp.text:
            try:
                wait = json.loads(resp.text)["error"]["message"]
                # Extract “1.659s”, take the number
                wait_secs = float("".join(ch for ch in wait if ch.isdigit() or ch=='.'))
            except Exception:
                wait_secs = 2.0
            time.sleep(wait_secs + 0.5)
            continue

        # Any other error → raise
        raise RuntimeError(f"Groq error {resp.status_code}: {resp.text}")

    raise RuntimeError("Max retries exceeded with Groq")
