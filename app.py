import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Calculator Profit Pariuri", layout="centered")
st.title("📊 Calculator Profit cu Mize Egale")

# CSS personalizat
st.markdown("""
    <style>
    label {
        color: green !important;
        font-weight: normal !important;
    }
    [data-baseweb="input"] input[type=number]::-webkit-outer-spin-button,
    [data-baseweb="input"] input[type=number]::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    [data-baseweb="input"] input[type=number] {
        -moz-appearance: textfield;
    }
    div.stButton > button {
        float: right;
        background-color: #28a745;
        color: white;
        border: none;
        padding: 0.5em 1em;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Etichete personalizate
labels = [
    "X / 1 & CA",
    "X / 2 & CA",
    "1 - 1 & CO",
    "12 / 12, GG & GR2",
    "12 / 12, NGG & 1.5G"
]

# Două coloane: input și rezultate
col_input, col_result = st.columns(2)

with col_input:
    cote = []
    for i in range(len(labels)):
        cota = st.number_input(f"{labels[i]}", min_value=1.01, format="%.2f", step=None, key=f"cot
