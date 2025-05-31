# PlanSearch: LLM-Driven Joke Generator

This project implements a humor generation system using a structured
PlanSearch pipeline. Given a topic (e.g., "penguins", "Node.js in a
VM"), the system uses a large language model (via Groq API) to:

1.  Generate diverse joke plans (e.g., formats, setups, metaphors)
2.  Write jokes by executing each plan
3.  Score each joke's funniness using an LLM-as-a-judge strategy
    (ICL-based)
4.  Return the top-k funniest jokes

------------------------------------------------------------------------

## Why this project?

Humor is one of the hardest forms of generative language,insanely subjective,
nuanced, and deeply cultural. Instead of treating it as a black-box text
generation task, this project breaks humor into structured components
using PlanSearch. The pipeline is modular, inspectable, and aligns with
modern LLM evaluation research.
Felt like this was a good solution to better and more robust open-ended generation responses evaluation

------------------------------------------------------------------------

## Architecture Diagram

(See included PNG: PlanSearch architecture)

------------------------------------------------------------------------

## How it Works
<img width="348" alt="Screenshot 2025-05-31 at 11 06 05 AM" src="https://github.com/user-attachments/assets/3cabfdf8-bb03-4378-a5bd-f5bfa2608aac" />




  -----------------------------------------------------------------------
  Step                   Description
  ---------------------- ------------------------------------------------
  Topic Input            User enters a topic (e.g., "penguins" or "nodejs
                         in a VM")

  Plan Generator         Uses an LLM to brainstorm 10--20 humorous angles
                         (e.g., puns, satire, cultural references)

  Plan Executor          Each plan is used to generate a unique joke via
                         LLM

  LLM-as-a-Judge         A separate model call rates each joke from 1--10
                         using an in-context judging prompt

  Top-K Ranking          Jokes are sorted by score, and the top few are
                         returned
  -----------------------------------------------------------------------

All LLM calls are served via Groq's API, using the
`meta-llama/llama-4-scout-17b-16e-instruct` model.

------------------------------------------------------------------------

## Running Locally

1.  Clone the repo: git clone
    https://github.com/sanskar240/PlanSearch-Implementation.git cd
    PlanSearch-Implementation

2.  Set up environment: python -m venv venv source venv/bin/activate pip
    install -r requirements.txt

3.  Add your .env: GROQ_API_KEY=your-groq-api-key-here

4.  Run: python main.py

------------------------------------------------------------------------

## What I Learned

-   PlanSearch \> single-prompting: Generating jokes via structured
    planning outperforms direct prompting in both quality and diversity.
-   LLM-as-a-Judge is hard: Even with ICL, judging humor is noisy and
    requires bias-aware design (temperature control, position
    randomization).
-   Groq is fast, but still subject to rate-limiting constraints on free
    tier.

------------------------------------------------------------------------

## What Surprised Me

-   The semantic diversity in the generated joke plans far exceeded
    expectations.
-   Some jokes generated from silly-sounding plans turned out to be the
    most hilarious.
-   Even without fine-tuning, LLMs can simulate humor genres like dry
    wit, absurdism, and one-liners remarkably well.

------------------------------------------------------------------------

## If I Had More Time/Compute

-   Add a novelty detector to measure joke originality (embedding
    similarity to known jokes).
-   Try plan reranking before execution using few-shot prompts.
-   Use multi-model evaluation (judge with multiple LLMs and ensemble
    the score).
-   Run human evaluations to compare model scores vs. real-world
    funniness ratings.

------------------------------------------------------------------------

## If This Were a Paper

To elevate this into a research-grade submission, I'd: - Collect human
ratings for 1000+ LLM-generated jokes and benchmark PlanSearch
vs. baseline sampling. - Build a humor-style classifier to group plans
into categories and analyze diversity vs. quality tradeoffs. - Evaluate
novelty, style, and coherence separately using custom metrics. - Extend
to multilingual humor to test cultural transferability of PlanSearch.

------------------------------------------------------------------------

## Repo Contents

main.py \# Entry point plansearch/ \# Core pipeline modules (generator,
executor, judge) utils/ \# Logger + LLM wrapper (Groq) data/ \# Optional
saved jokes .env \# \[not tracked\] your GROQ_API_KEY goes here
.gitignore \# Standard Python + secrets requirements.txt \# requests,
dotenv PlanSearch architecture diagram (PNG)

------------------------------------------------------------------------

## Sample Run

Funniest Joke PlanSearch Enter a topic or concept: penguins

Generating joke plans... 10 plans generated. Now writing jokes...
Scoring jokes with LLM-as-a-Judge...

Top Funniest Jokes: 1. \[9/10\] Tony the Penguin isn't in IT, but he's
great at ice-breaking. Plan: Penguin as mafia hitman

<img width="1077" alt="Screenshot 2025-05-31 at 12 05 59 PM" src="https://github.com/user-attachments/assets/986e4b37-9d4a-42e7-a1d7-705f9443cd71" />



------------------------------------------------------------------------

Built by Sanskar Pandey Powered by LLaMA 4 Scout (Groq) and structured
generation logic.
