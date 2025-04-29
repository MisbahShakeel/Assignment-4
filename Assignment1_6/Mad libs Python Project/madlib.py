import streamlit as st

# Inject CSS
st.markdown("""
    <style>
    .title {
        font-size: 50px;
        font-weight: bold;
        font-family: 'sans-serif';
        color: black;
        text-align: center;
    }
    .instructions {
        margin-top: 14px;
        font-size: 20px;
        color: #555;
        text-align: center;
    }
    .story {
        margin-top: 24px;
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        font-size: 22px;
        color: #333;
        text-align: center;
    } 
    div.stButton > button {
        background-color: #FF5733;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    
    div.stButton > button:hover {
        background-color: #C70039;
        color: black;
    </style>
""", unsafe_allow_html=True)

# Now your normal Streamlit code
st.markdown('<div class="title">😆 Mad Lib Game</div>', unsafe_allow_html=True)
st.markdown('<div class="instructions">Fill in the blanks to create a funny story!</div>', unsafe_allow_html=True)

# Inputs
adj = st.text_input("Enter an adjective:")
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
verb2 = st.text_input("Enter another verb:")
adverb = st.text_input("Enter an adverb:")

# Button
if st.button("Generate Mad Lib"):
    if adj and noun and verb and verb2 and adverb:
        mad_lib = f"""Coding is so {adj}! It makes me want to {verb} all day. 
        I love to do {verb2} and {adverb} code. I can't wait to learn more! 
        I want to be a {noun} when I grow up."""
        st.markdown(f'<div class="story">{mad_lib}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please fill in all fields!")
