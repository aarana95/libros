import streamlit as st
#import cv2
#import matplotlib.pyplot as plt
#import numpy as np
import safaribooks as sb
import argparse
import sys
import SessionState
import webbrowser
args = argparse.Namespace()

args.kindle = False
args.log = False
args.login = False
args.no_cookies = False


def main(args):
    text_file = open("Books/Output.txt", "w")
    text_file.write("Purchase Amount")
    text_file.close()
    #st.markdown(href = f'<a href="data:Books">Download csv file</a>', unsafe_allow_html=True)

    if st.button("descargar"):
        webbrowser.open("Books/Output.txt")

    session_state = SessionState.get(name="", button_start=False)

    st.title('Estamos probando')

    session_state.user = st.text_input("Usuario:", value="")
    session_state.password = st.text_input("Contraseña:", value="", type="password")

    credentials = session_state.user + ":" + session_state.password

    st.write(hasattr(session_state, 'login_button'))
    st.write(session_state.password)
    st.write(hasattr(session_state, 'password'))
    if not hasattr(session_state, 'login_button') or (session_state.user == '' or session_state.password == '' or not session_state.login_button):
        session_state.login_button = st.button("Login")

    if session_state.login_button:
        args.cred = sb.SafariBooks.parse_cred(credentials)
        session_state.libro = sb.SafariBooks(args)
        st.write(args.cred)

        args.bookid = st.text_input("Código del libro:", value="")


        if st.button("Descargar libro"):
            sys.stdout.write("funciona?")
            session_state.libro.descargar_libro(args)

main(args)