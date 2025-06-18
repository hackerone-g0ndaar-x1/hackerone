import random

def get_random_joke():
    jokes = [
        {"setup": "Why don't scientists trust atoms?", "punchline": "Because they make up everything!"},
        {"setup": "Why did the scarecrow win an award?", "punchline": "Because he was outstanding in his field!"},
        {"setup": "Why don’t skeletons fight each other?", "punchline": "They don’t have the guts."},
        {"setup": "What do you call fake spaghetti?", "punchline": "An impasta!"},
        {"setup": "How does a penguin build its house?", "punchline": "Igloos it together."},
    ]

    joke = random.choice(jokes)
    return f"{joke['setup']}\n{joke['punchline']}"

if __name__ == "__main__":
    print("Here's a random joke for you:\n")
    print(get_random_joke())
