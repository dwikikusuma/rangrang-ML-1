"""
Convert saved_model tensorflow to tflite

Usage :
  python convert_tflite.py -m [SAVED-MODEL PATH] [PARAMS]

Parameters:
  -m : Path to 'saved_model' folder
  -o : Pathlike to export tflite model

RangRang - Machine Learning - 2021
"""

import argparse
import tensorflow as tf

def convert(model_dir, export):
  # Convert the model
  converter = tf.lite.TFLiteConverter.from_saved_model(model_dir) 
  converter.optimizations = [tf.lite.Optimize.DEFAULT]
  converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS]
  tflite_model = converter.convert()

  # Save the model.
  with open(export, 'wb') as f:
    f.write(tflite_model)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Convert saved_model tensorflow to tflite")
  parser.add_argument("-m", 
                      "--model_dir",
                      help="Path to 'saved_model' folder",
                      type=str)
  parser.add_argument("-o", 
                      "--export",
                      help="Pathlike to export tflite model",
                      type=str)
  args = parser.parse_args()
  
  if args.export is None:
    args.export = './detect.tflite'

  convert(args.model_dir, args.export)
