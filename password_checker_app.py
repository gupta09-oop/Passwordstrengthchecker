import re
import hashlib
import requests
import streamlit as st

# ------------ Core Logic ------------
def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("📏 Use at least 12 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password): strength += 1
    else: feedback.append("🔠 Add uppercase letters.")

    # Lowercase check
    if re.search(r"[a-z]", password): strength += 1
    else: feedback.append("🔡 Add lowercase letters.")

    # Number check
    if re.search(r"[0-9]", password): strength += 1
    else: feedback.append("🔢 Include numbers.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): strength += 1
    else: feedback.append("💥 Include special characters.")

    # Breach check via HaveIBeenPwned
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    if is_password_breached(sha1):
        feedback.append("🚨 This password has appeared in data breaches.")
    else:
        strength += 1

    return strength, feedback

def is_password_breached(sha1_hash):
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        return suffix in response.text
    except:
        return False  # Safe default if API fails

# ------------ Streamlit UI ------------
st.set_page_config(page_title="PhishProof Password Checker", page_icon="🔐")
st.title("🔐 PhishProof Password Strength Checker")

password = st.text_input("Enter a password to test its strength")

if password:
    score, feedback = check_password_strength(password)
    st.markdown(f"**🔍 Strength Score:** `{score} / 6`")

    if feedback:
        for msg in feedback:
            st.warning(msg)
    else:
        st.success("✅ This password is strong!")
