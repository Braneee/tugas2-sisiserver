````md
# Simple LMS

## Deskripsi Project

Simple LMS merupakan project berbasis **Django** yang dijalankan menggunakan **Docker** dan **PostgreSQL** sebagai database. Project ini dibuat untuk memenuhi kebutuhan setup environment development dengan pendekatan containerization sehingga proses instalasi, konfigurasi, dan menjalankan aplikasi menjadi lebih konsisten serta mudah direplikasi.

## Learning Objectives

Project ini dibuat dengan tujuan untuk:

1. Memahami konsep **containerization** menggunakan Docker.
2. Mampu membuat dan mengonfigurasi **Dockerfile** serta **docker-compose.yml**.
3. Melakukan setup project **Django** dengan struktur yang rapi dan sesuai best practice.
4. Menghubungkan aplikasi Django dengan **PostgreSQL** yang berjalan di dalam container Docker.

## Project Structure

```bash
simple-lms/
├── docker-compose.yml
├── Dockerfile
├── .env
├── .env.example
├── requirements.txt
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md
```
````

## Teknologi yang Digunakan

- **Python**
- **Django**
- **PostgreSQL**
- **Docker**
- **Docker Compose**

## Konfigurasi Services

Project ini menggunakan dua service utama pada Docker Compose, yaitu:

### 1. Web

Service **web** digunakan untuk menjalankan aplikasi Django.

### 2. Database

Service **db** digunakan untuk menjalankan database PostgreSQL sebagai media penyimpanan data aplikasi.

## Environment Variables

Konfigurasi environment disimpan pada file `.env.example`.

### Contoh Isi File `.env.example`

```env
DEBUG=True
SECRET_KEY=django-insecure-change-this-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:postgres@database:5432/lms_db
REDIS_URL=redis://redis:6379/0
```

### Penjelasan Environment Variables

- **DEBUG**
  Digunakan untuk mengaktifkan mode debug pada Django.

- **SECRET_KEY**
  Kunci rahasia yang digunakan oleh Django untuk kebutuhan keamanan aplikasi.

- **ALLOWED_HOSTS**
  Berisi daftar host yang diizinkan untuk mengakses aplikasi Django.

- **POSTGRES_DB**
  Nama database PostgreSQL yang digunakan oleh aplikasi.

- **POSTGRES_USER**
  Username untuk mengakses database PostgreSQL.

- **POSTGRES_PASSWORD**
  Password untuk autentikasi database PostgreSQL.

- **POSTGRES_HOST**
  Host database PostgreSQL. Pada Docker Compose, nilainya menggunakan nama service database yaitu `db`.

- **POSTGRES_PORT**
  Port yang digunakan PostgreSQL, secara default adalah `5432`.

## Konfigurasi Database Django

Project ini menggunakan PostgreSQL sebagai database utama. Konfigurasi database pada Django terdapat di file `config/settings.py`.

Contoh konfigurasi:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "simple_lms_db"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}
```

Konfigurasi tersebut memungkinkan Django terhubung dengan database PostgreSQL yang berjalan pada container `db`.

## Konfigurasi Static Files

Static files pada project ini dikonfigurasikan pada file `config/settings.py` sebagai berikut:

```python
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Konfigurasi ini digunakan agar file statis seperti CSS, JavaScript, dan gambar dapat dikelola dengan baik pada project Django.

## Cara Menjalankan Project

Berikut langkah-langkah untuk menjalankan project:

### 1. Clone Repository

```bash
git clone https://github.com/Braneee/tugas2-sisiserver.git
cd tugas2-sisiserver
```

### 2. Build Docker Image

```bash
docker compose build
```
![20de4178-c830-4f33-bada-0b0af98f914a](https://github.com/user-attachments/assets/09c3cc37-ec24-4e6c-a067-5b860ce8127d)

### 3. Jalankan Container

```bash
docker compose up
```
![83c8c338-4c6c-41c9-8891-cd1947595149](https://github.com/user-attachments/assets/9c7d0c6a-de8b-4e58-8771-808c50a9d0e4)

### 4. Akses Aplikasi

Setelah container berjalan dengan baik, aplikasi dapat diakses melalui browser pada alamat berikut:

```bash
http://localhost:8000
```

## Cara Menghentikan Project

Untuk menghentikan seluruh container, gunakan perintah:

```bash
docker compose down
```

![d89a042b-c439-431d-b1f6-63b575851bb1](https://github.com/user-attachments/assets/558d3d8f-5fd6-4fbb-b355-052d8e3d8679)

Apabila ingin sekaligus menghapus volume yang digunakan, jalankan:

```bash
docker compose down -v
```

## Hasil yang Diharapkan

Jika seluruh konfigurasi berhasil dijalankan, maka hasil yang diharapkan adalah:

1. Docker Compose dapat berjalan tanpa error.
2. Service PostgreSQL berhasil aktif dan menerima koneksi.
3. Aplikasi Django dapat diakses melalui `http://localhost:8000`.
4. Koneksi antara Django dan PostgreSQL berjalan dengan baik.
5. Struktur project sesuai dengan ketentuan yang diberikan.

## Screenshot Django Welcome Page

![1bcf423d-11de-4c15-811f-413853559dcf](https://github.com/user-attachments/assets/5c2cbdaa-febf-481e-ae6c-6e747a81c47f)

## Kesimpulan

Project Simple LMS ini menunjukkan implementasi dasar setup environment development menggunakan Docker pada aplikasi Django dengan PostgreSQL. Dengan menggunakan Docker Compose, proses menjalankan aplikasi dan database menjadi lebih terstruktur, konsisten, dan mudah digunakan pada berbagai environment development.
