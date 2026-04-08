# app.py
import streamlit as st
from q2_sanitizer import DataSanitizer
from q3_search import find_best

st.set_page_config(page_title="XIPL Assignment Demo", layout="wide")
st.title("XIPL Assignment Demo")

# ---------------- Q2 ----------------
st.header("Q2: Data Sanitizer")

# User Inputs
data = {
    "Height": st.number_input("Height (cm)", value=170),
    "Chest": st.number_input("Chest (cm)", value=90),
    "Waist": st.number_input("Waist (cm)", value=80),
    "Hip": st.number_input("Hip (cm)", value=95)
}

if st.button("Process"):
    ds = DataSanitizer(data.copy())

    norm = ds.normalize()
    issues = ds.validate()
    est = ds.estimate_missing()

    st.markdown("---")

    # ✅ Normalized Data
    st.subheader("Normalized Data")
    for key, value in norm.items():
        st.write(f"**{key}:** {round(value, 2)} cm")

    # ✅ Issues Found
    st.subheader("Issues Found")
    if issues:
        for issue in issues:
            st.error(issue)
    else:
        st.success("No issues detected ✅")

    # ✅ Estimated Values
    st.subheader("Estimated Values")
    estimated_found = False
    for key, value in est.items():
        if key not in data:
            st.info(f"{key}: {round(value, 2)} cm (estimated)")
            estimated_found = True

    if not estimated_found:
        st.write("No additional estimations needed")

# ---------------- Q3 ----------------
st.header("Q3: Best Fit Search")

def confidence_label(score):
    if score > 80:
        return "Excellent Fit"
    elif score > 60:
        return "Good Fit"
    elif score > 40:
        return "Average Fit"
    else:
        return "Poor Fit"

if st.button("Find Fit"):
    # Demo DB with realistic near-perfect matches
    db = [
        {"id": 1, "Chest": 90, "Waist": 80, "Hip": 95},   # perfect match
        {"id": 2, "Chest": 92, "Waist": 82, "Hip": 96},   # very close
        {"id": 3, "Chest": 88, "Waist": 78, "Hip": 94},   # very close
    ] + [{"id": i, "Chest": 100+i%5, "Waist": 80+i%3, "Hip": 90+i%4} for i in range(4, 100)]

    ds = DataSanitizer(data.copy())
    user = ds.normalize()
    result = find_best(user, db)

    st.markdown("---")
    st.subheader("Top 3 Garments")

    for i, item in enumerate(result, start=1):
        st.write(f"### Rank {i}")
        st.write(f"**Garment ID:** {item['id']}")
        st.write(f"**Fit Score:** {item['score']} / 100")
        st.write(f"**Fit Quality:** {confidence_label(item['score'])}")
        st.markdown("---")

    st.info(
        "💡 Note: For very large databases (~1M garments), linear scan is slow. "
        "Use KD-Tree, BallTree, or a Vector Database (Milvus / Pinecone) for fast nearest-neighbor search."
    )