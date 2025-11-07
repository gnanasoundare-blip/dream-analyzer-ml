import joblib
import argparse

# Define interpretations
interpretations = {
    "anxiety": "Dreams of falling or being chased often reflect stress, fear, or anxiety in waking life.",
    "freedom": "Dreams of flying or open spaces reflect a desire for freedom, relief, or release.",
    "nostalgia": "Dreams of the past may suggest longing, unresolved emotions, or reflection.",
    "uncertainty": "Being lost or confused often mirrors uncertainty about decisions or life direction.",
    "fear": "Being chased or unable to escape typically indicates fear, avoidance, or pressure in your life.",
    "resilience": "Surviving storms or challenges reflects strength and growth after struggle.",
    "happy": "Joyful dreams often reflect satisfaction, gratitude, or emotional harmony.",
    "surprised": "Unexpected discoveries or odd events may show curiosity, or readiness for change."
}

def interactive_mode(model_dict, interpretations):
    # Extract model and vectorizer
    model = model_dict["model"]
    vectorizer = model_dict["vectorizer"]

    print("\nDream Analyzer (type 'quit' to exit)\n")

    while True:
        text = input("Describe your dream: ")
        if text.lower() == "quit":
            print("Goodbye! Sweet dreams 🌙")
            break

        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        confidence = max(model.predict_proba(vec)[0])

        meaning = interpretations.get(pred, "I have a hard time interpreting that theme yet.")
        print(f"\nPredicted theme: {pred}")
        print(f"Interpretation: {meaning}")
        print(f"Confidence: {confidence:.2f}\n---\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    args = parser.parse_args()

    model_dict = joblib.load(args.model)
    interactive_mode(model_dict, interpretations)


