import streamlit as st
import random

st.title("🎯 Guess the Number Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Initialize session state variables
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Input from the user
guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

# Guess button
if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

# Restart game
if st.button("Play Again"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.experimental_rerun()

# Show attempts and score
st.write(f"You have made {st.session_state.attempts} attempts.")