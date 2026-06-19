import streamlit as st
import pandas as pd

st.set_page_config(page_title="BioGenX Pro", layout="wide")

st.title("🧬 BioGenX Pro: Genome & Disease Intelligence System")

dna = st.text_area("Enter DNA Sequence")

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


def disease_ai_explanation(name, gc, dna):
    if name == "Cancer Risk":
        return (
            "This pattern shows elevated GC content with oncogene-like sequence presence. "
            "High GC regions are often associated with unstable replication zones, which may increase mutation probability in dividing cells."
        )

    elif name == "Mutation Risk":
        return (
            "The genome shows increased GC imbalance. This can lead to replication stress and higher mutation frequency during DNA copying processes."
        )

    elif name == "Genetic Disorder":
        return (
            "Specific repeat-like DNA patterns detected. Such patterns are often linked with structural instability in genetic coding regions."
        )

    elif name == "Stop Codon Instability":
        return (
            "Presence of stop codon-like patterns suggests premature termination signals, which may disrupt protein synthesis."
        )

    elif name == "Codon Stable Genome":
        return (
            "No abnormal stop codon disruptions detected. Codon structure appears stable for standard protein translation."
        )

    else:
        return "Genome appears stable with no significant abnormal biological markers detected."


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

        chart_data = pd.DataFrame({
            "Bases": ["A", "T", "G", "C"],
            "Count": [a, t, g, c]
        })

        st.bar_chart(chart_data.set_index("Bases"))

        st.subheader("🔁 Sequence Analysis")

        comp = complement(dna)
        rev_comp = comp[::-1]

        st.code("Complement: " + comp)
        st.code("Reverse Complement: " + rev_comp)

        codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
        st.write("Codons:", "-".join(codons))

        # ---------------- DISEASE ENGINE (3 MODELS) ---------------- #

        st.subheader("🧠 Algorithm Result (Multi-Model Analysis)")

        results = []

        # Model 1: GC Risk Model
        if gc > 60:
            results.append(("Mutation Risk", "High GC content detected leading to replication instability."))
        else:
            results.append(("Normal Genome", "GC content within stable biological range."))

        # Model 2: Cancer Pattern Model
        if "ATG" in dna and gc > 55:
            results.append(("Cancer Risk", "Oncogene-like start codon pattern with high GC imbalance detected."))
        else:
            results.append(("Stable Genome", "No oncogenic pattern detected in sequence."))

        # Model 3: Codon Stability Model
        unstable = ["TAA", "TAG", "TGA"]
        if any(i in dna for i in unstable):
            results.append(("Stop Codon Instability", "Premature termination codons found affecting protein synthesis."))
        else:
            results.append(("Codon Stable Genome", "No disruptive stop codon patterns found."))

        # DISPLAY RESULTS
        for i, (name, explanation) in enumerate(results, start=1):
            st.markdown(f"### 🔬 Model {i}: {name}")
            st.success(name)
            st.write("🧠 AI Explanation:")
            st.info(explanation)
            st.divider()
