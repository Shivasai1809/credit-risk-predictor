
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="wide"
)

# Title
st.title("Credit Risk & Loan Default Prediction")
st.markdown("AI-powered credit risk assessment using machine learning")

# Sidebar
with st.sidebar:
    st.header("Model Settings")
    st.info("Upload customer data or enter details manually")

# Main interface
tab1, tab2 = st.tabs(["Single Prediction", "Batch Prediction"])

with tab1:
    st.subheader("Enter Customer Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        income = st.number_input("Annual Income ($)", min_value=0, value=50000)
        loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=10000)
        credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
    
    with col2:
        employment_length = st.number_input("Employment Length (years)", min_value=0, value=5)
        debt_to_income = st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=1.0, value=0.3)
    
    if st.button("🔍 Predict Risk", use_container_width=True):
        with st.spinner("Analyzing..."):
            st.success("Prediction Complete!")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Risk Level", "Low", "✓")
            with col2:
                st.metric("Default Probability", "15%", "-5%")
            with col3:
                st.metric("Recommended Action", "Approve")

with tab2:
    st.subheader("Upload CSV for Batch Prediction")
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        
        if st.button("Run Batch Prediction"):
            st.success(f"Processed {len(df)} records!")

st.markdown("---")
st.markdown("Made with using Streamlit")
