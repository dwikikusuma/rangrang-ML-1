import os, json
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

with open(f'{os.path.dirname(__file__)}/query.json') as f:
    arguments = json.load(f)

paths = response.download(arguments)