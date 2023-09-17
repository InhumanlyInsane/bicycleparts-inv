Link : https://bicycleinv-app.adaptable.app/main/

Nama    : Vincent Suhardi \
NPM     : 2206082505 \
Kelas   : PBP F

## Tugas 2
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

### Buatlah bagan yang berisi _request_ client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
![Pipeline MVT](images/mvt_pipeline.png)

### Jelaskan mengapa kita menggunakan **_virtual environment_**? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan **_virtual environment_**?
Kita perlu menggunakan atau mengaktivasi _virtual environment_ ketika ingin mengembangkan suatu proyek agar perubahan yang kita lakukan terhadap sistem, seperti perubahan _dependencies_, tidak mempengaruhi _dependencies_ pada proyek. Contoh lain, bila kita ingin membuat beberapa proyek, kita harus mengaktivasi _virtual environment_ untuk masing-masing proyek agar perbedaan antara versi Python atau _dependencies_ yang dimiliki oleh setiap proyek tidak saling mempengaruhi satu dengan lainnya.

Aplikasi web berbasis Django tetap dapat dibuat tanpa menggunakan _virtual environment_, namun akan muncul beberapa konflik antara _dependencies_ dari berbagai macam proyek Django. Contohnya, pembuatan proyek tanpa menggunakan _virtual environment_ akan mengakibatkan suatu proyek menggunakan _dependencies_ yang sama dengan proyek lainnya atau yang berada pada sistem. Kita tentu tidak akan mengingat _dependencies_ apa saja yang kita butuhkan untuk proyek dan harus menggunakan semua _dependencies_ yang dibutuhkan dan yang tidak dibutuhkan. Jadi, meskipun proyek tetap dapat dikembangkan tanpa mengaktivasi _virtual environment_, tetapi akan sangat memperlambat pengerjaan.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC dibagi menjadi _Model_, _View_, dan _Controller_. Arsitektur ini dimulai dengan pengguna yang meminta _request_ terhadap _Controller_ terlebih dahulu. _Controller_ akan memproses _request_ data pengguna melalui _Model_ yang akan kemudian ditampilkan pada komponen _View_ dari arsitektur MVC.
- MVT dibagi menjadi _Model_, _View_, dan _Template_. Pengguna akan mengakses konfigurasi URL yang akan memberikan _request_ terhadap komponen _View_. Kemudian _View_ akan melakukan _query_ terhadap komponen _Model_ yang akan melakukan transaksi atau ekstraksi data dari suatu DBMS (_Database Management System_). Setelah _Model_ memperoleh data dari database, _Model_ akan mengirimkan _response_ kembali ke _View_ dan _View_ akan memilih _template_ tampilan yang sesuai dengan data yang diambil. Setelah _template_ ditentukan, bagian _Template_ dari arsitektur akan menampilkannya ke pengguna.
- MVVM dibagi menjadi _Model_, _View_, dan _View-Model_. Pada arsitektur ini, _View-Model_ bertindak sebagai perantara antara komponen _View_ dengan _Model_. _View_ memberitahu aksi dari pengguna kepada _View-Model_ dan kemudian berhubungan dengan _Model_ untuk mengambil atau menyimpan data. _View-Model_ juga bertanggung jawab atas _methods_, perintah, dan unsur-unsur lainnya yang menjaga keadaan dari _View_, mengambil data dari _Model_, dan menginisiasi suatu aksi pada _View_.

Perbedaan utama dari ketiganya adalah bagaimana komponen _Model_ dan _View_ saling terhubung untuk mengakses data dan menampilkan suatu tampilan bagi pengguna sesuai dengan data yang di-_query_.

