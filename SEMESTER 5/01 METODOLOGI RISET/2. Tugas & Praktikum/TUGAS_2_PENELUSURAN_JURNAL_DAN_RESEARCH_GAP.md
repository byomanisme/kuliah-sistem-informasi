# LEMBAR TUGAS METODOLOGI RISET (TUGAS 2)
## Penelusuran Jurnal Ilmiah dan Identifikasi Research Gap untuk Proposal Skripsi

---

### 👤 IDENTITAS MAHASISWA
* **Nama Lengkap:** LUKMAN HAKIM
* **NIM:** 241011700845
* **Program Studi:** S1 Sistem Informasi
* **Kelas:** 05SIFM002 / Reguler B (Semester 5)
* **Mata Kuliah:** Metodologi Riset (`22SIF0283`)
* **Dosen Pengampu:** Ahmad Asep Suhendi, S.Kom., M.Kom.

---

### 📌 RENCANA JUDUL SKRIPSI (PROPOSAL PENELITIAN)
> **"Pengembangan Sistem Informasi Manajemen Shift dan Penggajian Pekerja Harian Lepas Berbasis Mobile Menggunakan Metode Rapid Application Development (Studi Kasus: Gudang Fulfillment Segari)"**

* **Objek / Kasus Penelitian:** Gudang Fulfillment Segari (Rantai Pasok Logistik E-Grocery)
* **Target Pengguna:** Tenaga Kerja Harian Lepas (*Daily Worker* / *Warehouse Crew*) & Tim Operasional HR Gudang
* **Metode Rekayasa Sistem:** *Rapid Application Development* (RAD)
* **Arsitektur Solusi:** Mobile Application (*Offline-First* dengan SQLite & Cloud RESTful API Synchronization)

---

## 📑 BAGIAN I: ANALISIS MENDALAM 5 JURNAL ILMIAH TERKAIT

Berikut adalah hasil telaah literatur terhadap 5 jurnal ilmiah nasional dan terakreditasi terkini (2024–2026) yang memiliki keterkaitan langsung dengan pilar topik penelitian:

---

### 1. Jurnal 1: Penerapan Metode RAD pada Aplikasi Mobile Presensi
1. **Judul Penelitian:** *Analisis Metode Rapid Application Development untuk Aplikasi Absensi di Android*
2. **Nama Penulis:** A. O. A. Octaviano, S. Sofiana, dan M. R. Arrahman
3. **Tahun Publikasi:** 2025
4. **Sumber / Jurnal Publikasi:** *Kohesi: Jurnal Sains dan Teknologi*, Vol. 9, No. 12, Hal. 51–60.
5. **Permasalahan yang Diteliti:** Siklus pengembangan aplikasi absensi mobile seringkali memakan waktu lama dan kaku apabila menggunakan model tradisional (seperti Waterfall), sehingga sulit beradaptasi dengan perubahan kebutuhan pengguna dan alur kerja di lapangan.
6. **Metode atau Pendekatan yang Digunakan:** Metode *Rapid Application Development* (RAD) yang terbagi dalam 4 fase: *Requirements Planning*, *User Design* (pemodelan visual iteratif), *Construction* (pengkodean berbasis prototipe), dan *Cutover*.
7. **Hasil Penelitian:** Penerapan metode RAD berhasil mempercepat siklus peluncuran aplikasi mobile berbasis Android secara signifikan, meminimalkan revisi besar di akhir fase, dan menghasilkan tingkat kesesuaian antarmuka yang tinggi terhadap kebutuhan pengguna.
8. **Keterbatasan Penelitian:** Sistem yang dibangun hanya mencakup pencatatan kehadiran dasar (*clock-in* dan *clock-out*), belum diintegrasikan dengan kalkulasi upah/payroll, belum mendukung skema rotasi shift kerja, dan belum memiliki mekanisme kehandalan saat perangkat offline.
9. **Research Gap:** Belum ada integrasi metode RAD dalam membangun sistem presensi yang langsung terhubung dengan mesin kalkulasi penggajian dinamis (*daily payroll*) dan penanganan lingkungan kerja tanpa jaringan internet.

---

