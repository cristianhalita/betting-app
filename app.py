import streamlit as st
import numpy as np

st.set_page_config(page_title="SRS - Betting System", layout="centered")
st.title("SRS - Betting System")

# CSS: etichete verzi, fără bold, fără butoane +/-, buton Calculează aliniat dreapta
st.markdown("""
    <style>
    /* Verde simplu pentru etichete */
    label {
        color: green !important;
        font-weight: normal !important;
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
    /* Buton verde aliniat dreapta */
    div.stButton > button {
        float: right;
        background-color: #28a745;
        color: white;
        border: none;
        padding: 0.5em 1em;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Etichete personalizate
labels = [
    "X/1 & CARDS",
    "X/2 & CARDS",
    "1-1 & CORNERS",
    "12/12, GG & GR2",
    "12/12, NGG & 1.5G"
]

# Inputuri pentru cote
cote = []
for i in range(len(labels)):
    cota = st.number_input(f"{labels[i]}", min_value=1.01, format="%.2f", step=None, key=f"cota_{i}")
    cote.append(cota)

# Input pentru miza totală
miza_totala = st.number_input("Miza totală", min_value=1.0, format="%.2f", step=None, key="miza_total")

# Buton Calculează
if st.button("Calculează"):
    if all(c > 1.0 for c in cote) and miza_totala > 0:
        inv_sume = sum(1 / c for c in cote)
        castig_comun = miza_totala / inv_sume
        mize_optime = [castig_comun / c for c in cote]
        profituri = [castig_comun - m for m in mize_optime]

        st.subheader("📈 Rezultate")
        st.write("Câștig brut comun:", round(castig_comun, 2), "RON")

        table_data = {
            "Variantă": labels,
           "Miză optimă (RON)": [f"{m:.2f}" for m in mize_optime],
    "Profit net (RON)": [f"{p:.2f}" for p in profituri]
        }

        st.table(table_data)
        st.success("Calcule realizate cu succes!")
    else:
        st.error("Te rog completează toate cotele (>1.0) și miza totală (>0).")
