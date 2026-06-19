import streamlit as st

st.title("🧬 BioGenX: Genome Analysis + Disease Prediction")

dna = st.text_input("Enter DNA Sequence")

if st.button("Analyze"):

    dna = dna.upper()

    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    length = len(dna)

    if length == 0:
        st.error("Please enter DNA sequence")

    else:
        gc = ((g + c) / length) * 100

        st.subheader("📊 DNA Statistics")
        st.write("Length:", length)
        st.write("A:", a)
        st.write("T:", t)
        st.write("G:", g)
        st.write("C:", c)
        st.write("GC Content:", round(gc, 2), "%")

        st.subheader("🧬 Reverse Complement")

        complement = ""
        for i in dna:
            if i == "A":
                complement += "T"
            elif i == "T":
                complement += "A"
            elif i == "G":
                complement += "C"
            elif i == "C":
                complement += "G"

        st.write("Complement:", complement)
        st.write("Reverse Complement:", complement[::-1])

        # ---------------- DISEASE PREDICTION ---------------- #

        st.subheader("🦠 Disease Prediction Result")

        disease = "Normal"
        image_url = ""

        if "ATG" in dna or "ATGCG" in dna:
            disease = "⚠ Cancer Risk"
            image_url = "https://upload.wikimedia.org/wikipedia/commons/6/6b/Cancer_cells.jpg"

        elif "TTAGG" in dna:
            disease = "⚠ Genetic Disorder"
            image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/DNA_helix_structure.jpg"

        elif gc > 60:
            disease = "⚠ Mutation Risk"
            image_url = "https://upload.wikimedia.org/wikipedia/commons/8/8f/DNA_damage.jpg"

        else:
            disease = "✅ Normal"
            image_url = "https://upload.wikimedia.org/wikipedia/commons/1/1f/Healthy_cells.jpg"

        st.success(disease)

        if image_url:
            st.image(image_url, caption="Disease Reference Image")
