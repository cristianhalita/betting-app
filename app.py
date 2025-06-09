import streamlit as st
import numpy as np

st.set_page_config(page_title="Calculator Profit Pariuri", layout="centered")
st.title("📊 Calculator Profit cu Mize Optime")

st.markdown("Introdu cele 5 variante de pariu și o miză totală. Apasă 'Calculează' pentru a vedea mizele optime și profitul net egalizat.")

# Etichete personalizate
labels = [
    "X / 1  & CA",
    "X / 2 & CA",
    "1 - 1 & CO",
    "12 / 12, GG & GR2",
    "12 / 12, NGG & 1.5G"
]

# Inputuri afișate vertical
cote = []
for i in range(len(labels)):
    st.markdown(f"<b>{labels[i]}</b>", unsafe_allow_html=True)
    cota = st.text_input("", placeholder="Introdu cota", key=f"cota_{i}")
    try:
        cota = float(cota)
    except:
        cota = 0.0
    cote.append(cota)

miza_totala = st.number_input("Miza totală (RON)", min_value=1.0, step=0.5, format="%.2f")

# Buton pentru calcul aliniat la dreapta și stilizat
st.markdown("""
    <div style='display: flex; justify-content: flex-end;'>
        <form action="#" method="post">
            <button style='background-color: #28a745; color: white; padding: 0.5em 1em; border: none; border-radius: 5px;'>Calculează</button>
        </form>
    </div>
""", unsafe_allow_html=True)

if st.session_state.get("Calculează") or st.button("Calculează"):
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
