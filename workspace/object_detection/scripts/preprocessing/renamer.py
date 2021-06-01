import os
import argparse

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

    images = os.listdir(args.img_dir)

    # rename
    rename(images, args.img_dir)