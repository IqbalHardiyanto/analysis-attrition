import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# Judul aplikasi
st.title("Employee Attrition Prediction 📊")
st.write("Aplikasi ini memprediksi kemungkinan karyawan mengalami attrition 🧑🏿‍💻")

# Load model dan preprocessor dari folder model
@st.cache_resource
def load_model(model_name):
    model_path = os.path.join('model', f'{model_name}_model.pkl')
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"Model {model_name} tidak ditemukan di folder 'model'!")
        return None

@st.cache_resource
def load_preprocessor():
    preprocessor_path = os.path.join('model', 'preprocessor.pkl')
    if os.path.exists(preprocessor_path):
        return joblib.load(preprocessor_path)
    else:
        st.error("Preprocessor tidak ditemukan di folder 'model'!")
        return None

# Pilihan model
model_names = ['LogisticRegression', 'RandomForest', 'SVM']
selected_model = st.selectbox("Pilih Model", model_names)

# Load model dan preprocessor
model = load_model(selected_model)
preprocessor = load_preprocessor()

# Cek apakah model dan preprocessor berhasil dimuat
if model is None or preprocessor is None:
    st.stop()

# Input form
st.header("Masukkan Data Karyawan")

# Fungsi untuk input data
def input_features():
    features = {}
    
    col1, col2 = st.columns(2)
    
    with col1:
        features['Age'] = st.number_input("Usia", min_value=18, max_value=65, value=30)
        features['BusinessTravel'] = st.selectbox("Frekuensi Perjalanan Bisnis", 
                                                ['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'])
        features['DailyRate'] = st.number_input("Daily Rate", min_value=100, max_value=1500, value=800)
        features['Department'] = st.selectbox("Departemen", ['Sales', 'Research & Development', 'Human Resources'])
        features['DistanceFromHome'] = st.number_input("Jarak dari Kantor (km)", min_value=1, max_value=30, value=10)
        features['Education'] = st.selectbox("Tingkat Pendidikan", 
                                           [1, 2, 3, 4, 5],
                                           format_func=lambda x: f"Level {x}")
        features['EducationField'] = st.selectbox("Bidang Pendidikan", 
                                                ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'])
        features['Gender'] = st.radio("Jenis Kelamin", ['Male', 'Female'])
        features['HourlyRate'] = st.number_input("Hourly Rate", min_value=30, max_value=100, value=60)
        
    with col2:
        features['JobInvolvement'] = st.selectbox("Tingkat Keterlibatan Kerja", 
                                                 [1, 2, 3, 4],
                                                 format_func=lambda x: f"Level {x}")
        features['JobLevel'] = st.selectbox("Tingkat Pekerjaan", [1, 2, 3, 4, 5])
        features['JobRole'] = st.selectbox("Peran Pekerjaan", 
                                         ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                          'Manufacturing Director', 'Healthcare Representative', 'Manager',
                                          'Sales Representative', 'Research Director', 'Human Resources'])
        features['JobSatisfaction'] = st.selectbox("Kepuasan Kerja", [1, 2, 3, 4])
        features['MaritalStatus'] = st.selectbox("Status Pernikahan", ['Single', 'Married', 'Divorced'])
        features['MonthlyIncome'] = st.number_input("Pendapatan Bulanan", min_value=1000, max_value=20000, value=5000)
        features['MonthlyRate'] = st.number_input("Monthly Rate", min_value=2000, max_value=30000, value=15000)
        features['NumCompaniesWorked'] = st.number_input("Jumlah Perusahaan Sebelumnya", min_value=0, max_value=10, value=2)
    
    # Lanjutan input
    col3, col4 = st.columns(2)
    
    with col3:
        features['OverTime'] = st.radio("Lembur", ['Yes', 'No'])
        features['PercentSalaryHike'] = st.slider("Persentase Kenaikan Gaji (%)", min_value=10, max_value=25, value=15)
        features['PerformanceRating'] = st.selectbox("Rating Kinerja", [1, 2, 3, 4])
        
    with col4:
        features['RelationshipSatisfaction'] = st.selectbox("Kepuasan Hubungan", [1, 2, 3, 4])
        features['StockOptionLevel'] = st.selectbox("Tingkat Opsi Saham", [0, 1, 2, 3])
        features['TotalWorkingYears'] = st.number_input("Total Tahun Bekerja", min_value=0, max_value=40, value=10)
        features['TrainingTimesLastYear'] = st.number_input("Pelatihan Tahun Lalu", min_value=0, max_value=10, value=2)
        features['WorkLifeBalance'] = st.selectbox("Keseimbangan Kerja-Hidup", [1, 2, 3, 4])
        features['YearsAtCompany'] = st.number_input("Tahun di Perusahaan", min_value=0, max_value=40, value=5)
        features['YearsInCurrentRole'] = st.number_input("Tahun di Posisi Saat Ini", min_value=0, max_value=20, value=2)
        features['YearsSinceLastPromotion'] = st.number_input("Tahun Sejak Promosi Terakhir", min_value=0, max_value=15, value=1)
        features['YearsWithCurrManager'] = st.number_input("Tahun dengan Manager Saat Ini", min_value=0, max_value=20, value=2)
    
    return pd.DataFrame([features])

# Dapatkan input data
input_df = input_features()

# Tampilkan data input
st.subheader("Data yang Dimasukkan")
st.write(input_df)

# Prediksi ketika tombol ditekan
if st.button("Prediksi Attrition"):
    try:
        # Preprocess input data
        processed_input = preprocessor.transform(input_df)
        
        # Lakukan prediksi
        prediction = model.predict(processed_input)
        prediction_proba = model.predict_proba(processed_input)
        
        # Tampilkan hasil
        st.subheader("Hasil Prediksi")
        
        attrition_prob = prediction_proba[0][1] * 100
        st.metric("Probabilitas Attrition", f"{attrition_prob:.2f}%")
        
        if prediction[0] == 1:
            st.error("Prediksi: Karyawan berpotensi mengalami attrition")
        else:
            st.success("Prediksi: Karyawan tidak berpotensi mengalami attrition")
        
        # Tampilkan probabilitas detail
        st.write("Detail Probabilitas:")
        prob_df = pd.DataFrame({
            'Kelas': ['Tidak Attrition', 'Attrition'],
            'Probabilitas': [prediction_proba[0][0]*100, prediction_proba[0][1]*100]
        })
        st.bar_chart(prob_df.set_index('Kelas'))
        
    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")

# Tampilkan informasi model yang dipilih
st.sidebar.header("Informasi Model")
st.sidebar.write(f"Model yang dipilih: {selected_model}")
if model is not None:
    st.sidebar.success("✅ Model berhasil dimuat")
else:
    st.sidebar.error("❌ Model gagal dimuat")

if preprocessor is not None:
    st.sidebar.success("✅ Preprocessor berhasil dimuat")
else:
    st.sidebar.error("❌ Preprocessor gagal dimuat")