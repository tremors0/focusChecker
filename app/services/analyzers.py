import os
from watson_developer_cloud import VisualRecognitionV3
from .image_processor import transform_pil_image_to_image, transform_image_to_base64_string

API_KEY = 'iMRV-32K41RvrHxqTjLHYe1oyeUd_Zgp8UD_nKQPs6V6'
CLASSIFIER_ID = 'DefaultCustomModel_1266843186'
WATSON_VERSION = '2018-03-19'

visual_recognition = VisualRecognitionV3(WATSON_VERSION, iam_apikey=API_KEY)


def detect_faces(image):
    return visual_recognition.detect_faces(image).get_result()


def classify_images(images):
    result = []
    for image in images:
        data = {}
        img_data = transform_pil_image_to_image(image)
        filename = 'tmp.jpg'
        with open(filename, 'wb') as f:
            f.write(img_data)
        with open(filename, 'rb') as f:
            img_class = classify_attention(f)
            data['image'] = transform_image_to_base64_string(img_data)
            data['classes'] = img_class['images'][0]['classifiers'][0]['classes']
        if os.path.isfile(filename):
            os.remove(filename)
        result.append(data)
    return result


def classify_attention(image):
    return visual_recognition.classify(images_file=image, threshold=0, classifier_ids=[CLASSIFIER_ID]).get_result()

