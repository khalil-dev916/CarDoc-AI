import streamlit as st
from app.backend import get_response

st.set_page_config(page_title='AutoDiag Assistant', layout='centered')

st.title('🛠️ Automotive Diagnostic Assistant')
st.write('Describe your car problem in English or French, and get diagnostic suggestions.')

if 'history' not in st.session_state:
    st.session_state['history'] = []

lang = st.selectbox('Choose language / Choisissez la langue', ('English', 'Français'))

user_input = st.text_input('Your Problem / Votre problème:', '')

if st.button('Get Diagnosis') and user_input.strip():
    resp = get_response(user_input, lang)
    st.session_state['history'].append((user_input, resp))

if st.session_state['history']:
    st.subheader('Conversation History')
    for msg, resp in st.session_state['history'][-5:]:
        st.write(f'**You:** {msg}')
        st.write(f'**Assistant:** {resp}')