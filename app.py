import streamlit as st
import joblib

st.title("📧 Email Spam Classifier")

try:
    model = joblib.load("spam_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.write("Enter an email message to check if it is spam.")

email = st.text_area("Email Text")

if st.button("Check Spam"):
    email_vector = vectorizer.transform([email])
    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        st.error("🚨 Spam Email")
    else:
        st.success("✅ Not Spam")