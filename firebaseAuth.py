import streamlit as st

import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("heatloss-69a51-firebase-adminsdk-d8rr6-d86c640f76.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

#firebaseConfig = {
#  'apiKey': "AIzaSyB9kjl2i6X3RMv7xIZqQjSAv8JhAKQCEmo",
#  'authDomain': "heatloss-69a51.firebaseapp.com",
#  'projectId': "heatloss-69a51",
#  'storageBucket': "heatloss-69a51.appspot.com",
#  'messagingSenderId': "246578931349",
#  'appId': "1:246578931349:web:ae3b604548bd298557dd9c",
#  'measurementId': "G-SVDZVFQSB8"
#}
#firebase= pyrebase.initialize_app(firebaseConfig)
#auth = firebase.auth()
#db= firebase.database()
#storage= firebase.storage()

#Authentication
#Login

st.title("test login/signup")
choice = st.selectbox('Login/Signup', ['Login', 'Signup', 'Logout'])

def f():
    try:
        user= auth.get_user_by_email(email)
        userid = user.uid
        print(userid)
        st.success('Login Successful')
    except Exception as e:
        st.warning(e)



def r():
        
    try:
        user= auth.create_user(email= email, password= password)
        st.success('Account created successfully!')
        st.markdown('Please Login using your email and password')
        st.balloons()
    except Exception as e:
        st.warning(e)



if choice== 'Login':
    email= st.text_input("Enter your email")
    password= st.text_input("Enter your password", type= 'password')

    st.button('Login', on_click= f)


    

else:
    email= st.text_input("Enter your email")
    password= st.text_input("Enter your password", type= 'password')
    username= st.text_input("Enter your unique username")

    st.button('create my account', on_click= r)
        





