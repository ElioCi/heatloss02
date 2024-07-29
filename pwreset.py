import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

    def send_reset_email(to_email, reset_link):
        from_email = "solvingvv@gmail.com"  # Your email address
        from_password = "ocfa uypo udbb hsfy"  # Your email password
        subject = "Reset Your Password"
        body = f"Click the link to reset your password: {reset_link}"
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Your SMTP server
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            st.error(f"Error sending email: {e}")
            return False

    st.title("Reset Password")

    email = st.text_input("Enter your email address")

    if st.button("Send Password Reset Email"):
        if email:
            try:
                # Generate the password reset link
                reset_link = auth.generate_password_reset_link(email)
                
                # Send the link via email (requires setting up an email service)
                if send_reset_email(email, reset_link):
                    st.success("Password reset email sent! Please check your inbox.")
                else:
                    st.error("Failed to send password reset email. Please try again later.")
            except firebase_admin.auth.UserNotFoundError:
                st.error("No user found with this email address.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter your email address.")




