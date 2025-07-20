import streamlit as st
from checker import check_password_strength

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password")

if password:
    score, feedback = check_password_strength(password)
    st.write(f"🔍 Strength Score: {score}/6")

    if feedback:
        for item in feedback:
            st.warning(item)
    else:
        st.success("This is a strong password!")