### 2. Jurnal 2: Sistem Informasi Absensi & Penggajian Karyawan Berbasis Geofencing
1. **Judul Penelitian:** *Pengembangan Sistem Informasi Absensi dan Penggajian Karyawan Berbasis Geofencing (Studi Kasus: PT. Quanta Teknik Gemilang)*
2. **Nama Penulis:** Zainul Arham, Zulfiandri Zulfiandri, Mohammad Novrizal Sugiarto, Bayu Waspodo, dan Sarip Hidayatullah
3. **Tahun Publikasi:** 2026
4. **Sumber / Jurnal Publikasi:** *JATI (Jurnal Mahasiswa Teknik Informatika)*, Vol. 10, No. 2, DOI: `10.36040/jati.v10i2.17647`.
5. **Permasalahan yang Diteliti:** Proses rekapitulasi data absensi dan penggajian yang manual rentan terhadap manipulasi lokasi kehadiran (*fake GPS*), kesalahan kalkulasi rekapitulasi lembur/kehadiran bulanan, serta keterlambatan penyusunan laporan keuangan.
6. **Metode atau Pendekatan yang Digunakan:** *Rapid Application Development* (RAD) dengan arsitektur *frontend* mobile menggunakan Flutter, *backend* Laravel, basis data MySQL, serta integrasi teknologi *Geofencing* dan *Face Recognition*.
7. **Hasil Penelitian:** Berhasil membangun aplikasi terintegrasi yang mampu memvalidasi kehadiran karyawan secara akurat di dalam radius area kerja (*geofence*), menangkal manipulasi lokasi, serta mengotomatisasi perhitungan gaji bulanan secara real-time.
8. **Keterbatasan Penelitian:** Sistem dirancang khusus untuk karyawan tetap dengan skenario penggajian bulanan standar (*fixed monthly salary*), mensyaratkan koneksi internet aktif secara konstan (*always online*), serta tidak mengakomodasi pemotongan penalti denda mutu kerja (*quality control defect*).
9. **Research Gap:** Ketiadaan fitur penggajian multi-tier untuk tenaga kerja harian lepas (yang upahnya dihitung per shift kerja tertentu) dan belum adanya sistem penalti operasional gudang yang adaptif terhadap fluktuasi kehadiran harian serta kondisi sinyal lemah.

---

### 3. Jurnal 3: Perancangan Aplikasi Penggajian Mobile Menggunakan Flutter
1. **Judul Penelitian:** *Perancangan Aplikasi Penggajian Karyawan Berbasis Android dan Dart Flutter pada PT Andalan K3 Menggunakan Model Waterfall*
2. **Nama Penulis:** Nafis Surya Wiguna dan Nanang Nanang
3. **Tahun Publikasi:** 2024
4. **Sumber / Jurnal Publikasi:** *Jurnal Multidisipliner Bharasumba*, Vol. 3, No. 04, Hal. 131–154, DOI: `10.62668/bharasumba.v3i04.1273`.
5. **Permasalahan yang Diteliti:** Lambatnya distribusi slip gaji konvensional, risiko kekeliruan perhitungan tunjangan manual, serta minimnya transparansi rincian gaji bagi karyawan lapangan yang tidak setiap hari berada di kantor pusat.
6. **Metode atau Pendekatan yang Digunakan:** Model *Waterfall* klasik (analisis kebutuhan, desain antarmuka UML, pengkodean Dart/Flutter untuk Android, pengujian *black-box*).
7. **Hasil Penelitian:** Menghasilkan aplikasi mobile penggajian yang memungkinkan pekerja melihat rincian upah, rincian tunjangan, dan mengunduh slip gaji digital langsung dari smartphone secara praktis.
8. **Keterbatasan Penelitian:** Alur Waterfall membuat proses penyesuaian fungsionalitas memakan waktu lama, skema gaji masih berorientasi pada komponen bulanan baku karyawan kantoran, dan aplikasi berhenti berfungsi apabila perangkat tidak memiliki jaringan internet aktif.
9. **Research Gap:** Belum tersedianya modul kalkulasi upah mandiri (*self-service estimation*) untuk pekerja lepas non-bulanan yang memiliki variabel potongan harian, serta perlunya peralihan ke metode iteratif (RAD) untuk menangani dinamika regulasi upah pergudangan.

---

### 4. Jurnal 4: Penjadwalan & Rotasi Shift Tenaga Kerja Lapangan
1. **Judul Penelitian:** *Pengembangan Sistem Informasi Penjadwalan Shift TKBM Berbasis Flutter dan Dart: Studi Kasus PT JICT*
2. **Nama Penulis:** Asep Saepul Jamrud
3. **Tahun Publikasi:** 2025
4. **Sumber / Jurnal Publikasi:** *REMIK: Riset dan E-Jurnal Manajemen Informatika Komputer*, Vol. 9, No. 4, Hal. 2110–2120.
5. **Permasalahan yang Diteliti:** Pengelolaan penjadwalan shift kerja tenaga kerja lapangan/bongkar muat yang dilakukan melalui pencatatan manual dan grup pesan singkat menimbulkan miskomunikasi jadwal, bentrok giliran shift, serta tidak adanya arsip kehadiran terpusat.
6. **Metode atau Pendekatan yang Digunakan:** Model *Waterfall*, antarmuka Flutter & Dart, *backend* berbasis Firebase Cloud Services, dan evaluasi *Black-Box Testing*.
7. **Hasil Penelitian:** Terciptanya aplikasi mobile "MyTKBM" yang mampu mengotomasi penyusunan jadwal giliran kerja (*shift rotation*), pengajuan izin/tukar shift, serta presensi berbasis GPS secara terpusat.
8. **Keterbatasan Penelitian:** Sistem murni berfokus pada penjadwalan operasional shift tanpa mengintegrasikan logika perhitungan upah/payroll dari shift yang dijalankan, bergantung penuh pada layanan *cloud* Firebase, dan tidak memperhitungkan denda keterlambatan per menit.
9. **Research Gap:** Ketiadaan jembatan langsung antara riwayat pemenuhan shift kerja harian dengan formula penghitungan upah bertingkat (*multi-tier payroll* seperti shift MP3H, Double Shift, dan Reguler) beserta denda keterlambatan akumulatif.

