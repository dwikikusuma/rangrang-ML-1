"""
Script to rename image files

Usage :
    python renamer.py -d [PATH TO IMAGES FOLDER]

Parameters:
    -d : Path to image folder

RangRang - Machine Learning - 2021
"""

import os, argparse

def rename(images, img_dir):
    """ Rename image files """
    for i, image in enumerate(images):
        filename, extension = os.path.splitext(image)
        os.rename(os.path.join(img_dir, image), os.path.join(img_dir, f'{i}{extension}'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rename image file")
    parser.add_argument("-d", 
                        "--img_dir",
                        help="Path to image folder",
                        type=str)
    args = parser.parse_args()

    images = os.listdir(args.img_dir)

    # rename
    rename(images, args.img_dir)