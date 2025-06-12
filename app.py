import streamlit as st
import joblib

model = joblib.load('xgboost_best_model.pkl')

st.set_page_config(page_title="📰 News Detector", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stTextArea textarea {
            background-color: #ffffff;
            border: 1px solid #ced4da;
            border-radius: 0.5rem;
            font-size: 1rem;
        }
        .stButton>button {
            color: white;
            background-color: #0d6efd;
            border-radius: 5px;
            height: 3em;
            width: 10em;
            font-size: 1.1em;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color: #0d6efd;'>📰 News Classification App</h1>", unsafe_allow_html=True)
st.write("Enter a news article below and click Predict to see if it's real or fake.")


user_input = st.text_area("Enter News Article", height=200)

if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to classify.")
    else:
        prediction = model.predict([user_input])[0]

        if prediction == 0:
            st.success("This news appears to be **REAL**.", icon="✅")
        else:
            st.error("This news appears to be **FAKE**.", icon="🚨")