from plansearch.generator import generate_plans
from plansearch.executor import execute_plans
from plansearch.judge import score_jokes
from utils.logger import log_results

def main():
    print("Funniest Joke PlanSearch")
    topic = input("Enter a topic or concept (e.g., 'penguins', 'nodejs in a VM'): ").strip()

    print("\nGenerating joke plans...")
    plans = generate_plans(topic)

    print(f"{len(plans)} plans generated. Now writing jokes...")
    jokes = execute_plans(topic, plans)

    print("Scoring jokes with LLM-as-a-Judge...")
    scored_jokes = score_jokes(jokes)

    print("\nTop Funniest Jokes:")
    log_results(scored_jokes[:5])

if __name__ == "__main__":
    main()
