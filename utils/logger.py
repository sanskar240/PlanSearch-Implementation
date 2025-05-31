def log_results(jokes):
    for i, item in enumerate(jokes, 1):
        print(f"{i}. [{item['score']}/10] {item['joke']}")
        print(f"   Plan: {item['plan']}\n")
