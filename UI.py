import streamlit as st
#import cv2
#import matplotlib.pyplot as plt
#import numpy as np
import safaribooks as sb

st.title('Estamos probando')
user = st.text_input("Usuario:", value="")
password = st.text_input("Contraseña:", value="", type="password")
code = st.text_input("Código del libro:", value="")


credentials = user + ":" + password

parsed_cred = sb.SafariBooks.parse_cred(credentials)
st.write(parsed_cred)
if not parsed_cred:
    st.write("Mal metido " + user + " o contraseña: " + password)

#@SafariBooks(args_parsed)