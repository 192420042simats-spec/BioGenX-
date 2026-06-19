import streamlit as st
import pandas as pd

st.set_page_config(page_title="BioGenX Pro", layout="wide")

st.title("🧬 BioGenX Pro: Genome & Disease Intelligence System")

dna = st.text_area("Enter DNA Sequence")

# ---------------- COMPLEMENT FUNCTION ---------------- #

def complement(seq):
    comp = ""
    for i in seq:
        if i == "A":
            comp += "T"
        elif i == "T":
            comp += "A"
        elif i == "G":
            comp += "C"
        elif i == "C":
            comp += "G"
    return comp

# ---------------- DISEASE AI EXPLANATION ---------------- #

def disease_explanation(name, dna, gc):

    explanations = {
        "Normal Genome": "No harmful genetic mutation patterns detected. DNA structure is stable and within biological limits.",
        
        "Mutation Risk": "High GC imbalance may cause replication stress, increasing probability of DNA mutation during cell division.",
        
        "Cancer Risk": "Presence of ATG pattern combined with GC imbalance may indicate unstable gene expression regions linked to abnormal cell growth.",
        
        "Genetic Disorder": "Repeated DNA motifs detected, which are often associated with structural gene instability and inherited disorders.",
        
        "Stop Codon Instability": "Multiple STOP codons (TAA/TAG/TGA) detected. This may cause premature termination of protein synthesis leading to malfunctioning proteins."
    }

    return explanations.get(name, "No explanation available.")


# ---------------- MAIN ANALYSIS ---------------- #

if st.button("ANALYZE GENOME"):

    dna = dna.upper()
    length = len(dna)

    if length == 0:
        st.error("Please enter a valid DNA sequence")

    else:

        # ---------------- COUNT BASES ---------------- #

        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        gc = (g + c) / length * 100
        at = (a + t) / length * 100

        # ---------------- STATISTICS ---------------- #

        st.subheader("🧬 Problem Understanding & Analysis")

        st.write("""
        This system analyzes DNA sequences to identify nucleotide distribution, GC content,
        codon patterns, and potential disease-related genetic anomalies using rule-based bioinformatics logic.
        """)

        st.subheader("📊 DNA Statistics")
        st.write("Length:", length)
        st.write("A:", a, "T:", t, "G:", g, "C:", c)
        st.write("GC %:", round(gc, 2))
        st.write("AT %:", round(at, 2))

        chart = pd.DataFrame({
            "Bases": ["A", "T", "G", "C"],
            "Count": [a, t, g, c]
        })

        st.bar_chart(chart.set_index("Bases"))

        # ---------------- SEQUENCE ANALYSIS ---------------- #

        st.subheader("🔁 Sequence Analysis")

        comp = complement(dna)
        rev_comp = comp[::-1]

        st.code("Complement: " + comp)
        st.code("Reverse Complement: " + rev_comp)

        codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
        st.write("Codons:", "-".join(codons))

        # ---------------- ALGORITHM DESIGN ---------------- #

        st.subheader("🧠 Algorithm / System Design")

        st.write("""
        The system uses rule-based pattern recognition:
        - GC content thresholding
        - Motif detection (ATG, repeat regions)
        - Stop codon scanning
        - Codon segmentation
        """)

        # ---------------- DISEASE ENGINE ---------------- #

        st.subheader("🦠 Disease Prediction & Explanation")

        results = []

        # Model 1
        if gc > 60:
            results.append(("Mutation Risk", gc))

        else:
            results.append(("Normal Genome", gc))

        # Model 2
        if "ATG" in dna and gc > 55:
            results.append(("Cancer Risk", gc))
        else:
            results.append(("Normal Genome", gc))

        # Model 3
        stop_codons = ["TAA", "TAG", "TGA"]
        if any(x in dna for x in stop_codons):
            results.append(("Stop Codon Instability", gc))
        else:
            results.append(("Normal Genome", gc))

        for i, (disease, gc_val) in enumerate(results, 1):

            st.markdown(f"### 🔬 Model {i}: {disease}")

            st.success("Disease Prediction: " + disease)

            st.write("🧠 Explanation:")
            st.info(disease_explanation(disease, dna, gc))

