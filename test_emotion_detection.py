from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_dominant_emotion(self):
        test_param_dict = {
            "I am glad this happend" : "joy",
            "I am really mad about this" : "anger",
            "I feel disgusted just hearing about this" : "disgust",
            "I am so sad about this" : "sadness",
            "I am really afraid that this will happen" : "fear"
        }
        for k, v in test_param_dict.items():
            response = emotion_detector(k)
            # print(f'{k} : {v} -> {response}')
            self.assertEqual(response['dominant_emotion'], v)

unittest.main()