from nrclex import NRCLex

def detect_strongest_emotion(text):
    # Create an NRCLex object for the input text
    text_object = NRCLex(text)

    print('\n', text_object.affect_dict)
    print('\n', text_object.raw_emotion_scores)

    # Get the dominant emotion
    dominant_emotion = text_object.top_emotions[0][0]

    return dominant_emotion

if __name__ == "__main__":
    # Example text for emotion detection
    sample_text = "This is whack i don't like you"

    # Perform emotion detection on the sample text
    strongest_emotion = detect_strongest_emotion(sample_text)

    print(strongest_emotion)