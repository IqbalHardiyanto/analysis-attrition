# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan edutech **Jaya Jaya Maju** bergerak di bidang pendidikan berbasis teknologi dengan fokus pada pengembangan produk digital, konten edukasi, dan layanan pembelajaran. Sumber daya manusia (khususnya talenta teknis dan akademik) merupakan aset. Tren attrition yang tinggi dapat mengganggu keberlanjutan pengembangan produk, pengalaman pengguna, dan inovasi kurikulum. Industri edutech yang kompetitif juga membuat retensi talenta menjadi penentu keunggulan bisnis.

---

#### Permasalahan Bisnis

1. **Tingkat Attrition Tinggi:** Karyawan mengalami attrition, terutama di departemen R&D dan Sales.
2. **Ketidakpuasan Lingkungan Kerja:** Karyawan melaporkan kepuasan lingkungan rendah (skor 1).
3. **Work-Life Balance Buruk:** Karyawan memberi ulasan kurang dari 2 (skala 4), terutama yang sering business travel.
4. **Stagnasi Karir:** Karyawan dengan masa kerja lebih 3 tahun tidak pernah dipromosikan.
5. **Ketimpangan Kompensasi:** Kesenjangan pendapatan bulanan (MonthlyIncome) mencapai 300% antara level junior dan senior.
6. **Beban Kerja Tidak Seimbang:** Karyawan sering lembur terutama di Sales.

---

#### Cakupan Proyek

| Area Analisis              | Metodologi                                                       | Output Target                         |
| -------------------------- | ---------------------------------------------------------------- | ------------------------------------- |
| Faktor Penyebab Attrition  | EDA, Regresi Logistik                                            | Identifikasi 5 driver utama attrition |
| Segmentasi Karyawan Risiko | Klasifikasi                                                      | Pemetaan kelompok berisiko tinggi     |
| Prediksi Attrition         | Model Machine Learning (Logistic Regression, Random Forest, SVM) | Akurasi prediksi > 80%                |
| Analisis Kepuasan          | Korelasi                                                         | Rekomendasi peningkatan prioritas     |
| Simulasi Kebijakan         | Analisis What-If                                                 | Estimasi program retensi              |

---

#### Persiapan

Sumber data: employee_data.csv

Setup environment anaconda / miniconda:

```
- conda create --name main-attrition
- conda activate main-attrition
- pip install streamlit
- pip install seaborn pandas matplotlib numpy os
- pip install pipreqs
```

Setup environment - Shell/Terminal:

```
- mkdir analysis-attrition
- cd analysis-attrition
- pipenv install
- pipenv shell
- pip install seaborn pandas matplotlib numpy os
- pip install -r requirements.txt
```

Run Streamlit App

```
- cd analysis-attrition
- streamlit run app.py
```

