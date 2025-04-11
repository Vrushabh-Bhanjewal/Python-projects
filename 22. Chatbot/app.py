
import random

greetings = ["Hello!", "Hi there!", "Hey!", "Howdy!", "Greetings!"]
farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!"]
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why was the math book sad? It had too many problems."
]
facts = [
    "Honey never spoils. Archaeologists have found edible honey in ancient tombs.",
    "Bananas are berries, but strawberries aren't.",
    "Octopuses have three hearts."
]
colors = ["Red", "Blue", "Green", "Purple", "Orange", "Turquoise"]


print("🤖 ChatBot")
print(' - Ask me for a joke\n - Fact\n - Color \n - Greeting\n - say bye to exit.\n')
while True:
    user = input("You: ").lower()

    if "joke" in user:
        print("ChatBot:", random.choice(jokes))
    elif "fact" in user:
        print("ChatBot:", random.choice(facts))
    elif "color" in user:
        print("ChatBot: My favorite color is", random.choice(colors))
    elif any(word in user for word in ["hi", "hello", "greet"]):
        print("ChatBot:", random.choice(greetings))
    elif "bye" in user:
        print("ChatBot:", random.choice(farewells))
        break
    else:
        print("ChatBot: I can tell you a joke, fact, color, or greet you!")
