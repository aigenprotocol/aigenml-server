import os

UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")
MODEL_ALLOWED_EXTENSIONS = {'h5'}
IMAGE_ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg', 'gif'}
MODELS_DIR = os.environ.get("MODELS_DIR")
