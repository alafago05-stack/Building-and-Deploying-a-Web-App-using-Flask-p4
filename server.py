"""
Flask web server for Emotion Detection Application.
Provides a web interface to analyze emotions in user text input.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """
    Receives text input, analyzes emotions using the Watson NLP API,
    and returns the formatted result or an error message.
    Returns:
        str: Formatted emotion analysis result or an error message.
    """
    text_to_analyze = request.form["textToAnalyze"]

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response["dominant_emotion"]

    # Handle invalid or blank input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]

    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_output


@app.route("/")
def index():
    """
    Renders the home page of the Emotion Detection web application.
    Returns:
        HTML page: The index.html file from the templates folder.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    