# scripts/run_competition.py
from app.competitions import run_competition

prompt = "Create a unique, refreshing non-alcoholic summer beverage using citrus and herbs."

variations = [
    "You are a creative mixologist.",
    "You are a health-conscious beverage consultant.",
    "You are a food scientist optimizing for taste and shelf life."
]

if __name__ == "__main__":
    results = run_competition(prompt, variations)

    for style, output in results.items():
        print(f"\n--- {style} ---\n{output}\n")
