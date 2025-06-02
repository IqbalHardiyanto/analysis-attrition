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

Sumber data: terdapat pada folder "model"

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

link demo aplikasi attrition employee [Streamlit app](https://analysis-attrition-fvjimsfbcynw44559cnpxs.streamlit.app/)

---

## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

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
  - WorkLifeBalance ≤ 2
  - YearsSinceLastPromotion = 0 meski masa kerja >3 tahun
- **Prediksi akurat**: Model ML (Random Forest) mencapai **akurasi >80%** dalam identifikasi karyawan berpotensi resign

---

## Rekomendasi Action Items

##### 🚀 **Segera Implementasi**

- **Program "Flexi-Work"** Berikan WFH 2 hari/minggu untuk karyawan dengan DistanceFromHome >10 km (terdampak 34% karyawan).
- **Penyesuaian Kompensasi**Naikkan gaji 10–15% untuk peran kritis di R&D dengan MonthlyIncome <$5000 (17% karyawan).
- **Career Path Transparan**
  Buat kebijakan promosi wajib tiap 2 tahun (tertarget ke 31% karyawan stagnan).

##### 📈 **Strategi Jangka Menengah**

- **Redesign Peran Sales**Kurangi beban kerja non-essential (misal: administrasi) untuk tim Sales yang OverTime >20%.
- **Wellness Program**Luncurkan subsidi konseling & fitness tracker untuk karyawan WorkLifeBalance ≤2.
- **Skill Development**
  Berikan sertifikasi tech/edtech gratis bagi karyawan dengan TrainingTimesLastYear <2.

##### 💡 **Strategi Inovatif**

- **Equity untuk Talent Kritis**Tawarkan opsi saham perusahaan untuk karyawan R&D dengan TotalWorkingYears >5.
- **Kolaborasi Edu-Content**
  Beri insentif proyek mandiri (20% waktu kerja) untuk inovasi produk edutech.
