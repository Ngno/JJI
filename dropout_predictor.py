#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import joblib

#######################
# Page configuration
st.set_page_config(
    page_title="Dropout Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# PREPARE DATA
# Load the dataset
data_url = "https://raw.githubusercontent.com/Ngno/JJI/main/df_dashboard%20.csv"
df = pd.read_csv(data_url,  delimiter=',', encoding='utf-8')

df_model_url = "https://raw.githubusercontent.com/Ngno/JJI/main/df_model.csv"
df_model = pd.read_csv(df_model_url, delimiter=',', encoding='utf-8')

# Define columns for numeric input
numeric_columns = [
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade",
    "Age_at_enrollment",
    "Curricular_units_2nd_sem_enrolled",
    "Admission_grade",
    "Curricular_units_2nd_sem_evaluations",
    "Previous_qualification_grade",
    "Curricular_units_2nd_sem_without_evaluations",
    "GDP"
]

# Define columns for one-hot encoding (categorical columns)
categorical_columns = [
    "Status",
    "Application_mode",
    "Gender",
    "Course",
    "Mothers_qualification",
    "Marital_status",
    "Mothers_occupation"
]

# Define binary columns and their notes
binary_columns = {
    "Tuition_fees_up_to_date": "(1=Yes, 0=No)",
    "Scholarship_holder": "(1=Yes, 0=No)",
    "Debtor": "(1=Yes, 0=No)",
    "Gender": "(1=Male, 0=Female)"
}


######################

# Navigation Sidebar
st.sidebar.title("Welcome!")


#######################

# Render functions
# Justify text function
def render_justified_text(text):
    st.markdown(
        f"""
        <style>
        .justified-text {{
            text-align: justify;
        }}
        </style>
        <div class="justified-text">
        {text}
        </div>
        """, 
        unsafe_allow_html=True
    )    


#########   
# 'Prediction' page render function
rf_model = joblib.load('rf_model.joblib')
scaler = joblib.load('scaler.joblib')
model_one_hot_columns = joblib.load('model_one_hot_columns.joblib')

# 'Prediction' page render function
def render_prediction_page(df):
    st.title("Dropout Predictor")
    st.write("Predict student dropout based on student's profile.")
    st.write("Provide the student's details below and click 'Predict' to determine the likelihood of dropout.")

    input_data = {}

    # Split into two columns
    col1, col2 = st.columns(2)

    # Input controls for all columns (numeric and categorical)
    for idx, col in enumerate(df_model.columns):
        if col == 'Status':
            continue 
        
        with (col1 if idx % 2 == 0 else col2):
            if col in numeric_columns:
                input_data[col] = st.number_input(f"Enter {col}:", key=col)
            elif col in binary_columns:
                input_data[col] = st.selectbox(f"Select value for {col} {binary_columns[col]}:", options=[0, 1], key=col)
            else:
                unique_values = df_model[col].unique()
                input_data[col] = st.selectbox(f"Select value for {col}:", unique_values, key=col)

    if st.button("Predict"):
        # Encode the input data
        input_df = pd.DataFrame([input_data])
        input_encoded = pd.get_dummies(input_df, columns=model_one_hot_columns, drop_first=True, dtype=int)

        # Ensure the input data has the same columns as the training data
        missing_cols = set(scaler.get_feature_names_out()) - set(input_encoded.columns)
        for col in missing_cols:
            input_encoded[col] = 0
        input_encoded = input_encoded[scaler.get_feature_names_out()]

        # Standardize the data (if needed)
        input_scaled = scaler.transform(input_encoded)

        # Use the trained model to predict
        y_pred_user = rf_model.predict(input_scaled)
        dropout_probability = rf_model.predict_proba(input_scaled)[0][1]

        # Display prediction results
        st.write(f"Predicted Dropout: {'Yes' if y_pred_user[0] else 'No'}")
        st.write(f"Dropout Probability: {dropout_probability * 100:.2f}%")


# Add text footer at the sidebar
st.sidebar.markdown(
    """
    <div style="height: 100px;"></div> <!-- Empty div with specified height -->
    <div style="text-align: center; font-size: small; color: grey;">
        &copy; 2024 Anggi Novitasari. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)
######################################################################

# STREAMLIT DEPLOYMENT
render_prediction_page(df_model)

######################################################################