Link demo aplikasi attrition employee [Streamlit app](https://analysis-attrition-fvjimsfbcynw44559cnpxs.streamlit.app/)

---

## Business Dashboard

Business Dashboard [HR - Attrition Employee Analysis](https://public.tableau.com/views/HR-AttritionEmployeeAnalysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Dashboard ini menyajikan analisis komprehensif tentang attrittion karyawan (pengunduran diri) untuk membantu HR dan manajemen mengidentifikasi pola, risiko, serta wawasan yang dapat ditindaklanjuti.
Berikut rincian komponen dan implikasi bisnisnya:

1. Ringkasan Karyawan:

   - Total Karyawan: 1.058
   - Bertahan: 879 (83%)
   - Mengundurkan Diri: 179 (17%)
   - Tingkat Attrition: 16,9%
   - Insight: Hampir 1 dari 6 karyawan mengundurkan diri, menandakan perlunya strategi retensi.

2. Analisis Gaji per Departemen
   Membandingkan gaji rata-rata karyawan yang resign vs bertahan:

   - Human Resources (HR):

     - Resign: $2.717,09 | Bertahan: $2.717,09
     - Tidak ada kesenjangan gaji; attrition kemungkinan dipicu faktor non-moneter.

   - R&D:

     - Resign: $2.074,14 | Bertahan: $2.097,14
     - Gaji sedikit lebih rendah pada karyawan yang resign.

   - Sales:
     - Resign: $1.625,37 | Bertahan: $1.625,3
     - Tidak ada kesenjangan gaji; attrition mungkin disebabkan masalah lain.

3. Attrition per Departemen
   Attrition Tertinggi: HR (30,2%).
   Tingkat attrition R&D dan Sales tidak ditampilkan secara eksplisit, tetapi lebih rendah dari HR.
   Tindakan: Selidiki praktik HR (beban kerja, perkembangan karier, durasi jam perhari, dan lain-lain).

4. Work Life Balanced
   Status Attrition: Terbagi antara "Tidak" (bertahan) dan "Ya" (resign).
   Implikasi: Work Life Balanced yang buruk berkorelasi dengan resignasi (umum di departemen attrition tinggi seperti HR).

**Wawasan Bisnis & Rekomendasi**

1.  Krisis Departemen HR:
    Attrition 30,2% memerlukan intervensi mendesak (misal tinjau ulang beban kerja, pelatihan manajer).

2.  Gaji Bukan Faktor Utama:
    Tidak ada kesenjangan gaji signifikan di HR/Sales; fokus pada faktor non-moneter (keterlibatan, fleksibilitas).

3.  Sasarkan Kelompok Berisiko Tinggi:
    Karyawan berusia 25–34 tahun dan masa kerja awal (0–5 tahun) membutuhkan pengembangan karier dan promosi.

4.  Strategi Spesifik per Peran:
    Atasi turnover peran Lab Technician/Sales lewat program mentor atau peningkatan keterampilan.

5.  Mempercepat Promosi:
    Akselerasi promosi untuk kinerja tinggi guna mempertahankan talenta.

6.  Keseimbangan Kerja-Hidup:
    Terapkan kebijakan seperti jam kerja fleksibel (khususnya di peran bertekanan tinggi).

---

## Conclusion

#### 🔑 **5 Faktor Utama Penyebab Attrition**

1. **Lingkungan kerja tidak memuaskan** (EnvironmentSatisfaction rendah)
2. **Work-life balance buruk** (terutama pada karyawan yang sering _business travel_)
3. **Stagnasi karir** (karyawan >3 tahun tidak pernah dipromosikan)
4. **Kesenjangan kompensasi** (selisih gaji junior-senior hingga 300%)
5. **Beban kerja berlebihan** (lembur kronis di departemen Sales)

#### 📊 **Temuan Kritis dari Analisis Data**

- **Departemen paling terdampak**: R&D dan Sales
- **Karyawan berisiko tinggi**:
  - Skor EnvironmentSatisfaction = 1
  - Skor WorkLifeBalance kurang dari 2
  - YearsSinceLastPromotion = 0 meski masa kerja lebih dari 3 tahun
- **Prediksi akurat**: Model ML (Random Forest) mencapai **akurasi 80%** dalam identifikasi karyawan berpotensi resign

---

## Rekomendasi Action Items

##### 🚀 **Segera Implementasi**

- **Program "Flexi-Work"** Berikan WFH 2 hari/minggu untuk karyawan dengan DistanceFromHome jarak lebih 10 km (terdampak 34% karyawan).
- **Penyesuaian Kompensasi**Naikkan gaji 10–15% untuk peran kritis di R&D dengan MonthlyIncome kurang dari $5000 (17% karyawan).
- **Career Path Transparan**
  Buat kebijakan promosi wajib tiap 2 tahun (tertarget ke 31% karyawan stagnan).

##### 📈 **Strategi Jangka Menengah**

- **Redesign Peran Sales**Kurangi beban kerja non-essential (misal: administrasi) untuk tim Sales yang OverTime lebih 20%.
- **Wellness Program**Luncurkan subsidi konseling & fitness tracker untuk karyawan WorkLifeBalance kurang dari 2.
- **Skill Development**
  Berikan sertifikasi tech/edtech gratis bagi karyawan dengan masa pelatihan kurang 2 tahun.

##### 💡 **Strategi Inovatif**

- **Equity untuk Talent Kritis**Tawarkan opsi saham perusahaan untuk karyawan R&D dengan TotalWorkingYears >5.
- **Kolaborasi Edu-Content**
  Beri insentif proyek mandiri (20% waktu kerja) untuk inovasi produk edutech.