---

### 5. Jurnal 5: Arsitektur Offline-First pada Sistem Informasi Presensi Mobile
1. **Judul Penelitian:** *Pengembangan Sistem Asisten Administrasi Presensi dengan Fitur Autentikasi Visual dan Manajemen Data Offline-First*
2. **Nama Penulis:** F. H. Siregar, A. M. Nur, dan D. R. Wijaya
3. **Tahun Publikasi:** 2026
4. **Sumber / Jurnal Publikasi:** *Calamus: Journal of Computer Science and Information Systems*, Vol. 5, No. 1, Hal. 45–58.
5. **Permasalahan yang Diteliti:** Wilayah operasional lapangan seringkali mengalami *blank spot* atau ketiadaan jaringan internet yang stabil, sehingga aplikasi presensi online gagal mencatat transaksi kehadiran dan menyebabkan komplain dari para pekerja.
6. **Metode atau Pendekatan yang Digunakan:** Arsitektur *Offline-First* dengan penyimpanan lokal klien (*Local Database*), arsitektur MVVM, dan sinkronisasi otomatis dua arah (*Two-Way Auto Sync*) saat koneksi internet pulih.
7. **Hasil Penelitian:** Aplikasi mampu mencatat data transaksi kehadiran secara instan tanpa hambatan latensi jaringan saat berada di zona *offline*, serta menyinkronkan seluruh catatan transaksi secara otomatis ke server pusat tanpa duplikasi data.
8. **Keterbatasan Penelitian:** Penelitian dibatasi hanya pada presensi dan pengenalan visual kehadiran siswa/staf, belum menyentuh manajemen kompensasi/upah finansial, dan belum mencakup validasi aturan kerja shift industri.
9. **Research Gap:** Belum diimplementasikannya arsitektur *offline-first* pada sistem manajemen tenaga kerja gudang logistik yang menggabungkan presensi shift kerja, tracking kuota SKU, dan perhitungan estimasi upah harian secara terdesentralisasi.

---

## 📊 BAGIAN II: TABEL MATRIKS IDENTIFIKASI RESEARCH GAP (OUTPUT UTAMA)

| No | Judul Jurnal | Tahun | Metode | Hasil Penelitian | Keterbatasan | Research Gap (Celah Penelitian untuk Proposal Skripsi) |
| :-: | :--- | :-: | :--- | :--- | :--- | :--- |
| **1** | Analisis Metode Rapid Application Development untuk Aplikasi Absensi di Android | 2025 | Rapid Application Development (RAD) | Mempercepat siklus pengembangan aplikasi absensi mobile dan menghasilkan antarmuka yang sangat responsif terhadap kebutuhan user. | Hanya memvalidasi absensi dasar, tanpa modul kalkulasi upah/payroll, dan belum memiliki proteksi offline. | Belum mengintegrasikan metode RAD pada sistem presensi yang terhubung langsung dengan kalkulasi upah dinamis dan arsitektur *offline-first*. |
| **2** | Pengembangan Sistem Informasi Absensi dan Penggajian Karyawan Berbasis Geofencing (Studi Kasus: PT. Quanta Teknik Gemilang) | 2026 | RAD, Flutter, Laravel, Geofencing & Face Recognition | Mengotomatisasi absensi berkoordinat geofencing anti-fake GPS dan kalkulasi penggajian bulanan secara terintegrasi. | Skema gaji hanya untuk karyawan tetap bulanan, memerlukan koneksi internet stabil terus-menerus, tanpa denda mutu kerja. | Belum mengakomodasi kalkulasi payroll *multi-tier* bagi pekerja harian lepas dan penanganan pemotongan denda mutu operasional gudang. |
| **3** | Perancangan Aplikasi Penggajian Karyawan Berbasis Android dan Dart Flutter pada PT Andalan K3 Menggunakan Model Waterfall | 2024 | Model Waterfall, Dart & Flutter Android | Mempermudah karyawan mengakses slip gaji digital dan transparansi rincian tunjangan secara mobile. | Model Waterfall kaku terhadap perubahan kebutuhan, perhitungan upah berbasis gaji bulanan tetap, tidak ada penyimpanan offline. | Belum menerapkan pendekatan iteratif cepat (RAD) untuk mengakomodasi fleksibilitas upah harian lepas dan modul slip gaji mandiri (*self-service*). |
| **4** | Pengembangan Sistem Informasi Penjadwalan Shift TKBM Berbasis Flutter dan Dart: Studi Kasus PT JICT | 2025 | Waterfall, Flutter & Dart, Firebase Backend | Mengotomasi rotasi penjadwalan shift kerja tenaga kerja lapangan secara terpusat dan presensi GPS. | Tidak memiliki modul kalkulasi upah/payroll, ketergantungan penuh pada cloud online, tanpa validasi denda telat per menit. | Belum ada integrasi langsung antara rotasi shift kerja harian dengan kalkulasi upah harian bertingkat (Reguler, MP3H, Double Shift) dan denda keterlambatan. |
| **5** | Pengembangan Sistem Asisten Administrasi Presensi dengan Fitur Autentikasi Visual dan Manajemen Data Offline-First | 2026 | Offline-First Architecture, Local Database, Auto-Sync | Sistem tetap berfungsi mencatat presensi tanpa koneksi internet di area *blank spot* dan auto-sync saat online. | Hanya fokus pada presensi dan pengenalan wajah, tanpa modul finansial/upah dan tanpa klasifikasi shift industri. | Belum diterapkannya arsitektur *offline-first* pada aplikasi manajemen shift dan kalkulasi upah terintegrasi untuk pekerja gudang e-grocery. |

