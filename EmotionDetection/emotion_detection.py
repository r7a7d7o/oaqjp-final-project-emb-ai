import requests
import json
from pprint import pprint

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Emotion detector function  input string, output dictionary
    """
    # Connection variables
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Request
    response = requests.post( url = url, headers = headers, json = input_json )

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
    text = "I am so happy I am doing this."
    response = emotion_detector(text)
    print(response)