## Tugas 3
### Apa perbedaan antara form `POST` dan `GET` dalam Django?
`POST` merupakan segala _request_ yang dapat menambahkan, menghapus, atau merubah keadaan pada server, contohnya penambahan data baru pada database. Sedangkan `GET` juga merupakan suatu _request_ tetapi hanya bertujuan untuk mengambil atau menerima data dan tidak melakukan perubahan terhadap server.

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
HTML merupakan suatu kerangka dari sebuah web di mana dalam konteks pengiriman data, HTML digunakan untuk menampilkan data melalui format penulisan yang sudah dibuat pada HTML. Sedangkan berkas XML dan JSON memiliki fungsi yang saman yaitu untuk menyimpan data yang diterima dari _request_ pengguna melalui HTML dan juga berfungsi untuk melakukan transmisi data kembali ke tampilan HTML. Perbedaan XML dan JSON berada pada struktur berkasnya di mana XML memiliki struktur seperti pohon dan JSON memiliki struktur _key-value pair_ seperti struktur data _dictionary_.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Berkas JSON menggunakan sintaks bahasa pemrograman _Javascript_ yang banyak digunakan oleh pengembang aplikasi web modern. JSON menyimpan data dalam bentuk array sehingga dapat melakukan transmisi data dengan lebih cepat dan juga memiliki struktur yang lebih mudah dibaca oleh pengguna dibandingkan dengan XML.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**1. Membuat input `form` untuk menambahkan objek model pada app sebelumnya.** \
Saya memulai dengan membuat berkas baru yang dinamakan `forms.py` pada direktori aplikasi `main` untuk membangun struktur yang dapat menerima input pengguna masuk ke dalam model aplikasi. Pada berkas tersebut, saya membuat kelas baru yang saya namakan `ItemForm`. Kelas ini merupakan subclass dari kelas `ModelForm` dari _library_ `django.forms` yang digunakan untuk membangun aplikasi yang memiliki database. Kemudian saya tambahkan kelas lagi di dalam kelas `ItemForm` yang dinamakan `Meta` yang bertujuan untuk mendefinisikan informasi (_metadata_) yang dapat diisikan pada _form_. Kelas `Meta` memiliki dua variabel yaitu variabel `model` yang menerima kelas model yang sudah dibuat sebelumnya di `models.py` dinamakan `Item` dan juga _fields_ atau data-data apa saja yang telah kita definisikan pada model.

**2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.** \
Saya memulai pembuatan fungsi dengan mengimpor beberapa _library_ dari Django, yaitu `HttpResponseRedirect`, `HttpResponse`, `reverse`, dan `serializers`. 

Untuk format HTML, saya membuat fungsi baru yang dinamakan `create_item` yang menerima parameter _request_. Fungsi ini bertujuan untuk membuat suatu formulir yang dapat menerima data baru dari _input_ pengguna dan diawali dengan pembuatan kelas `ItemForm` yang menerima parameter `request.POST` **atau** `None` untuk menerima _request_ data dari pengguna menggunakan metode `POST` yang dapat mengubah model aplikasi. Kemudian dilakukan validasi terhadap _object form_ yang telah dibuat dan bila valid maka akan disimpan isi data dari _form_ dan mengembalikan halaman web ke `main.html`. \

Untuk format XML dan JSON, saya membuat fungsi `show_xml` untuk tampilan XML dan `show_json` untuk tampilan JSON dari data yang sudah berada pada model database. Masing-masing fungsi tersebut mengambil seluruh data dari model dengan sintaks `Item.objects.all()` dan menggunakan fungsi `HttpResponse` dengan parameter `serializers.serialize` untuk men-_translate_ tampilan respons dari aplikasi menjadi dalam bentuk XML atau JSON.

Untuk format XML dan JSON by ID, saya membuat fungsi `show_xml_by_id` untuk format XML dan `show_json_by_id` untuk format JSON. Kedua fungsi ini menerima parameter _request_ dan `id` sebagai ID dari data yang ingin diakses. Fungsi berawal dengan pengambilan data menggunakan metode `.filter()` berdasarkan ID yang ingin diperoleh, selengkapnya `Item.objects.filter(pk=id)`. Sama dengan kedua fungsi `show_xml` dan `show_json` sebelumnya, fungsi-fungsi ini menggunakan fungsi `HttpResponse` dengan parameter `serializers.serialize` tetapi dengan data yang berdasarkan ID yang diinginkan.

**3. Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.**
Tahap ini dilakukan di dalam berkas `urls.py` di mana untuk setiap fungsi, akan ditambahkan sebuah URL menggunakan fungsi `path` dari _library_ `django.urls`. Setiap fungsi dari `views.py` akan diimpor ke dalam berkas ini dan masing-masing _path_ akan dimasukkan ke dalam _list_ `urlpatterns` dengan penjelasan dari setiap fungsi sebagai berikut:
- Fungsi `create_item` diberikan _path_ `create-item` dan nama `create_item`.
- Fungsi `show_xml` diberikan _path_ `xml/` dan nama `show_xml`.
- Fungsi `show_json` diberikan _path_ `json/` dan nama `show_json`.
- Fungsi `show_xml_by_id` diberikan _path_ `xml/<int:id>/` dan  nama `show_xml_by_id`.
- Fungsi `show_json_by_id` diberikan _path_ `json/<int:id>/` dan nama `show_json_by_id`.
`<int:id>` pada fungsi `show_xml_by_id` dan `show_json_by_id` merupakan sebuah _placeholder_ bagi ID XML/JSON yang ingin ditampilkan kepada pengguna.

### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
#### HTML Viewer
![HTML viewer](images/html_viewer.png)
#### XML Viewer
![XML viewer](images/xml_viewer.png)
#### JSON Viewer
![JSON viewer](images/json_viewer.png)
#### XML by ID Viewer
![XML by ID viewer](images/xmlid_viewer.png)
#### JSON by ID Viewer
![JSON by ID viewer](images/jsonid_viewer.png)