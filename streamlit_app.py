import streamlit as st 

st.set_page_config(
    page_title='Super App!',
    page_icon=':ice_cream:', # This is an emoji shortcode. Could be a URL too.
)

# Set the app title 
st.title('My First Streamlit App') 
# Add a welcome message 
st.markdown('Welcome to my :red[Streamlit] app!') 
# Create a text input 
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
st.write('Customized Message:', user_input)
