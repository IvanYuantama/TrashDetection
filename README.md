# Trash Detection 
![image](https://github.com/user-attachments/assets/83a29fdb-a6e6-4cb4-8bcc-cfcd3a7b1b75)

![image](https://github.com/user-attachments/assets/427e777b-d98f-493d-b6b7-e585d8739405)

Proyek ini adalah sebuah sistem deteksi objek yang dapat membedakan antara sampah **organik** dan **anorganik** secara *real-time* menggunakan kamera atau dari gambar yang diunggah. Proyek ini dibangun menggunakan **Python** dan *framework* **Flask**, dengan model *machine learning* yang dilatih untuk mengenali berbagai jenis sampah.

Dataset : https://universe.roboflow.com/siscer-project/sampah-organik-dan-anorganik/dataset/4

## 📜 Deskripsi Proyek

Tujuan utama dari proyek ini adalah untuk menyediakan alat sederhana yang dapat membantu dalam proses pemilahan sampah. Dengan memanfaatkan teknologi *computer vision*, sistem ini dapat secara otomatis mengidentifikasi dan mengklasifikasikan sampah, yang pada akhirnya dapat membantu meningkatkan efisiensi proses daur ulang.

***

## ✨ Fitur Utama

* **Deteksi Real-Time**: Mampu mendeteksi sampah organik dan anorganik langsung dari *feed* kamera.
* **Unggah Gambar**: Pengguna dapat mengunggah gambar untuk dianalisis.
* **Antarmuka Web Sederhana**: Antarmuka pengguna yang mudah digunakan, dibangun dengan HTML, CSS, dan JavaScript.
* **Model Kustom**: Menggunakan model deteksi objek yang telah dilatih secara khusus pada *dataset* sampah.

***

## 💻 Teknologi yang Digunakan

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS, JavaScript
* **Machine Learning**: Model deteksi objek (kemungkinan besar berbasis YOLO atau sejenisnya, dilihat dari file `best.pt`)

***

## 🚀 Cara Menjalankan Proyek

Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

1.  **Clone Repositori**
    ```bash
    git clone [https://github.com/IvanYuantama/TrashDetection.git](https://github.com/IvanYuantama/TrashDetection.git)
    cd TrashDetection
    ```

2.  **Instal Dependensi**
    Pastikan Anda memiliki Python dan pip terinstal. Kemudian, jalankan perintah berikut untuk menginstal semua *library* yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan Aplikasi**
    Setelah instalasi selesai, jalankan aplikasi Flask dengan perintah:
    ```bash
    python app.py
    ```

4.  **Akses Aplikasi**
    Buka *browser* web Anda dan kunjungi `http://127.0.0.1:5000` untuk mulai menggunakan aplikasi.

***
