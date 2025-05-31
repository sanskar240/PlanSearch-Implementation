PLAN_PROMPT = """You are a professional joke writer. 
List {n} different humorous plans, formats, or angles for telling a joke about the topic: '{topic}'.
Each plan should describe a different humorous idea — such as a pun, absurd situation, dark twist, or observational setup.
Just list the ideas, not full jokes."""

JUDGE_PROMPT = """You are a professional comedy critic.

Rate the following joke on a scale of 1 (not funny) to 10 (very funny).
Focus on creativity, timing, and surprise. Return only a number.

Joke: "{joke}"
Rating:"""
