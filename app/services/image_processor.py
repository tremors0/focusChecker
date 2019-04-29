from PIL import Image
from io import BytesIO
import base64


def crop_faces(img_file, faces_data):
    if len(faces_data["images"]) == 0:
        return {"status": "NO_FACE"}

    im = Image.open(img_file)
    faces = faces_data["images"][0]["faces"]
    cropped_images = []
    for face in faces:
        face_location = face["face_location"]
        height = face_location["height"]
        width = face_location["width"]
        left = face_location["left"]
        top = face_location["top"]
        cropped_images.append(im.crop((left, top, left + width, top + height)))
    return cropped_images


def transform_image_to_base64_string(image):
    return base64.b64encode(image).decode('ascii')


def transform_pil_image_to_image(image):
    buffered = BytesIO()
    # transform to RGB to support formats without alpha channel
    img_rgb = image.convert("RGB")
    img_rgb.save(buffered, format="JPEG")
    return buffered.getvalue()
