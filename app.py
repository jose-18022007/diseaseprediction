import streamlit as st

st.title("🔍 Bayes' Theorem: Medical Test Interpreter")
st.markdown("""
This app calculates the probability that you actually have a disease **given a positive test result**, 
using **Bayes' Theorem**. Adjust the inputs below to see how results change!
""")

# Sidebar for inputs
st.sidebar.header("🧪 Test & Population Parameters")
prevalence = st.sidebar.slider("Disease Prevalence (P(D))", 0.0, 1.0, 0.01, 0.01, format="%.2f")
sensitivity = st.sidebar.slider("Test Sensitivity (P(+|D))", 0.0, 1.0, 0.95, 0.01, format="%.2f")
specificity = st.sidebar.slider("Test Specificity (P(-|¬D))", 0.0, 1.0, 0.90, 0.01, format="%.2f")

# Calculate false positive rate
false_positive_rate = 1 - specificity

# Apply Bayes' Theorem
numerator = sensitivity * prevalence
denominator = numerator + (false_positive_rate * (1 - prevalence))

if denominator == 0:
    posterior = 0.0
else:
    posterior = numerator / denominator

# Display results
st.subheader("📊 Results")
col1, col2, col3 = st.columns(3)
col1.metric("Prevalence", f"{prevalence:.1%}")
col2.metric("Sensitivity", f"{sensitivity:.1%}")
col3.metric("Specificity", f"{specificity:.1%}")

st.success(f"**Probability you have the disease given a positive test: {posterior:.2%}**")

# Explanation
st.subheader("🧠 How It Works")
st.markdown(f""")
Bayes' Theorem updates our belief after seeing new evidence (a positive test):
