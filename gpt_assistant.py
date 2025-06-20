# gpt_assistant.py – Updated for openai>=1.0.0

import openai
import streamlit as st

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def ask_gpt_advisor(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling GPT: {e}"
