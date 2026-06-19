import streamlit as st
import pandas as pd

st.set_page_config(page_title="BioGenX Pro", layout="wide")

st.title("🧬 BioGenX Pro: Genome & Disease Visualization System")

dna = st.text_area("Enter DNA Sequence")

# ---------------- ALGORITHM SELECTION ---------------- #

algorithm = st.selectbox(
    "Select Analysis Algorithm",
    [
        "Basic GC Analysis",
        "Mutation Risk Model",
        "Codon Stability Check"
    ]
)

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


if st.button("ANALYZE GENOME"):

    dna = dna.upper()
    length = len(dna)

    if length == 0:
        st.error("Enter valid DNA sequence")

    else:

        # ---------------- BASE COUNT ---------------- #

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
        st.code("Complement: " + comp)
        st.code("Reverse Complement: " + comp[::-1])

        codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
        st.write("Codons:", "-".join(codons))

        # ---------------- ALGORITHM ENGINE ---------------- #

        st.subheader("🧠 Algorithm Result")

        disease = ""
        image_url = ""

        if algorithm == "Basic GC Analysis":

            if gc > 60:
                disease = "Mutation Risk"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/8/8f/DNA_damage.jpg"
            else:
                disease = "Normal Genome"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/1/1f/Healthy_cells.jpg"


        elif algorithm == "Mutation Risk Model":

            if "ATG" in dna and gc > 55:
                disease = "Cancer Risk"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/6/6b/Cancer_cells.jpg"
            elif gc > 50:
                disease = "High Mutation Probability"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/8/8f/DNA_damage.jpg"
            else:
                disease = "Stable Genome"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/1/1f/Healthy_cells.jpg"


        elif algorithm == "Codon Stability Check":

            unstable_patterns = ["TAA", "TAG", "TGA"]

            if any(codon in dna for codon in unstable_patterns):
                disease = "Stop Codon Instability"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/DNA_helix_structure.jpg"
            else:
                disease = "Codon Stable Genome"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/1/1f/Healthy_cells.jpg"

        st.success("Result: " + disease)

        st.subheader("🧬 Visualization")
        st.image(image_url, use_container_width=True)
