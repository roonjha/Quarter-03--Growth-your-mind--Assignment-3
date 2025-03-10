import streamlit as st
import re

#password ka function banana he.

def apna_password(password):
    print("Type your password")


#input ka variables:
password = input("Enter your password.")
apna_password(password)

#conditions k liye

if len(password) < 8:
    print("Week Password, Minimum 8 charactors required!")
    
else:
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    special_case = re.search(r"[!@#$%^&*+=]", password)
    digit = re.search(r"[0-9]", password)

if  not upper or not lower or not digit:
    print("Wrong Password, You password must contains atleast")
    print(" -1 Upper Case letter (A-Z)")
    print(" -1 Lower Case letter (a-z)")
    print(" -1 Special Case letters (A-Z)")

apna_password(password)