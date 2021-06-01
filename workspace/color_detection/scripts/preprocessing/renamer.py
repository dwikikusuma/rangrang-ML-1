import os
import argparse

DOWNLOAD_DIR = 'downloads'

def rename(images, img_dir):
    for i, image in enumerate(images):
        filename, extension = os.path.splitext(image)
        os.rename(os.path.join(img_dir, image), os.path.join(img_dir, f'{i}{extension}'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rename image file")
    parser.add_argument("-d", 
                        "--img_dir",
                        help="Image directory inside downloads folder",
                        type=str)
    args = parser.parse_args()

    img_dir = os.path.join(DOWNLOAD_DIR, args.img_dir)
    images = os.listdir(img_dir)

    # rename
    rename(images, img_dir)
