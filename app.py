# app.py — Main entry point for Flip2Grade

import streamlit as st
import pandas as pd
from flip_score import calculate_flip_score
from image_grading import analyze_card_image
from gpt_assistant import ask_gpt_advisor

st.set_page_config(page_title="Flip2Grade", layout="wide")
st.title("📈 Flip2Grade – AI-Powered Card Flip Analyzer")

st.sidebar.header("🔍 Search & Flip")
search_query = st.sidebar.text_input("Enter card name (e.g. Elly De La Cruz PSA 10)", "2024 Bowman Chrome Jackson Holliday")
raw_price = st.sidebar.number_input("Raw card price ($)", min_value=1.0, value=20.0)
psa10_price = st.sidebar.number_input("Recent PSA 10 price ($)", min_value=1.0, value=60.0)
grading_fee = st.sidebar.number_input("Grading fee ($)", min_value=0.0, value=20.0)

if st.sidebar.button("💰 Calculate Flip Score"):
    score, profit = calculate_flip_score(raw_price, psa10_price, grading_fee)
    st.metric(label="Estimated Flip Profit", value=f"${profit:.2f}", delta=f"Flip Score: {score}/100")

st.header("🧠 Upload a Card Image for Grading Estimate")
uploaded_file = st.file_uploader("Upload a clear image of the front of your raw card")
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Card", use_column_width=True)
    grade, centering = analyze_card_image(uploaded_file)
    st.success(f"Estimated Grade: PSA {grade} | Centering: {centering}")

st.header("💬 Ask the GPT Card Advisor")
user_question = st.text_input("Ask something like: 'What are the best 2024 Bowman Chrome rookies to flip?'")
if user_question:
    response = ask_gpt_advisor(user_question)
    st.info(response)
