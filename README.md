# ML side of RangRang

Bagian pembelajaran mesin dari project capstone bangkit tim `uwuwu` -> `RangRang`

![Karena belum ada logo jadi anggap aja ada logonya :v]()

## To Do

1. Membuat model menggunakan `tensorflow`<br>
   Model yang harus di buat:

   1. Object detection model
   2. Color detection model
2. Convert Model ke `TFLite`
3. Merancang skema dan ekosistem saat model di deploy di aplikasi<br>
   Kalau bisa sistemnya sudah di buat agar anak android tinggal ngurus UIny.
   
## Sumber Bacaan

1. Transfer Learning Object detection model - [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
2. [Running TF2 Detection API Models on mobile](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tf2.md)
3. [Real-time Object Detection using SSD MobileNet V2 on Video Streams](https://heartbeat.fritz.ai/real-time-object-detection-using-ssd-mobilenet-v2-on-video-streams-3bfc1577399c)
4. dll

## Note

1. Tentuin transfer learning yang bakal di pake. -> `SSD Mobilenet` kayaknya bagus sih.
2. Buat model lewat transfer learning dan di train di publik dataset macem COCO dan semacemnya perlu di pilah dulu datanya berdasarkan labelnya, apakah object itu perlu ato enggak di masukkin ke dalam model.
3. Saat di deploy di android perlu pikirin apakah realtime detection atau ambil gambar terlebih dahulu lewat metode panorama lalu di lakukan deteksi.