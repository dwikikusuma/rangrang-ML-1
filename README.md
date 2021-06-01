# ML side of RangRang

Bagian pembelajaran mesin dari project capstone bangkit tim `uwuwu` -> `RangRang`

![Logo](assets/logo.jpeg)

## To Do

1. Mencari data untuk `object detection` & `color detection`
2. Membuat model menggunakan `tensorflow`<br>
   Model yang harus di buat:
   1. object detection model
   2. color detection model
3. Convert Model ke `TFLite`
4. Merancang skema dan ekosistem saat model di deploy di aplikasi<br>
   Kalau bisa sistemnya sudah di buat agar anak android tinggal ngurus UIny.

## Update on Object Detection Model

1. Karena harus ada custom trainingnya maka model akan di fine tune dengan dataset baru menggunakan tensorflow object detection library
2. link google colab [ssd mobilenet v2](https://colab.research.google.com/drive/1Ja64uMfznUTYkf2aDoeT3nSKJzVG66Kq?usp=sharing)
3. link google colab 2 [RangRang-ML](https://colab.research.google.com/drive/1y35rdQ02BWiMvyiHE-5zA9kQg8yCnZCC?usp=sharing)

### Note

- dia ngedetect nya general banget kaya kursi,tv,potted plant
- kalo mau nambha lebel kayanya tinggal masukin di label index terus di train deh kemaren nonotn di sini [youtube](https://www.youtube.com/watch?v=K0eDKO13O_s)

## Update on Color Detection Model

1. Perlu cari dataset yang mengandung benda dan warnanya sebagai label dari benda tsb.<br>
   Kalau jeleknya gak nemu datanya di internet berarti kita cari sendiri datanya.
   
## Sumber Bacaan

1. [Object Detection API with TensorFlow 2](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md)
2. [Training Custom Object Detector](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)
3. Transfer Learning Object detection model - [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
4. [Running TF2 Detection API Models on mobile](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tf2.md)
5. [Real-time Object Detection using SSD MobileNet V2 on Video Streams](https://heartbeat.fritz.ai/real-time-object-detection-using-ssd-mobilenet-v2-on-video-streams-3bfc1577399c)
6. [color detection](https://towardsdatascience.com/image-color-identification-with-machine-learning-and-image-processing-using-python-f3dd0606bdca)
7. [color detection 2](https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71)

### Image Downloader

Download image dari google image dengan query yang bisa di atur di `workspace\training_demo\scripts\query.json` dengan cara

1. Install `google-image-downloader` library
   ```
   git clone https://github.com/Joeclinton1/google-images-download.git
   cd google-images-download 
   python setup.py install
   ```
2. Run `image_downloader.py`
   ```
   python workspace/training_demo/scripts/image_downloader.py
   ```

Setelah itu hasil download akan terdapat pada folder `downloads`

**Note**

Untuk jumlah `limit > 100` download `chromedriver` [di sini](https://sites.google.com/a/chromium.org/chromedriver/downloads) lalu extract pada suatu folder. Lalu run `image_downloader.py` dengan argumen `-c`. Contoh

```
python workspace/object_detection/scripts/image_downloader.py -c C:/tools/chromedriver/chromedriver.exe
```