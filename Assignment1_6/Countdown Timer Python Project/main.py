import streamlit as st
import time

# Custom CSS styling
st.markdown("""
    <style>
    .main-title {
        font-size: 50px;
        font-weight: bold;
        color: black;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtext {
        text-align: center;
        color: #555;
        margin-bottom: 1em;
    }
    .timer {
        font-size: 60px;
        font-weight: bold;
        color: black;
        text-align: center;
        margin: 20px 0;
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
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #999;
        margin-top: 2em;
    }
    </style>
""", unsafe_allow_html=True)

# Title and instructions
st.markdown('<div class="main-title">⏳ Countdown Timer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Set a timer, start the countdown, and reset when needed.</div>', unsafe_allow_html=True)

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "seconds_left" not in st.session_state:
    st.session_state.seconds_left = 0

# Start timer function
def start_timer():
    try:
        total_seconds = int(st.session_state.input_seconds)
        if total_seconds > 0:
            st.session_state.seconds_left = total_seconds
            st.session_state.running = True
        else:
            st.error("Please enter a positive number.")
    except ValueError:
        st.error("Please enter a valid number.")

# Reset timer function
def reset_timer():
    st.session_state.running = False
    st.session_state.seconds_left = 0

# Input and buttons
st.text_input("Enter countdown time in seconds:", value="60", key="input_seconds")
col1, col2 = st.columns(2)
with col1:
    st.button("▶️ Start Timer", on_click=start_timer)
with col2:
    st.button("🔄 Reset Timer", on_click=reset_timer)

# Countdown logic
if st.session_state.running and st.session_state.seconds_left > 0:
    timer_placeholder = st.empty()
    while st.session_state.seconds_left > 0:
        mins, secs = divmod(st.session_state.seconds_left, 60)
        hrs, mins = divmod(mins, 60)
        timer_display = f"{hrs:02}:{mins:02}:{secs:02}"
        timer_placeholder.markdown(f'<div class="timer">⏱️ {timer_display}</div>', unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.seconds_left -= 1
    st.session_state.running = False
    timer_placeholder.markdown('<div class="timer">⏰ Time\'s up!</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ by [Your Name]</div>', unsafe_allow_html=True)
