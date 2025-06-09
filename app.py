import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculator Profit Pariuri", layout="centered")
st.title("📊 Calculator Profit cu Mize Egale")

# CSS: verde etichete, fără bold, fără butoane +/-
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

labels = [
    "X / 1 & CA",
    "X / 2 & CA",
    "1 - 1 & CO",
    "12 / 12, GG & GR2",
    "12 / 12, NGG & 1.5G"
]

# Colectăm inputurile
cote = []
mize_optime = []
profituri = []
calculeaza = False

st.subheader("📥 Introdu datele")

for i in range(len(labels)):
    cota = st.number_input(f"{labels[i]}", min_value=1.01, format="%.2f", step=None, key=f"cota_{i}")
    cote.append(cota)
    st.markdown(f"<div id='miza_{i}'></div>", unsafe_allow_html=True)  # loc pentru miză calculată

miza_totala = st.number_input("Miza totală (RON)", min_value=1.0, format="%.2f", step=None, key="miza_total")

# Buton
calculeaza = st.button("✅ Calculează")

# Calcul și afișare sub fiecare input
if calculeaza:
    if all(c > 1.0 for c in cote) and miza_totala > 0:
        inv_sume = sum(1 / c for c in cote)
        castig_comun = miza_totala / inv_sume
        mize_optime = [castig_comun / c for c in cote]
        profituri = [castig_comun - m for m in mize_optime]

        st.markdown("### 📈 Rezultate")
        st.write(f"**Câștig brut comun:** `{round(castig_comun, 2)} RON`")
        
        for i in range(len(labels)):
            st.markdown(
                f"<div style='margin-top:-20px; margin-bottom:20px; color:#28a745;'>"
                f"Miză optimă: <b>{round(mize_optime[i], 2)} RON</b><br>"
                f"Profit net: <b>{round(profituri[i], 2)} RON</b>"
                f"</div>",
                unsafe_allow_html=True
            )
        st.success("Calcule realizate cu succes!")
    else:
        st.error("Completează toate cotele (>1.0) și miza totală (>0).")
