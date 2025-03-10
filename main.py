import streamlit as st
import re

# Password checking function
def check_password_strength(password):
    messages = []  # To collect messages
    
    if len(password) < 8:
        messages.append("❌ Weak Password! Minimum 8 characters required!")
    else:
        upper = re.search(r"[A-Z]", password)
        lower = re.search(r"[a-z]", password)
        special_case = re.search(r"[!@#$%^&*+=]", password)
        digit = re.search(r"[0-9]", password)

        # Collect issues if missing
        if not upper:
            messages.append(" Add at least 1 Uppercase letter (A-Z)")
        if not lower:
            messages.append(" Add at least 1 Lowercase letter (a-z)")
        if not digit:
            messages.append(" Add at least 1 Digit (0-9)")
        if not special_case:
            messages.append(" Add at least 1 Special Character (!@#$%^&*+=)")

        # If no issues, it's a strong password
        if upper and lower and digit and special_case:
            messages.append("✅🔒 Strong Password! Well done!")

    return messages

# Streamlit GUI
st.title(" Password Strength Meter")

password = st.text_input("Enter your password:")

if password:  # If user entered something
    result = check_password_strength(password)
    for msg in result:
        st.write(msg)
