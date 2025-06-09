import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculator Profit Pariuri", layout="centered")
st.title("📊 Calculator Profit cu Mize Egale")

# CSS: etichete verzi, fără bold, fără +/-
st.markdown("""
    <style>
    /* Verde simplu pentru etichete */
    label {
        color: green !important;
        font-weight: normal !important;
    }
    /* Eliminare butoane +/- din number_input */
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

# Etichete exact cum ai cerut
labels = [
    "X / 1 & CA",
    "X / 2 & CA",
    "1 - 1 & CO",
    "12 / 12, GG & GR2",
    "12 / 12, NGG & 1.5G"
]

# Cote verticale
cote = []
for i in range(len(labels)):
    cota = st.number_input(f"{labels[i]}", min_value=1.01, format="%.2f", step=None, key=f"cota_{i}")
    cote.append(cota)

# Miza totală
miza_totala = st.number_input("Miza totală (RON)", min_value=1.0, format="%.2f", step=None, key="miza_total")

# Buton Calculează aliniat dreapta
_, col_btn = st.columns([3, 1])
with col_btn:
    if st.button("✅ Calculează"):
        if all(c > 1.0 for c in cote) and miza_totala > 0:
            inv_sume = sum(1 / c for c in cote)
            castig_comun = miza_totala / inv_sume
            mize_optime = [castig_comun / c for c in cote]
            profituri = [castig_comun - m for m in mize_optime]

            st.subheader("📈 Rezultate")
            st.write("Câștig brut comun:", round(castig_comun, 2), "RON")

            table_data = {
                "Variantă": labels,
                "Miză optimă (RON)": [round(m, 2) for m in mize_optime],
                "Profit net (RON)": [round(p, 2) for p in profituri]
            }

            st.table(table_data)
            st.success("Calcule realizate cu succes!")
        else:
            st.error("Te rog completează toate cotele (>1.0) și miza totală (>0).")
