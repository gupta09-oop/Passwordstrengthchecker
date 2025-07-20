# 🔐 PhishProof Password Strength Checker

Welcome to the **PhishProof Password Strength Checker**, a cybersecurity-focused tool built to help users evaluate the strength of their passwords using both local logic and live breach data. This project is part of a broader security toolkit aimed at promoting safer online habits—perfect for security students, ethical hackers, and curious developers alike.

---

## ⚙️ Features

- 📏 Checks for minimum password length (12+ characters)
- 🔡 Detects missing character types (uppercase, lowercase, numbers, symbols)
- 🚨 Validates passwords against real-world breach data via [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3)
- 🎯 Returns actionable feedback to improve weak passwords
- 📊 Uses a Streamlit interface for easy testing and demos

---

## 🔧 How to Run Locally

### 1. Clone the repo:

```bash
git clone https://github.com/<your-username>/phishproof-password-checker.git
cd phishproof-password-checker

2
pip install -r requirements.txt
3
streamlit run password_checker_app.py
