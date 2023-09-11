Link : https://bicycleinv-app.adaptable.app/main/

Nama    : Vincent Suhardi \
NPM     : 2206082505 \
Kelas   : PBP F

### Jelaskan bagaimana cara kamu mengimplementasikan __checklist__ di atas secara __step-by-step__ (bukan hanya sekedar mengikuti tutorial).

**1. Membuat proyek Django baru.** \
Langkah awal yang saya lakukan dalam memulai proyek ini adalah dengan membuat repositori (repo) GitHub baru. Setelah itu, inisiasi repo lokal pada komputer saya dengan menggunakan perintah `git init`. Sebelum saya memulai inisiasi proyek Django, _best practice_ yang perlu dilakukan adalah untuk mengaktifkan _virtual environment_ Python. Ini akan membantu memisahkan dependensi proyek ini dari proyek Django lainnya, memastikan keselamatan dan konsistensi pada proyek. Setelah _virtual environment_ aktif, langkah selanjutnya adalah menyiapkan komponen-komponen penting yang dibutuhkan untuk aplikasi dan menyimpannya dalam file bernama `requirements.txt`. File ini berisi daftar dependensi yang diperlukan untuk menjalankan proyek saya. Saya kemudian menginstal file yang berisikan dependensi-dependensi ini menggunakan perintah `pip install` milik Python. Setelah semua dependensi terinstal, saya menggunakan perintah `startproject` untuk membuat struktur direktori proyek Django yang sesuai dengan persiapan dependensi. Pada langkah selanjutnya, saya melakukan konfigurasi terhadap file `settings.py` dengan mengizinkan akses dari semua host agar proyek dapat diakses dengan lebih mudah pada tahap pengembangan awal. Kemudian saya membuat file `.gitignore` yang diletakkan pada direktori utama sekaligus repo lokal yang dihubungkan dengan repo pada GitHub. File ini berisikan pola-pola teks file/direktori untuk diabaikan. Akhirnya, saya melakukan push commit repo lokal untuk memperbarui komponen pada repo di GitHub.

**2. Membuat aplikasi dengan nama `main` pada proyek tersebut.** \
_Virtual environment_ tetap saya aktivasikan terlebih dahulu. Kemudian menggunakan script `manage.py` yang sudah berada di dalam direktori utama, saya menggunakan perintah `python manage.py startapp main` pada _command prompt_ untuk menginisiasi aplikasi `main` pada proyek. Untuk memberitahu proyek Django bahwa saya telah menginisiasi aplikasi yang baru, saya menambahkan `main` (nama aplikasi) pada list `INSTALLED_APPS` yang berada di `settings.py` direktori proyek.

**3. Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.** \
Pembuatan pola URL berada di `urls.py` pada direktori proyek `bicycleparts_inv`. Saya mengambil _method_ `include` dan `path` dari _library_ `django.urls` untuk membentuk pola URL dari aplikasi-aplikasi yang berada pada proyek. Pada kode `urls.py`, ditambahkan _method_ `path` pada list `urlpatterns` yang menerima dua argumen yaitu rute berupa `main/` dan juga pengarahan menggunakan `include` ke file `urls.py` yang berada pada direktori aplikasi `main` sebelumnya.

**4. Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.** \
**- `name` sebagai nama _item_ dengan tipe `CharField`.** \
**- `amount` sebagai jumlah _item_ dengan tipe `IntegerField`.** \
**- `description` sebagai deskripsi _item_ dengan tipe `TextField`.** \
Dalam tahap ini, saya mengisikan file `models.py` yang berfungsi sebagai bagian Model dari aplikasi. Pada file tersebut, saya mengimpor `models` terlebih dahulu dari _library_ `django.db`. Kemudian saya membuat model baru `Item` yang dibuat dengan membentuk suatu _class_ yang merupakan _subclass_ dari `models.Model`. Pada _class_ model yang telah dibuat, ditambahkan beberapa _field_ atau atribut untuk model sebagai berikut:
- `date_added` menggunakan atribut `DateField`.
- `name` menggunakan atribut `CharField`.
- `amount` menggunakan atribut `IntegerField`.
- `price` menggunakan atribut `IntegerField`.
- `description` menggunakan atribut `TextField`.

**5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.** \
Pada `views.py`, saya mengawali dengan mengimpor `render` dari _library_ `django.shortcuts` sebagai _method_ yang berfungsi untuk mengembalikan respons HTTP yang akan menampilkan _template_ yang sesuai. Di dalam fungsi ini, saya membuat _dictionary_ `context` yang berisikan beberapa data, yaitu `app_name` (nama aplikasi), `name` (nama saya), dan `class` (kelas mata kuliah PBP), untuk ditampilkan. Fungsi berakhir dengan memanggil _method_ `render` yang akan menampilkan `main.html` dengan data yang sesuai `context`. 

**6. Membuat sebuah _routing_ pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.** \
Pada file `urls.py` yang berada pada direktori aplikasi `main`, saya menambahkan pola URL pada list `urlpatterns` untuk aplikasi dengan menggunakan _method_ yang sama seperti pada `urls.py` pada direktori proyek, yaitu `path` dari _library_ `django.urls`. `path` di sini menerima tiga argumen berupa rute dari `views.py` yang merupakan _string_ kosong sebab berada di direktori yang sama, fungsi `show_main` yang sudah dibuat dalam file `views.py`, dan nama dari pola URL.

**7. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.** \
Setelah selesai melakukan konfigurasi, _commit_ dan _push_ terhadap proyek, saya menuju ke situs web Adaptable. Saya melakukan _sign-in_ terlebih dahulu untuk menghubungkan repo yang berada pada GitHub ke Adaptable. Kemudian saya memilih repo `bicycleparts-inv` sebagai repo proyek yang ingin di-_deploy_. Setelah itu, saya memilih beberapa opsi lainnya seperti `Python App Template` sebagai tipe _template_ dari proyek dan `PostgreSQL` sebagai _database management system_ yang akan digunakan oleh model dari aplikasi proyek. Terdapat juga beberapa konfigurasi yang saya lakukan seperti menyesuaikan versi Python, memasukkan perintah yang sesuai pada `Start Command`, yaitu `python manage.py migrate && gunicorn bicycleparts_inv.wsgi` khusus untuk proyek saya, dan juga mencentang bagian `HTTP Listener on Port`. Akhirnya, proyek akan di-_deploy_.