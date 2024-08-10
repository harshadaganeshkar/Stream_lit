import streamlit as st
import pandas as pd
import json

# Load previous data
def load_data():
    try:
        with open('skill_swap_data.json', 'r') as file:
            data = json.load(file)
            return pd.DataFrame(data)
    except FileNotFoundError:
        return pd.DataFrame(columns=['username', 'offer', 'request'])

def save_data(df):
    with open('skill_swap_data.json', 'w') as file:
        json.dump(df.to_dict(orient='records'), file)

# Page configuration
st.set_page_config(page_title="SkillSwap", page_icon="🤝")

# App title
st.title("SkillSwap Platform")

# User input for registration
st.header("Register Your Skill Swap Offer")
username = st.text_input("Enter your username")
offer = st.text_input("What skill can you offer?")
request = st.text_input("What skill would you like to learn?")

if st.button("Submit"):
    if username and offer and request:
        # Load existing data
        df = load_data()
        # Add new entry
        new_entry = pd.DataFrame([[username, offer, request]], columns=['username', 'offer', 'request'])
        df = pd.concat([df, new_entry], ignore_index=True)
        # Save updated data
        save_data(df)
        st.success("Your skill swap offer has been posted!")
    else:
        st.error("Please fill out all fields.")

# Display available offers and requests
st.header("Browse Skill Swap Offers")
df = load_data()
if not df.empty:
    st.write(df)
else:
    st.write("No skill swap offers available yet.")

# Run the Streamlit app
if __name__ == "__main__":
    st.write("Run this file using `streamlit run [filename.py]`")
