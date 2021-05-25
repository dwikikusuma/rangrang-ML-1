# ML side of RangRang

Bagian pembelajaran mesin dari project capstone bangkit tim `uwuwu` -> `RangRang`

![Karena belum ada logo jadi anggap aja ada logonya :v]()

## To Do

1. Mencari dataset untuk `color detection`
2. Membuat model menggunakan `tensorflow`<br>
   Model yang harus di buat:

   1. color detection model
3. Convert Model ke `TFLite`
4. Merancang skema dan ekosistem saat model di deploy di aplikasi<br>
   Kalau bisa sistemnya sudah di buat agar anak android tinggal ngurus UIny.

## Update on Object Detection Model

1. Kayaknya modelnya udah gk perlu di train lagi pake data `coco` karena emang udah di sediain model objetc detection dari tensorflownya yang udah di latih sebelumnya di data itu.
2. Tinggal ubah bentuknya jadi `.tflite` supaya lebih ringkas baik size nya dan biar bisa di deploy di android
3. Cuman untuk model object detection perlu perlakuan khusus buat ngubah jadi `.tflite, bisa di baca [di sini](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tf2.md)
4. Evaluate label dari model `ssd-mobilenet-v2`. Labelnya bisa dilihat [di sini](https://gist.github.com/aallan/fbdf008cffd1e08a619ad11a02b74fa8)
5. link google colab [ssd mobilenet v2](https://colab.research.google.com/drive/1Ja64uMfznUTYkf2aDoeT3nSKJzVG66Kq?usp=sharing)
### Note
- dia ngedetect nya general banget kaya kursi,tv,potted plant
- kalo mau nambha lebel kayanya tinggal masukin di label index terus di train deh kemaren nonotn di sini [youtube](https://www.youtube.com/watch?v=K0eDKO13O_s)
## Update on Color Detection Model

1. Perlu cari dataset yang mengandung benda dan warnanya sebagai label dari benda tsb.<br>
   Kalau jeleknya gak nemu datanya di internet berarti kita cari sendiri datanya.
   
## Sumber Bacaan

1. Transfer Learning Object detection model - [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
2. [Running TF2 Detection API Models on mobile](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tf2.md)
3. [Real-time Object Detection using SSD MobileNet V2 on Video Streams](https://heartbeat.fritz.ai/real-time-object-detection-using-ssd-mobilenet-v2-on-video-streams-3bfc1577399c)
4. [color detection](https://towardsdatascience.com/image-color-identification-with-machine-learning-and-image-processing-using-python-f3dd0606bdca)
5. [color detection 2](https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71)

## Note

1. Tentuin transfer learning yang bakal di pake. -> `SSD Mobilenet` kayaknya bagus sih.
2. Buat model lewat transfer learning dan di train di publik dataset macem COCO dan semacemnya perlu di pilah dulu datanya berdasarkan labelnya, apakah object itu perlu ato enggak di masukkin ke dalam model.
3. Saat di deploy di android perlu pikirin apakah realtime detection atau ambil gambar terlebih dahulu lewat metode panorama lalu di lakukan deteksi.
