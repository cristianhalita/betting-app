import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculator Profit Pariuri", layout="centered")
st.title("📊 Calculator Profit cu Mize Egale")

# CSS pentru etichete verzi, fără +/-, și rezultate bine spațiate
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
    .rezultat {
        margin-top: -8px;
        margin-bottom: 25px;
        color: #28a745;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Etichete
labels = [
    "X / 1 & CA",
    "X / 2 & CA",
    "1 - 1 & CO",
    "12 / 12, GG & GR2",
    "12 / 12, NGG & 1.5G"
]

# Inputuri cote
cote = []
for i, label in enumerate(labels):
    st.markdown(f"**{label}**")
    cota = st.number_input("", min_value=1.01, format="%.2f", step=None, key=f"cota_{i}")
    cote.append(cota)

# Miza totală
st.markdown("**Miza totală (RON)**")
miza_totala = st.number_input("", min_value=1.0, format="%.2f", step=None, key="miza_total")

# Buton
if st.button("✅ Calculează"):
    if all(c > 1.0 for c in cote) and miza_totala > 0:
        inv_suma = sum(1 / c for c in cote)
        castig_comun = miza_totala / inv_suma
        mize_optime = [castig_comun / c for c in cote]
        profituri = [castig_comun - m for m in mize_optime]

        st.markdown("### 📈 Rezultate")
        st.write(f"**Câștig brut comun:** `{round(castig_comun, 2)} RON`")

        # Reafișăm fiecare bloc cu rezultatul LIPIT de inputul său
        for i, label in enumerate(labels):
            st.markdown(f"**{label}**")
            st.number_input("", value=cote[i], format="%.2f", disabled=True, key=f"out_cota_{i}")
            st.markdown(
                f"<div class='rezultat'>Miză optimă: <b>{round(mize_optime[i], 2)} RON</b> | "
                f"Profit net: <b>{round(profituri[i], 2)} RON</b></div>",
                unsafe_allow_html=True
            )

        st.success("Calcule realizate cu succes!")
    else:
        st.error("Completează toate cotele (>1.0) și miza totală (>0).")
