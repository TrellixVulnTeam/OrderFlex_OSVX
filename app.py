import streamlit as st
import streamlit_authenticator as stauth
from multiapp import MultiApp
from apps import home, new, model # import your app modules here

app = MultiApp()
st.set_page_config(page_title="OrderFlex", page_icon="📢", layout="wide")
col1, col2, col3 = st.columns(3)

col2.title("📢 OrderFlex")

names = ['John Smith','Rebecca Briggs','Luis Filipe']
usernames = ['jsmith','rbriggs','luis']
passwords = ['123','456','1995']

hashed_passwords = stauth.Hasher(passwords).generate()


authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

with col2:
    name, authentication_status, username = authenticator.login('Login','main')

    
if authentication_status:
    app.add_app("Home", home.app)
    app.add_app("Nova Order de serviço", new.app)
    app.add_app("Model", model.app)
    app.run()
elif authentication_status == False:
    col2.error('Username/password is incorrect')
elif authentication_status == None:
    col2.warning('Please enter your username and password')

