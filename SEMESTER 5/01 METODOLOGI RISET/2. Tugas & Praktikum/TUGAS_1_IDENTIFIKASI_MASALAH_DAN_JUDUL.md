# 📝 LEMBAR JAWABAN TUGAS METODOLOGI RISET
### Identifikasi Masalah & Perumusan Judul Skripsi S1 Sistem Informasi

* **Nama Mahasiswa:** LUKMAN HAKIM
* **N I M:** 241011700845
* **Kelas / Shift:** REGULER B (Semester 5)
* **Program Studi:** S1 Sistem Informasi
* **Fakultas:** Ilmu Komputer
* **Universitas:** Universitas Pamulang (UNPAM)
* **Mata Kuliah:** Metodologi Riset
* **Objek Kasus:** Gajiku Segari (Segari Salary Tracker & Work Shift Manager)

---

## A. Objek Penelitian Riil (Studi Kasus)
Penelitian ini mengangkat objek studi empiris pada operasional tenaga kerja harian lepas (*Daily Worker*) di pusat pemenuhan pesanan (*Fulfillment Center*) **PT Sayur Untuk Semua (Segari)**. Sistem kerja lapangan memiliki dinamika rotasi shift yang fleksibel (Reguler, MP3H, Double MP3H), aturan toleransi keterlambatan (*grace period* 5 menit), penalti keterlambatan bertingkat (>3 kali denda Rp 100.000), potongan denda komplain 6 kategori mutu QC (barang kurang, kemasan rusak, busuk, kontaminasi kotor), serta insentif target kuota pemilahan (*picking SKU*).

---

## B. Pembahasan Lembar Pertanyaan Tugas

### 1. Apa fenomenanya?
**Pertumbuhan sektor *e-grocery* dan rantai pasok logistik modern yang mendorong tingginya penyerapan tenaga kerja harian lepas (*Daily Worker* / Gig Workers), di mana sistem kerja menuntut fleksibilitas rotasi shift dan kepatuhan terhadap Standard Operating Procedure (SOP) mutu serta kecepatan pemenuhan pesanan.**

### 2. Apa masalah utamanya?
**Ketimpangan informasi dan tingginya potensi selisih (*discrepancy*) pada perhitungan upah bersih (*Take-Home Pay*) pekerja harian lepas akibat ketiadaan sistem pencatatan mandiri yang transparan, valid, dan terstandarisasi.**
* Ketiadaan akses langsung pekerja ke sistem HR/payroll internal secara berkala.
* Kompleksitas perhitungan multi-tier (Reguler, MP3H, toleransi telat, denda keterlambatan).
* Beban potongan denda 6 kategori komplain cacat mutu QC tanpa rincian tanggal dan bukti audit mandiri.
* Pencatatan manual di kertas rentan hilang dan sulit dijadikan bukti klaim koreksi saat penggajian.

### 3. Siapa pengguna sistem?
1. **Pengguna Utama (*Primary End-User*):** Tenaga Kerja Harian Lepas (*Daily Worker* / kru *picker*, *packer*, dan *sorter*) di gudang fulfillment Segari.
2. **Pengguna Sekunder (*Secondary Stakeholder*):** Koordinator Shift / Supervisor Lapangan dan Tim HR Payroll (yang menerima laporan rekapitulasi slip gaji PDF resmi hasil ekspor aplikasi).

### 4. Teknologi apa yang cocok?
1. **Frontend Mobile Framework:** **Flutter & Dart** (Cross-platform Android & iOS, hemat memori, dan responsif di smartphone entry-level).
2. **Database Lokal:** **SQLite & SharedPreferences** (*Offline-First Architecture*, dapat beroperasi tanpa internet di gudang).
3. **Backend & Sinkronisasi:** **RESTful API** berbasis Cloud Server dengan JSON dan 2-Way Sync.
4. **Reporting Engine:** **PDF Generation Library** untuk mencetak slip gaji digital terstandarisasi.

### 5. Aplikasi seperti apa yang dapat dibangun?
Aplikasi Mobile **Work Shift Manager & Real-Time Payroll Calculator** berbasis *Offline-First* dengan modul utama:
* Presensi cerdas (Clock-In/Clock-Out) dengan deteksi menit keterlambatan dan *grace period* 5 menit.
* Kalkulator payroll otomatis multi-tier (Reguler, MP3H, Double MP3H, Training).
* Modul kontrol denda keterlambatan akumulatif (>3x) dan 6 kategori mutu komplain QC.
* Pelacak progres target kuota harian picking SKU (Severity 1, 2, 3).
* Ekspor rekapitulasi slip gaji PDF siap cetak dan sinkronisasi cloud cadangan.

### 6. Buat satu rumusan masalah.
> *"Bagaimana merancang dan mengimplementasikan aplikasi manajemen shift kerja dan estimasi upah harian lepas berbasis mobile dengan menerapkan aturan kalkulasi payroll multi-tier dan validasi presensi guna meningkatkan akurasi serta transparansi penerimaan upah pekerja?"*

### 7. Buat satu judul skripsi.
> **"Rancang Bangun Sistem Informasi Manajemen Shift Kerja dan Kalkulasi Upah Pekerja Harian Lepas Berbasis Mobile (Studi Kasus: Gudang Fulfillment Segari)"**
> 
> *Alternatif Judul:*  
> **"Pengembangan Aplikasi Manajemen Presensi dan Kalkulasi Penggajian Multi-Tier Berbasis Flutter untuk Pekerja Harian Lepas pada Pusat Distribusi E-Grocery"**

---

## C. Metodologi Penelitian & Pengujian
* **Model Pengembangan:** SDLC Waterfall / Agile Scrum (Analisis Kebutuhan, Desain UML, Koding Flutter/API, Pengujian).
* **Pengujian Fungsional:** Black Box Testing (*Boundary Value Analysis* pada toleransi 5 menit dan denda bertingkat).
* **Pengujian Pengguna:** *System Usability Scale* (SUS) dan *User Acceptance Testing* (UAT) langsung kepada para kru harian lepas.
