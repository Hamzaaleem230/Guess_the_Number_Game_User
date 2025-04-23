# guess_the_number.py
import random
import streamlit as st

st.set_page_config(page_title="Guess the Number", page_icon="🎯")

st.title("🎯 Guess the Number Game")

# Initialize the random number in session_state if not already done
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""

# Input from the user
guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, key="guess_input")

# Submit button
if st.button("Submit"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.session_state.message = "🔻 Too low! Try again."
    elif guess > st.session_state.number:
        st.session_state.message = "🔺 Too high! Try again."
    else:
        st.session_state.message = f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} tries."

# Display the message
if st.session_state.message:
    if "Congratulations" in st.session_state.message:
        st.success(st.session_state.message)
    else:
        st.info(st.session_state.message)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Hamza Syed")

# Check out the output
# https://guessthenumbergameuser-8fvcmzv4zdtfre4m4xyddg.streamlit.app/
