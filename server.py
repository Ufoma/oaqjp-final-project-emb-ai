"""Server module for the Emotion Detection Flask application.

This module sets up a Flask web server to handle emotion detection requests
using the EmotionDetection package. It serves an HTML interface and processes
text input to determine dominant emotions via the Watson NLP API.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index.html template as the main page.

    Returns:
        str: Rendered HTML content from the templates/index.html file.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """Handle GET requests to the /emotionDetector endpoint.

    Retrieves text to analyze from the query parameter 'textToAnalyze',
    processes it using the emotion_detector function, and returns a formatted
    response. Handles blank inputs and invalid API responses with an error message.

    Returns:
        str: Formatted string with emotion scores and dominant emotion, or
             error message if input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
