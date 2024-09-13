import streamlit as st 

st.set_page_config(
    page_title='Super App!',
    page_icon=':ice_cream:', # This is an emoji shortcode. Could be a URL too.
)

url = "https://www.streamlit.io"

# Set the app title 
st.markdown('# My First :red[Streamlit] App') 
# Add a welcome message 
st.markdown('Welcome to my [Streamlit](%s) app!' % url) 
# Create a text input 
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
st.write('Customized Message:', user_input)

color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.markdown('My favorite :%s[color] is' % color)
