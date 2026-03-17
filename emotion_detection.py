import requests
import json
from pprint import pprint

def emotion_detector(text_to_analyze: str) -> dict:
    # Connection variables
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Request
    response = requests.post( url = url, headers = headers, json = input_json )
    
    response_json = json.loads(response.text)
    response_dict = response_json['emotionPredictions'][0]['emotion']

    return response.text
    max_score = {
        'emotion_name': '',
        'emotion_score': 0
    }

    for key, value in response_dict:
        if value > max_score['emotion_score']:
            max_score['emotion_score'] = value
            max_score['emotion_name'] = key

    response_obj = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness'],
        'dominant_emotion': max_score['emotion_name']
    }

    return response_obj

if __name__ == "__main__":
    text = "I love this new technology."
    response = emotion_detector(text)
    print(response)