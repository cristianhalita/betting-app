import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculator Profit Pariuri", layout="centered")
st.title("📊 Calculator Profit cu Mize Optime")

st.markdown("Introdu cele 5 variante de pariu și o miză totală. Apasă 'Calculează' pentru a vedea mizele optime și profitul net egalizat.")

# CSS pentru etichete verzi și ascunderea butoanelor +/- din inputuri
st.markdown("""
    <style>
    label, div[data-testid="stNumberInput"] > div > div > input {
        color: green !important;
    }
    /* Ascunde butoanele +/- */
    [data-testid="stNumberInput"] input::-webkit-outer-spin-button,
    [data-testid="stNumberInput"] input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    [data-testid="stNumberInput"] input[type=number] {
        -moz-appearance: textfield;
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

# Inputuri pentru cote (afișate vertical)
cote = []
for i in range(len(labels)):
    st.markdown(f"**{labels[i]}**")
    cota = st.number_input("", min_value=1.01, format="%.2f", key=f"cota_{i}", step=None)
