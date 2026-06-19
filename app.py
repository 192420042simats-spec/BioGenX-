import streamlit as st
import pandas as pd

st.set_page_config(page_title="BioGenX Pro", layout="wide")

st.title("🧬 BioGenX Pro: Genome & Disease Intelligence System")

dna = st.text_area("Enter DNA Sequence")

def complement(seq):
    comp = ""
    for i in seq:
        if i == "A": comp += "T"
        elif i == "T": comp += "A"
        elif i == "G": comp += "C"
        elif i == "C": comp += "G"
    return comp

if st.button("ANALYZE GENOME"):

    dna = dna.upper()
    length = len(dna)

    if length == 0:
        st.error("Enter valid DNA sequence")

    else:

        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        gc = (g + c) / length * 100
        at = (a + t) / length * 100

        st.subheader("🧬 DNA STATISTICS")
        st.write("Length:", length)
        st.write("A:", a, "T:", t, "G:", g, "C:", c)
        st.write("GC %:", round(gc, 2))
        st.write("AT %:", round(at, 2))

        # Chart
        chart_data = pd.DataFrame({
            "Bases": ["A", "T", "G", "C"],
            "Count": [a, t, g, c]
        })

        st.bar_chart(chart_data.set_index("Bases"))

        st.subheader("🔁 Sequence Analysis")

        comp = complement(dna)
        rev = dna[::-1]

        st.code("Complement: " + comp)
        st.code("Reverse Complement: " + comp[::-1])

        st.subheader("🧬 Codon Breakdown")

        codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
        st.write("-".join(codons))

        # ---------------- DISEASE ENGINE ---------------- #

        st.subheader("🦠 Disease Prediction Engine")

        risk = "Low"
        disease = "Healthy Genome"
        images = []

        if "ATG" in dna and gc > 55:
            risk = "HIGH"
            disease = "⚠ Cancer Risk"
            images.append("https://upload.wikimedia.org/wikipedia/commons/6/6b/Cancer_cells.jpg")

        elif gc > 60:
            risk = "MEDIUM"
            disease = "⚠ Mutation Risk"
            images.append("https://upload.wikimedia.org/wikipedia/commons/8/8f/DNA_damage.jpg")

        elif "TTAGG" in dna:
            risk = "MEDIUM"
            disease = "⚠ Genetic Disorder"
            images.append("https://upload.wikimedia.org/wikipedia/commons/3/3f/DNA_helix_structure.jpg")

        else:
            risk = "LOW"
            disease = "✅ Normal Genome"
            images.append("https://upload.wikimedia.org/wikipedia/commons/1/1f/Healthy_cells.jpg")

        st.success("Disease: " + disease)
        st.info("Risk Level: " + risk)

        st.subheader("🧾 Bio Report Score")

        score = 100 - (gc * 0.5)

        if risk == "HIGH":
            score -= 40
        elif risk == "MEDIUM":
            score -= 20

        st.metric("Bio-Health Score", round(score, 2))

        st.subheader("🧬 Disease Visualization")

        for img in images:
            st.image(img, use_container_width=True)
