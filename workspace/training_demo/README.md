```
python scripts/preprocessing/generate_tfrecord.py -x images/train -l annotations/label_map.pbtxt -o annotations/train.record
python scripts/preprocessing/generate_tfrecord.py -x images/test -l annotations/label_map.pbtxt -o annotations/test.record
```

```
python model_main_tf2.py --model_dir=models/model_aku --pipeline_config_path=models/model_aku/pipeline.config
```

```
python ../../research/object_detection/export_tflite_graph_tf2.py --pipeline_config_path models/model_aku/pipeline.config --trained_checkpoint_dir models/model_aku/ --output_directory exported-models
```

```
python scripts/convert_tflite.py -m exported-models/saved_model -o detect.tflite
```

```
python scripts/add_metadata.py -m detect.tflite -l label_map.txt -o detect.tflite
```