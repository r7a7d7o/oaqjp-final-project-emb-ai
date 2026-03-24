"""
Web server file for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main index page of the Emotion Detection application.

    Returns:
        str: Rendered HTML template ('index.html').
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Handle emotion detection requests via GET or POST methods.

    This function processes text input from users, detects emotions using the
    emotion_detector function, and returns formatted results or an error message
    if the input is invalid.

    Returns:
        str: Formatted string with emotion scores and dominant emotion, or an
        error message if the input is invalid.
    """
    if request.method == 'POST':
        text_to_analyze = request.form['text']
    else: # GET
        text_to_analyze = request.args.get('textToAnalyze', '')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Check if the result is valid (e.g., dominant_emotion is None or text is empty)
    if ('dominant_emotion' not in result
            or result['dominant_emotion'] is None
            or not text_to_analyze):
        return "Invalid text! Please try again!"

    # Format the response as per the customer's request, split for line length
    response = (
        f"""For the given statement, the system response is 
        'anger': {result['anger']}, 
        'disgust': {result['disgust']}, 
        'fear': {result['fear']},
        'joy': {result['joy']} and 
        'sadness': {result['sadness']}. 
        The dominant emotion is **{result['dominant_emotion']}**."""
    )
    return response

if __name__ == '__main__':
    # Run the Flask application on localhost:5000 in debug mode
    app.run(host='localhost', port=5000, debug=True)
