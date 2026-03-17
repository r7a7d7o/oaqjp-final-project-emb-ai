import requests
import json


def emotion_detector(text_to_analyze: str) -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = post( url = url, headers = headers, json = input_json )
    
    return response

text = "I feel sad today."

response = emotion_detector(text)

print(response)