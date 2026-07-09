import streamlit as st
from report_generator import generate_report



st.set_page_config(
    page_title="AI Executive Decision Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("AI Executive Decision Intelligence")


industry = st.selectbox(
    "Select Industry",
    [
        "Telecom"
        # "Banking",
        # "Healthcare",
        # "Retail"
    ]
)

telecom_area = st.selectbox(
    "Business Area",
    [
        "BSS",
        "OSS",
        "5G",
        "Revenue Assurance",
        "Customer Churn",
        "NOC Operations"
    ]
)


# timeline = st.selectbox(
#     "Timeline",
#     ["30 Days","90 Days","6 Months","12 Months"]
# )


problem = st.text_area(
    "Business Problem / Question",
    height=150
)

objective = st.text_input(
    "Business Objective"
)


if st.button("Generate Report"):

    restricted_words = ["terrorism", "bomb", "hack", "source code", "virus"]

    if any(word in problem.lower() for word in restricted_words):
        st.error("Input not allowed.")
        st.stop()

    with st.spinner("Analyzing business case..."):
        report = generate_report(
            industry,
            telecom_area,
            problem,
            objective
        )

    st.markdown(report)