"""
Flask server for emotion detection application.

This module provides routes to render the main page and
to analyze emotions from user-provided text using the
emotion_detector function.
"""

from flask import Flask, jsonify, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the main application page.

    Returns:
        str: Rendered HTML template.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Analyze emotions from the provided text input.

    Returns:
        Response: JSON response with emotion analysis or
        an error message for invalid input.
    """
    text_to_analyze = (
        request.args.get("textToAnalyze") or request.form.get("text")
    )

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
