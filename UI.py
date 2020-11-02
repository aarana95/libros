import streamlit as st
#import cv2
#import matplotlib.pyplot as plt
#import numpy as np
import safaribooks as sb
import argparse

args = argparse.Namespace()

st.title('Estamos probando')
user = st.text_input("Usuario:", value="")
password = st.text_input("Contraseña:", value="", type="password")
args.bookid = st.text_input("Código del libro:", value="")


credentials = user + ":" + password

args.cred = sb.SafariBooks.parse_cred(credentials)

if not args.cred:
    st.write("Mal metido " + user + " o contraseña: " + password)
st.write(args)

sb.SafariBooks(args)