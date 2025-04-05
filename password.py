#🔐 project 02: password strenght meter sir zia project 3

#📌 Objective:
#build a password strenght meter in python that evalutes a user's password based on securtiy rules.
#The program will:

# ANalize passwords based on lenght, character, types, and patterns,
#Assing a strenght score(weak,moderate,strong).
#provide feedback to weak passwords.
#use control flow, type casting, strings and function.

# 🔵 Requirments

#1. password strenght criteria

#A strong password should:
#✅ Be at least 8 character long
#✅ contain upercase and lowercase letters
#✅include at least one digit(8-9)
#✅ Have one special character (!@#$%^&*)

#2. Scoring system
# Weak (score: 1-2) - Short, missing key elements
# Moderate (score: 3-4) - Good but missing some security features
# Strong (score: 5-6) - Meets all criteria

#3.feedback system

#If the password is weak, suggest improvments.
#If the password is strong, display a success message.


import re
import streamlit as st

# page styleing 
st.set_page_config(page_title="password strenght checker", page_icon="🌘", layout="centered")
# custom css
st.markdown("""
<style>
    .main{text-aling: center;}
    .stTextInput {widht:60% !important; margin:} 
    .stButton button{widht: 50%; background-color #4CAF50; color: white; font-size: 18px; }
    .stButton button: hover{ background-color: #45a049; }
</style>             
""", unsafe_allow_html=True)

# page tilte and discription
st.title("🔒 Password strenght Gentretar")
st.write("Enter your password below to check its security level. 🔍")

# function to check password
def check_password_strenght(password):
    score=0
    feedback = []

    if len(password)>= 8:
        score += 1 #increment score by 1
    else:
        feedback.append(" ❌ password should be **atleast 0 character long**")
            
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append(" ❌ password  should include **both upercase (A-Z) and lowercase (a-z) letters** .")
         
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" ❌ password should include **atleast one number (0-9) **.")

#special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append(" ❌ Include **at least one special character [!@#$%^&*]**.")


# display password strenght results
    if score == 4:
        st.success("✅ **strong password** - your password is secure.") 
    elif score == 3:
        st.info("⚠️ **Moderate password** - Consider improving security by adding more feature.")
    else:
        st.error("❌ **weak password** - Follow the suggestion below to strenght it.")

#feedback
    if feedback:
        with st.expander("🔍 **Improve your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")                            

        
#Button working
if st.button("check password"):
    if password:
        check_password_strenght(password)
    else:
        st.warning(" ⚠️ please enter a password first! ")  #show warning if password empty            


