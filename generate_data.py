import csv
import random

themes = {
    "fear": [
        "I was being chased by something unknown",
        "I was trapped in a dark room",
        "I was drowning in deep water",
        "I was falling endlessly",
        "Something was after me but I couldn’t run"
    ],
    "happiness": [
        "I was laughing with my friends",
        "I was flying through the sky",
        "I met someone I loved again",
        "I found a treasure chest full of gold",
        "Everyone around me was smiling"
    ],
    "sadness": [
        "I was alone in an empty house",
        "I was crying but no one could hear me",
        "Everything I loved disappeared",
        "It was raining and I was lost",
        "I said goodbye to someone I loved"
    ],
    "nostalgia": [
        "I was back in my old school",
        "I saw my childhood home again",
        "I met an old friend from years ago",
        "I played with my childhood toys",
        "I walked through familiar streets from the past"
    ],
    "freedom": [
        "I was flying over mountains",
        "I was running across open fields",
        "I was swimming in the ocean",
        "I climbed to the top of a tall cliff",
        "I felt like I could go anywhere"
    ],
    "surprise": [
        "I opened a door and saw something unexpected",
        "I was suddenly somewhere else",
        "Someone gave me an unexpected gift",
        "I woke up and realized I was dreaming",
        "Everything changed suddenly"
    ]
}

data = []
for theme, dreams in themes.items():
    for dream in dreams:
        data.append([dream, theme])
        # Add 3-4 variations of each dream
        for _ in range(3):
            variant = dream.replace("I", random.choice(["I", "Someone", "We", "They"]))
            data.append([variant, theme])

with open("dreams.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["dream_text", "theme"])
    writer.writerows(data)

print("Generated dreams.csv with", len(data), "entries!")