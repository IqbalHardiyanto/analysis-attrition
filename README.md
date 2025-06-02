# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan edutech **Jaya Jaya Maju** bergerak di bidang pendidikan berbasis teknologi dengan fokus pada pengembangan produk digital, konten edukasi, dan layanan pembelajaran. Sumber daya manusia (khususnya talenta teknis dan akademik) merupakan aset. Tren attrition yang tinggi dapat mengganggu keberlanjutan pengembangan produk, pengalaman pengguna, dan inovasi kurikulum. Industri edutech yang kompetitif juga membuat retensi talenta menjadi penentu keunggulan bisnis.

---

### Permasalahan Bisnis

1. **Tingkat Attrition Tinggi:** Karyawan mengalami attrition, terutama di departemen R&D dan Sales.
2. **Ketidakpuasan Lingkungan Kerja:** Karyawan melaporkan EnvironmentSatisfaction rendah (skor 1).
3. **Work-Life Balance Buruk:** Karyawan memiliki WorkLifeBalance ≤2 (skala 4), terutama yang sering business travel.
4. **Stagnasi Karir:** Karyawan dengan masa kerja >3 tahun tidak pernah dipromosikan (YearsSinceLastPromotion=0).
5. **Ketimpangan Kompensasi:** Kesenjangan pendapatan bulanan (MonthlyIncome) mencapai 300% antara level junior dan senior.
6. **Beban Kerja Tidak Seimbang:** Karyawan rutin lembur (OverTime=Yes), terutama di Sales.

---

### Cakupan Proyek

| Area Analisis              | Metodologi                                                       | Output Target                         |
| -------------------------- | ---------------------------------------------------------------- | ------------------------------------- |
| Faktor Penyebab Attrition  | EDA, Regresi Logistik                                            | Identifikasi 5 driver utama attrition |
| Segmentasi Karyawan Risiko | Klasifikasi                                                      | Pemetaan kelompok berisiko tinggi     |
| Prediksi Attrition         | Model Machine Learning (Logistic Regression, Random Forest, SVM) | Akurasi prediksi > 80%                |
| Analisis Kepuasan          | Korelasi                                                         | Rekomendasi peningkatan prioritas     |
| Simulasi Kebijakan         | Analisis What-If                                                 | Estimasi program retensi              |

---

### Persiapan

Sumber data: ....

Setup environment:

```

```

---

## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

---

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

---

### Rekomendasi Action Items

#### 🚀 **Segera Implementasi (Quick Wins)**

- **Program "Flexi-Work"**Berikan WFH 2 hari/minggu untuk karyawan dengan DistanceFromHome >10 km (terdampak 34% karyawan).
- **Penyesuaian Kompensasi**Naikkan gaji 10–15% untuk peran kritis di R&D dengan MonthlyIncome <$5000 (17% karyawan).
- **Career Path Transparan**
  Buat kebijakan promosi wajib tiap 2 tahun (tertarget ke 31% karyawan stagnan).

#### 📈 **Strategi Jangka Menengah**

- **Redesign Peran Sales**Kurangi beban kerja non-essential (misal: administrasi) untuk tim Sales yang OverTime >20%.
- **Wellness Program**Luncurkan subsidi konseling & fitness tracker untuk karyawan WorkLifeBalance ≤2.
- **Skill Development**
  Berikan sertifikasi tech/edtech gratis bagi karyawan dengan TrainingTimesLastYear <2.

#### 🔍 **Inisiatif Berbasis Data**

- **Sistem Early Warning Attrition**Bangun dashboard real-time dengan parameter:`EnvironmentSatisfaction <2, JobInvolvement <3, YearsSinceLastPromotion >3`.
- **"Stay Interview"**
  Wawancara rutin dengan karyawan berisiko tinggi (output model prediktif).

#### 💡 **Strategi Inovatif**

- **Equity untuk Talent Kritis**Tawarkan opsi saham perusahaan untuk karyawan R&D dengan TotalWorkingYears >5.
- **Kolaborasi Edu-Content**
  Beri insentif proyek mandiri (20% waktu kerja) untuk inovasi produk edutech.
