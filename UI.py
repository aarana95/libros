import streamlit as st
#import cv2
#import matplotlib.pyplot as plt
#import numpy as np
import safaribooks as sb
import argparse
import sys
args = argparse.Namespace()

args.kindle = False
args.log = False
args.login = False
args.no_cookies = False

st.title('Estamos probando')

user = st.text_input("Usuario:", value="")
password = st.text_input("Contraseña:", value="", type="password")



credentials = user + ":" + password

if st.button("Login"):
    args.cred = sb.SafariBooks.parse_cred(credentials)
    libro = sb.SafariBooks(args)
    st.write(args.cred)

#De momento por defecto
    args.bookid = st.text_input("Código del libro:", value="")
    sys.stdout.write("funciona?")
    if st.button("Descargar libro"):
        sys.stdout.write("funciona?")
        libro.descargar_libro(args)