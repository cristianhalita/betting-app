
import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculator Profit Pariuri", layout="centered")
st.title("📊 Calculator Profit cu Mize Optime")

st.markdown("Introdu 5 cote și o miză totală. Apasă 'Calculează' pentru a vedea mizele optime și profitul net egalizat.")

# Inputuri
cols = st.columns(5)
cote = []
for i, col in enumerate(cols):
    cota = col.number_input(f"Cota {i+1}", min_value=1.01, step=0.01, format="%.2f", key=f"cota_{i}")
    cote.append(cota)

miza_totala = st.number_input("Miza totală (RON)", min_value=1.0, step=0.5, format="%.2f")

# Buton pentru calcul
if st.button("Calculează"):
    if all(c > 1.0 for c in cote) and miza_totala > 0:
        inv_sume = sum(1 / c for c in cote)
        castig_comun = miza_totala / inv_sume
        mize_optime = [castig_comun / c for c in cote]
        profituri = [castig_comun - m for m in mize_optime]

        st.subheader("📈 Rezultate")
        st.write("Câștig brut comun:", round(castig_comun, 2), "RON")

        table_data = {
            "Cota": cote,
            "Miză optimă (RON)": [round(m, 2) for m in mize_optime],
            "Profit net (RON)": [round(p, 2) for p in profituri]
        }

        st.table(table_data)
        st.success("Calcule realizate cu succes!")
    else:
        st.error("Te rog completează toate cotele (>1.0) și miza totală (>0).")
