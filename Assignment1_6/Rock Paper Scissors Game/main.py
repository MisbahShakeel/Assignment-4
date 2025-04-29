import streamlit as st
import random

# Inject custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
        padding: 20px;
        border-radius: 12px;
    }
    h1 {
        color: black;
        text-align: center;
        font-size: 3em;
    }
    .stSelectbox label {
        font-weight: bold;
        font-size: 1.1em;
    }
    .stButton button {
        background-color: #6c63ff;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #574fd6;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Rock Paper Scissors Game")
st.write("Choose your option:")

# Options for the game
options = ['rock', 'paper', 'scissors']
user_choice = st.selectbox("Select your choice:", options)

if st.button("Play Game"):
    computer_choice = random.choice(options)

    def is_win(user, computer):
        return (user == 'rock' and computer == 'scissors') or \
               (user == 'paper' and computer == 'rock') or \
               (user == 'scissors' and computer == 'paper')

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif is_win(user_choice, computer_choice):
        st.balloons()
        result = "You win!"
    else:
        result = "You lose!"

    st.markdown(f"<h3>Computer chose: {computer_choice}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2>{result}</h2>", unsafe_allow_html=True)
