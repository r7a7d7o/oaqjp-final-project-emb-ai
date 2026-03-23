""" Emotion Detection """

import json
import requests

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Detects emotions in the provided text using an external NLP service.

    The function sends the input text to an emotion prediction API, retrieves
    scores for five emotions (anger, disgust, fear, joy, sadness), and
    determines the dominant emotion based on the highest score. If the API
    returns a 400 status code (e.g., due to blank input), a dictionary with
    all emotion values set to None is returned.

    Args:
        text_to_analyze (str): The text to be analyzed for emotional content.

    Returns:
        dict: A dictionary with the following keys:
            - 'anger' (float or None): anger score
            - 'disgust' (float or None): disgust score
            - 'fear' (float or None): fear score
            - 'joy' (float or None): joy score
            - 'sadness' (float or None): sadness score
            - 'dominant_emotion' (str or None): the emotion with the highest score,
              or None if no valid scores are available.

    Raises:
        Requests-related exceptions may be raised if the API call fails due to
        network issues, invalid URLs, etc. (not handled in this function).
    """

    # Connection variables
    url = 'https://sn-watson-emotion.labs.skills.network/v1/'
    url += 'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Request
    response = requests.post( url = url, headers = headers, json = input_json, timeout=5 )

    # Handling for empty request
    if response.status_code == 400:
        empty_dict = {
            "joy": None,
            "anger" : None,
            "disgust" : None,
            "sadness" : None,
            "fear"  : None,
            "dominant_emotion": None
        }
        return empty_dict

    # Traverse through json
    response_json = json.loads(response.text)
    response_dict = response_json['emotionPredictions'][0]['emotion']

    # Max score
    max_score = {
        'emotion_name': '',
        'emotion_score': 0
    }

    for key, value in response_dict.items():
        if value > max_score['emotion_score']:
            max_score['emotion_score'] = value
            max_score['emotion_name'] = key

    response_obj = {
        'anger': response_dict['anger'],
        'disgust': response_dict['disgust'],
        'fear': response_dict['fear'],
        'joy': response_dict['joy'],
        'sadness': response_dict['sadness'],
        'dominant_emotion': max_score['emotion_name']
    }
    return response_obj

if __name__ == "__main__":
    TEXT = "I am so happy I am doing this."
    answer = emotion_detector(TEXT)
    print(answer)
