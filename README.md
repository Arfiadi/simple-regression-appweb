# Aplikasi Web Regresi Linier Sederhana

Aplikasi web sederhana adalah proyek UTS mata kuliah pemrograman 3. Appweb sederhana ini memungkinkan pengguna untuk mengunggah file CSV yang berisi dua kolom data, melakukan analisis regresi linier sederhana di sisi server, dan memvisualisasikan data asli beserta garis trennya di sisi klien.

Proyek ini dibangun menggunakan:
* **Backend**: Python, Flask, Pandas, dan pustaka matriks kustom.
* **Frontend**: HTML, CSS, dan JavaScript (dengan Chart.js).
* **Containerization**: Docker dan Docker Compose.

## Prasyarat

* [Docker Desktop](https://www.docker.com/products/docker-desktop/) terinstal dan sedang berjalan di komputer Anda.

## Cara Menjalankan Aplikasi

1.  **Clone repositori ini:**
    ```bash
    git clone [URL-repositori-anda]
    ```

2.  **Navigasi ke direktori proyek:**
    ```bash
    cd simple-regression-appweb
    ```

3.  **Jalankan aplikasi dengan Docker Compose:**
    Buka terminal di direktori ini dan jalankan perintah berikut. Perintah ini akan membangun *image* dan memulai *container* untuk backend dan frontend.
    ```bash
    docker-compose up --build
    ```

4.  **Akses Aplikasi:**
    Setelah proses build selesai dan server berjalan, buka browser Anda dan kunjungi:
    **`http://localhost:8080`**

## Cara Menggunakan

1.  Klik tombol **"Choose File"** dan pilih file `.csv` dari komputer Anda.
2.  Pastikan file CSV tersebut memiliki **tepat dua kolom** data numerik.
3.  Klik tombol **"Analyze"**.
4.  Hasil analisis berupa grafik dan persamaan regresi akan ditampilkan.
