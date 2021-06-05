"""
Script to add metadata to tflite model

Usage :
    python add_metadata.py -m [PATH TFLITE MODEL] -l [PATH TO LABEL.txt] [PARAMS]

Parameters :
    -m : Path to tflite model
    -l : Path to label.txt
    -o : Pathlike to export tflite model

RangRang - Machine Learning - 2021
"""

import argparse

from tflite_support.metadata_writers import object_detector
from tflite_support.metadata_writers import writer_utils
from tflite_support import metadata

MODEL_PATH = "detect.tflite"

def metadata_writer(model_path, label, export):
    ObjectDetectorWriter = object_detector.MetadataWriter
    writer = ObjectDetectorWriter.create_for_inference(
        writer_utils.load_file(model_path), [127.5], [127.5], [label]
    )
    writer_utils.save_file(writer.populate(), export)

    # Verify the populated metadata and associated files.
    displayer = metadata.MetadataDisplayer.with_model_file(export)
    print("Metadata populated:")
    print(displayer.get_metadata_json())
    print("Associated file(s) populated:")
    print(displayer.get_packed_associated_file_list())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Add metadata to tflite model")
    parser.add_argument("-m", 
                        "--model_path",
                        help="Path to tflite model",
                        type=str)
    parser.add_argument("-l", 
                        "--label_file",
                        help="Path to label.txt",
                        type=str)
    parser.add_argument("-o", 
                        "--export",
                        help="Pathlike to export tflite model",
                        type=str)
    args = parser.parse_args()
  
    if args.model_path is None:
        args.model_path = MODEL_PATH
    if args.export is None:
        args.export = MODEL_PATH

    metadata_writer(args.model_path, args.label_file, args.export)