---

## 🎯 BAGIAN III: SINTESIS NOVELTY & RESEARCH GAP PROPOSAL SKRIPSI

Berdasarkan sintesis dari kelima jurnal ilmiah bereputasi di atas, celah penelitian (*Research Gap*) utama yang menjadi landasan kebaruan (*novelty*) dari rencana skripsi **Lukman Hakim** adalah:

> **"Mayoritas penelitian terdahulu mengenai sistem presensi dan penggajian berbasis mobile berfokus pada karyawan tetap perkantoran (*fixed monthly salary*) dengan asumsi konektivitas internet selalu stabil (*always online*), serta menggunakan alur pengembangan konvensional yang kaku. Belum ada penelitian yang mengintegrasikan metode pengembangan cepat (Rapid Application Development / RAD) untuk membangun sistem informasi presensi mandiri dan kalkulasi upah harian lepas bertingkat (*multi-tier payroll*: Reguler, MP3H, Double MP3H), yang dilengkapi penalti denda operasional mutu produk (*Quality Control*) dan denda keterlambatan akumulatif, dengan dukungan arsitektur *Offline-First* guna mengatasi kendala *blank spot* sinyal pada gudang *fulfillment logistik*."**

---

### 💬 FORMAT PESAN SIAP KIRIM UNTUK DOSEN (MENTARI / WHATSAPP)

> **Selamat Pagi/Siang Bapak Ahmad Asep Suhendi, S.Kom., M.Kom.**
>
> Izin mengumpulkan **Tugas 2: Penelusuran Jurnal dan Identifikasi Research Gap untuk Proposal Skripsi** pada mata kuliah Metodologi Riset.
>
> Berikut ringkasan penelusuran 5 jurnal ilmiah yang relevan dengan rencana judul skripsi saya:
> - **Nama Mahasiswa:** LUKMAN HAKIM
> - **NIM:** 241011700845
> - **Kelas:** 05SIFM002 / Reguler B (Semester 5)
> - **Rencana Judul Skripsi:** *"Pengembangan Sistem Informasi Manajemen Shift dan Penggajian Pekerja Harian Lepas Berbasis Mobile Menggunakan Metode Rapid Application Development (Studi Kasus: Gudang Fulfillment Segari)"*
>
> **Fokus Research Gap yang Diangkat:**
> Dari telaah 5 jurnal nasional terkini (2024–2026), ditemukan bahwa penelitian sistem absensi & penggajian mobile sebelumnya masih berfokus pada karyawan tetap (*fixed monthly salary*) dan mensyaratkan koneksi internet aktif (*always online*). Penelitian yang saya usulkan mengisi celah tersebut dengan menghadirkan otomasi kalkulasi upah *multi-tier* harian lepas (Reguler, MP3H, Double Shift), penanganan denda operasional mutu produk QC, serta arsitektur *Offline-First* untuk area gudang logistik minim sinyal menggunakan metode *Rapid Application Development* (RAD).
>
> 📄 Berkas PDF tabel analisis lengkap telah saya unggah ke dalam sistem.
>
> Terima kasih atas bimbingan dan arahan Bapak.
