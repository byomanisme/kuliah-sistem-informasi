import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
import pymupdf

class NumberedCanvas(canvas.Canvas):
    """Canvas untuk menambahkan nomor halaman dinamis (Halaman X dari Y) dan running header."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (mulai halaman 2)
        if self._pageNumber > 1:
            self.drawString(36, 814, "TUGAS METODOLOGI RISET — LUKMAN HAKIM (NIM: 241011700845)")
            self.drawRightString(559, 814, "S1 SISTEM INFORMASI UNPAM")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, 808, 559, 808)

        # Footer (semua halaman)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 32, 559, 32)
        self.drawString(36, 22, "Topik Riset: Rancang Bangun Sistem Informasi Manajemen Shift & Upah Harian (Gajiku Segari)")
        page_text = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(559, 22, page_text)
        self.restoreState()


def build_pdf(filename="TUGAS_METODOLOGI_RISET_LUKMAN_HAKIM.pdf"):
    # Printable area: width = 595.27 - 72 = 523.27
    content_width = 523
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom typography colors
    color_primary = colors.HexColor("#1E3A8A")     # Navy
    color_secondary = colors.HexColor("#0D9488")   # Teal / Segari Dark Green
    color_dark = colors.HexColor("#0F172A")        # Slate 900
    color_gray = colors.HexColor("#334155")        # Slate 700

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=color_primary,
        alignment=1 # Center
    )

    sub_title_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=color_secondary,
        alignment=1 # Center
    )

    inst_style = ParagraphStyle(
        'DocInst',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#475569"),
        alignment=1 # Center
    )

    section_heading = ParagraphStyle(
        'SecHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=color_primary,
        spaceBefore=5,
        spaceAfter=3
    )

    q_title_style = ParagraphStyle(
        'QTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#1E293B")
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.5,
        textColor=color_dark
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=color_gray,
        leftIndent=10
    )

    quote_style = ParagraphStyle(
        'QuoteCustom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor("#0F766E")
    )

    meta_label = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#1E3A8A")
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=color_dark
    )

    story = []

    # 1. KOP SURAT / HEADER DOKUMEN
    story.append(Paragraph("TUGAS INDIVIDU METODOLOGI RISET", title_style))
    story.append(Spacer(1, 1))
    story.append(Paragraph("IDENTIFIKASI MASALAH DAN PERUMUSAN JUDUL SKRIPSI", sub_title_style))
    story.append(Spacer(1, 1))
    story.append(Paragraph("PROGRAM STUDI S1 SISTEM INFORMASI &bull; FAKULTAS ILMU KOMPUTER &bull; UNIVERSITAS PAMULANG", inst_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.2, color=color_primary, spaceBefore=0, spaceAfter=5))

    # 2. IDENTITAS MAHASISWA (TABLE)
    data_identitas = [
        [
            Paragraph("Nama Mahasiswa", meta_label), Paragraph(": <b>LUKMAN HAKIM</b>", meta_val),
            Paragraph("Mata Kuliah", meta_label), Paragraph(": <b>Metodologi Riset</b>", meta_val)
        ],
        [
            Paragraph("N I M", meta_label), Paragraph(": <b>241011700845</b>", meta_val),
            Paragraph("Program Studi", meta_label), Paragraph(": S1 Sistem Informasi", meta_val)
        ],
        [
            Paragraph("Kelas / Shift", meta_label), Paragraph(": <b>REGULER B</b> (Semester 5)", meta_val),
            Paragraph("Fakultas / Kampus", meta_label), Paragraph(": Ilmu Komputer / Universitas Pamulang", meta_val)
        ],
        [
            Paragraph("Objek Studi Kasus", meta_label), Paragraph(": <b>Gajiku Segari (Salary & Shift Tracker)</b>", meta_val),
            Paragraph("Tahun Akademik", meta_label), Paragraph(": Ganjil 2026/2027", meta_val)
        ]
    ]

    t_identitas = Table(data_identitas, colWidths=[90, 171, 90, 172])
    t_identitas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor("#CBD5E1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_identitas)
    story.append(Spacer(1, 5))

    # 3. PENGANTAR STUDI KASUS RIIL
    story.append(Paragraph("A. Ringkasan Objek Penelitian Riil (Studi Kasus)", section_heading))
    p_intro = Paragraph(
        "Penelitian ini mengangkat objek studi empiris pada operasional tenaga kerja harian lepas (<i>Daily Worker</i>) "
        "di pusat pemenuhan pesanan (<i>Fulfillment Center</i>) <b>PT Sayur Untuk Semua (Segari)</b>. Sistem kerja operasional "
        "memiliki kompleksitas perhitungan upah harian yang dinamis, meliputi pembagian shift (Reguler, MP3H, Double MP3H), "
        "toleransi keterlambatan (<i>grace period</i> 5 menit), penalti keterlambatan akumulatif (>3 kali denda Rp 100.000), "
        "potongan denda komplain 6 kategori mutu QC (barang kurang, kemasan rusak, busuk, kontaminasi kotor), "
        "serta insentif target kuota pemilahan (<i>picking SKU</i>).",
        body_style
    )
    story.append(p_intro)
    story.append(Spacer(1, 4))

    # 4. PEMBAHASAN 7 PERTANYAAN TUGAS
    story.append(Paragraph("B. Pembahasan Lembar Pertanyaan Tugas Metodologi Riset", section_heading))
    story.append(Spacer(1, 2))

    qa_list = [
        (
            "1. Apa fenomenanya?",
            [
                Paragraph("<b>Fenomena Empiris yang Diteliti:</b>", q_title_style),
                Paragraph(
                    "Pesatnya ekspansi industri logistik dan <i>e-grocery</i> modern di Indonesia mendorong tingginya ketergantungan "
                    "perusahaan terhadap tenaga kerja harian lepas (<i>Daily Worker / Gig Workers</i>) di pergudangan (<i>Fulfillment Center</i>). "
                    "Pekerja harian menghadapi dinamika rotasi shift yang fleksibel, target pemenuhan kuota pesanan harian (picking SKU), "
                    "serta pengawasan Standard Operating Procedure (SOP) mutu yang ketat melalui skema denda operasional.",
                    body_style
                )
            ]
        ),
        (
            "2. Apa masalah utamanya?",
            [
                Paragraph("<b>Masalah Utama (Problem Statement):</b>", q_title_style),
                Paragraph(
                    "<b>Ketimpangan informasi dan tingginya potensi selisih (<i>discrepancy</i>) pada perhitungan upah bersih (<i>Take-Home Pay</i>) "
                    "pekerja harian lepas akibat ketiadaan sistem pencatatan mandiri yang transparan, valid, dan terstandarisasi.</b>",
                    quote_style
                ),
                Paragraph("Faktor-faktor penyebab masalah utama meliputi:", body_style),
                Paragraph("&bull; <b>Ketiadaan Akses HR Real-Time:</b> Pekerja harian lepas tidak memiliki akses langsung ke sistem payroll internal perusahaan untuk memverifikasi absensi dan lembur secara harian.", bullet_style),
                Paragraph("&bull; <b>Kompleksitas Multi-Tier Payroll:</b> Upah melibatkan variabel dinamis (shift reguler vs MP3H, toleransi telat 5 menit, dan denda keterlambatan >3 kali sebulan).", bullet_style),
                Paragraph("&bull; <b>Denda Komplain Mutu QC:</b> Pembebanan potongan denda atas 6 kategori komplain cacat mutu tanpa rincian tanggal dan bukti audit yang dapat diverifikasi mandiri.", bullet_style),
                Paragraph("&bull; <b>Pencatatan Manual Rentan Hilang:</b> Pekerja kesulitan melakukan klaim koreksi gaji saat gajian karena bukti catatan fisik sering tercecer.", bullet_style)
            ]
        ),
        (
            "3. Siapa pengguna sistem?",
            [
                Paragraph("<b>Target Pengguna Sistem (Stakeholders):</b>", q_title_style),
                Paragraph("&bull; <b>Pengguna Utama (<i>Primary End-User</i>):</b> Tenaga Kerja Harian Lepas (<i>Daily Worker</i> / kru <i>picker</i>, <i>packer</i>, dan <i>sorter</i>) di gudang fulfillment Segari yang membutuhkan sistem presensi mandiri, pelacak denda, dan kalkulator gaji bersih real-time.", bullet_style),
                Paragraph("&bull; <b>Pengguna Sekunder (<i>Secondary Stakeholder</i>):</b> Koordinator Shift / Supervisor Lapangan dan Tim HR Payroll yang menerima dokumen rekapitulasi slip gaji PDF resmi hasil ekspor aplikasi sebagai pembanding klaim gaji.", bullet_style)
            ]
        ),
        (
            "4. Teknologi apa yang cocok?",
            [
                Paragraph("<b>Arsitektur & Tumpukan Teknologi (Technology Stack):</b>", q_title_style),
                Paragraph("&bull; <b>Frontend Mobile:</b> <b>Flutter & Dart</b> — Menghasilkan aplikasi mobile cross-platform yang responsif, hemat memori, dan stabil di smartphone Android entry-level milik pekerja.", bullet_style),
                Paragraph("&bull; <b>Database & Penyimpanan Lokal:</b> <b>SQLite & SharedPreferences (Offline-First)</b> — Memungkinkan input presensi dan shift tanpa ketergantungan koneksi internet di area gudang minim sinyal.", bullet_style),
                Paragraph("&bull; <b>Backend & Sinkronisasi:</b> <b>RESTful API & Cloud Storage</b> — Sinkronisasi dua arah (<i>2-Way Cloud Push/Pull</i>) dan Google Drive Backup untuk keamanan data.", bullet_style),
                Paragraph("&bull; <b>Reporting Engine:</b> <b>PDF Generation Library</b> — Pembuatan slip rekapitulasi upah digital resmi yang dapat dibagikan via WhatsApp.", bullet_style)
            ]
        ),
        (
            "5. Aplikasi seperti apa yang dapat dibangun?",
            [
                Paragraph("<b>Spesifikasi Aplikasi yang Dibangun:</b>", q_title_style),
                Paragraph(
                    "Aplikasi Mobile <b>Work Shift Manager & Real-Time Payroll Calculator</b> berbasis <i>Offline-First</i> dengan modul utama:",
                    body_style
                ),
                Paragraph("&bull; <b>Presensi Cerdas (Clock-In & Out):</b> Pencatatan jam kehadiran dengan perhitungan menit keterlambatan otomatis dan toleransi <i>grace period</i> 5 menit.", bullet_style),
                Paragraph("&bull; <b>Kalkulator Multi-Tier Payroll:</b> Estimasi otomatis upah harian sesuai jenis shift kerja (Reguler, MP3H, Double MP3H, Training).", bullet_style),
                Paragraph("&bull; <b>Modul Kontrol Denda & QC:</b> Log sanksi keterlambatan (>3x denda Rp 100.000) dan 6 kategori mutu komplain gudang.", bullet_style),
                Paragraph("&bull; <b>Pelacak Kuota SKU & Ekspor PDF:</b> Visualisasi progres target picking SKU harian dan generator slip gaji bulanan siap cetak.", bullet_style)
            ]
        ),
        (
            "6. Buat satu rumusan masalah.",
            [
                Paragraph("<b>Rumusan Masalah Penelitian:</b>", q_title_style),
                Paragraph(
                    "<b>\"Bagaimana merancang dan mengimplementasikan aplikasi manajemen shift kerja dan estimasi upah harian lepas "
                    "berbasis mobile dengan menerapkan aturan kalkulasi payroll multi-tier dan validasi presensi guna meningkatkan "
                    "akurasi serta transparansi penerimaan upah pekerja?\"</b>",
                    quote_style
                )
            ]
        ),
        (
            "7. Buat satu judul skripsi.",
            [
                Paragraph("<b>Judul Skripsi yang Diusulkan:</b>", q_title_style),
                Paragraph(
                    "<b>\"Rancang Bangun Sistem Informasi Manajemen Shift Kerja dan Kalkulasi Upah Pekerja Harian Lepas Berbasis Mobile "
                    "(Studi Kasus: Gudang Fulfillment Segari)\"</b>",
                    quote_style
                ),
                Spacer(1, 1),
                Paragraph("<i>Alternatif Judul (Pendekatan Software Engineering):</i>", meta_label),
                Paragraph(
                    "\"Pengembangan Aplikasi Manajemen Presensi dan Kalkulasi Penggajian Multi-Tier Berbasis Flutter "
                    "untuk Pekerja Harian Lepas pada Pusat Distribusi E-Grocery\"",
                    body_style
                )
            ]
        )
    ]

    for q_title, q_contents in qa_list:
        card_content = [
            Paragraph(f"<b>{q_title}</b>", ParagraphStyle('QHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, textColor=color_primary, leading=11.5)),
            Spacer(1, 2),
            HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#CBD5E1"), spaceBefore=0, spaceAfter=3)
        ]
        card_content.extend(q_contents)

        t_card = Table([[card_content]], colWidths=[content_width])
        t_card.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FFFFFF")),
            ('BOX', (0, 0), (-1, -1), 0.6, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))

        story.append(t_card)
        story.append(Spacer(1, 4))

    # 5. NILAI TAMBAH: RENCANA PENGUJIAN & METODOLOGI RISET
    story.append(Paragraph("C. Metodologi Penelitian & Pengujian yang Diusulkan", section_heading))
    story.append(Paragraph(
        "Rancangan metodologi riset dan pengujian sistem yang diterapkan meliputi:",
        body_style
    ))
    story.append(Paragraph("&bull; <b>Metode Pengembangan Sistem:</b> Menggunakan model <b>SDLC Waterfall / Agile Scrum</b> melalui tahapan Analisis Kebutuhan, Perancangan UML (Use Case, Activity, Sequence), Implementasi Kode (Flutter & REST API), dan Pengujian.", bullet_style))
    story.append(Paragraph("&bull; <b>Metode Pengujian Fungsionalitas:</b> Menggunakan teknik <b>Black Box Testing</b> (<i>Boundary Value Analysis</i>) untuk memvalidasi presisi kalkulasi upah, toleransi 5 menit, dan denda bertingkat.", bullet_style))
    story.append(Paragraph("&bull; <b>Metode Pengujian Pengguna:</b> Menggunakan instrumen <b>System Usability Scale (SUS)</b> dan <b>User Acceptance Testing (UAT)</b> langsung kepada para pekerja harian lepas untuk mengukur aspek kemudahan (<i>usability</i>) sistem.", bullet_style))
    story.append(Spacer(1, 6))
    
    # Lembar Pengesahan Mahasiswa
    t_sign = Table([
        [
            Paragraph("", body_style),
            Paragraph("Tangerang Selatan, 21 September 2026<br/>Mahasiswa Penyusun,<br/><br/><br/><b><u>LUKMAN HAKIM</u></b><br/>NIM. 241011700845", ParagraphStyle('SignStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=8.2, leading=11.5, alignment=1))
        ]
    ], colWidths=[290, 233], style=[
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF berhasil dibuat: {filename}")

if __name__ == "__main__":
    build_pdf()
    doc = pymupdf.open("TUGAS_METODOLOGI_RISET_LUKMAN_HAKIM.pdf")
    print(f"Total halaman: {len(doc)}")
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        pix.save(f"page_{i+1}.png")
        print(f"Saved page_{i+1}.png")
