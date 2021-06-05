"""
Download image according to the query.json file

Usage :
    python image_downloader.py [PARAMS - OPTIONAL]

Parameters :
    -c : Path to executable chromedriver

RangRang - Machine Learning - 2021
"""

import os, json, argparse
from google_images_download import google_images_download

def download(arguments):
    """ Download image files according to query """
    response = google_images_download.googleimagesdownload()
    paths = response.download(arguments)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download images from google image")
    parser.add_argument("-c", 
                        "--chromedriver",
                        help="Path to executable chromedriver",
                        type=str)
    args = parser.parse_args()

    with open(f'{os.path.dirname(__file__)}/query.json') as f:
        arguments = json.load(f)

    if arguments['limit'] > 100:
        if args.chromedriver is not None:
            arguments['chromedriver'] = args.chromedriver
        else:
            raise KeyError('Jika limit > 100 harus menspesifikasikan chromedriver. Lihat README')
    
    download(arguments)