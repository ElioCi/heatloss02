import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

import os
import json

firebase_config = {
    'type': "service_account",
    'projectId': st.secrets['FIREBASE_PROJECT_ID'],
    'private_key_id': st.secrets['FIREBASE_PRIVATE_KEY_ID'],
    'private_key': st.secrets["FIREBASE_PRIVATE_KEY"],
    'client_email': st.secrets['FIREBASE_CLIENT_EMAIL'],
    'client_id': st.secrets['FIREBASE_CLIENT_ID'],
    'auth_uri': st.secrets['FIREBASE_AUTH_URI'],
    'token_uri':st.secrets['FIREBASE_TOKEN_URI'],
    'auth_provider_x509_cert_url': st.secrets['FIREBASE_AUTH_PROVIDER_X509_CERT_URL'],
    'client_x509_cert_url': st.secrets['FIREBASE_CLIENT_X509_CERT_URL'],
    'universe_domain': "googleapis.com"
}

cred = credentials.Certificate(firebase_config)


if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)


def app():
    
    if 'user' not in st.session_state:
            st.session_state.user = None
    
    if 'userid' not in st.session_state:
            st.session_state.userid = None
    if 'usermail' not in st.session_state:
            st.session_state.usermail = None
    if 'username' not in st.session_state:
            st.session_state.username = None

    st.title("Login")

    def f():
        try:
            user= auth.get_user_by_email(email)
            
            if user.email_verified:
            
                userid = user.uid
                usermail = user.email
                username = user.display_name
                st.session_state.user = user
                st.session_state.userid = userid
                st.session_state.usermail = usermail
                st.session_state.username = username
            
                st.success('Login Successful')
            else:
                st.warning("Email non verificata. Controlla la tua casella di posta per il link di verifica.")
                
        except Exception as e:
            st.warning(e)
    

    # Function to log out
    def logout():
        st.session_state['user'] = None
        # Additional logout steps if needed (e.g., clearing cookies)
        st.success("You have been logged out.")


    email= st.text_input("Enter your email")
    password= st.text_input("Enter your password", type= 'password')

    st.button('Login', on_click= f)

    if st.session_state['user'] != None:
        st.sidebar.write(f'Welcome *{st.session_state["username"]}*')
        #st.sidebar.write(f'user id: *{st.session_state["userid"]}*')
        st.sidebar.write(f'email: *{st.session_state["usermail"]}*')

        st.sidebar.button("Logout", on_click= logout)
    
    
    
        
        
        
    





