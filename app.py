import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="ChurnGuard AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

model = joblib.load("churn_model.pkl")

st.markdown("""
<style>
.block-container {
    max-width: 1400px;
    padding-top: 2rem;
}

.hero {
    padding: 30px;
    border-radius: 16px;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 40px;
    margin-bottom: 8px;
}

.hero p {
    color: #cbd5e1;
    font-size: 17px;
}

.metric-card {
    padding: 22px;
    border-radius: 14px;
    background-color: #1e293b;
    border: 1px solid #334155;
    text-align: center;
}

.metric-title {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 8px;
}

.metric-value {
    color: white;
    font-size: 28px;
    font-weight: bold;
}

.section-title {
    font-size: 25px;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 15px;
}

.info-card {
    padding: 16px;
    border-radius: 10px;
    background-color: #1e293b;
    border-left: 4px solid #3b82f6;
    margin-bottom: 10px;
}

.risk-card {
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}

[data-testid="stSidebar"] {
    min-width: 300px;
    max-width: 300px;
}
</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown("""
<div class="hero">
    <h1>📊 ChurnGuard AI</h1>
    <p>AI-Powered Customer Churn Prediction & Retention Analytics</p>
</div>
""", unsafe_allow_html=True)


# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("👤 Customer Profile")
st.sidebar.caption("Enter customer information")

st.sidebar.markdown("---")

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

senior_citizen = st.sidebar.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.sidebar.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.sidebar.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=12
)

phone_service = st.sidebar.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.sidebar.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.sidebar.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.sidebar.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.sidebar.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.sidebar.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.sidebar.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.sidebar.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)


# ==============================
# CREATE CUSTOMER DATA
# ==============================

customer = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})


# ==============================
# MAIN SECTION
# ==============================

st.markdown(
    '<div class="section-title">🔍 Customer Risk Analysis</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter customer details from the sidebar and analyze the customer's "
    "probability of churn."
)

predict = st.button(
    "🚀 Analyze Customer",
    type="primary",
    use_container_width=True
)


# ==============================
# PREDICTION
# ==============================

if predict:

    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0][1]

    probability_percent = probability * 100


    # ==========================
    # RISK LEVEL
    # ==========================

    if probability_percent < 40:
        risk = "Low Risk"
    elif probability_percent < 70:
        risk = "Medium Risk"
    else:
        risk = "High Risk"


    # ==========================
    # PREDICTION RESULT
    # ==========================

    if prediction == 1:
        prediction_text = "Likely to Churn"
    else:
        prediction_text = "Unlikely to Churn"


    # ==========================
    # TOP METRICS
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Churn Probability</div>
                <div class="metric-value">
                    {probability_percent:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Risk Level</div>
                <div class="metric-value">
                    {risk}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">Prediction</div>
                <div class="metric-value">
                    {prediction_text}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("---")


    # ==========================
    # PROBABILITY
    # ==========================

    st.markdown(
        '<div class="section-title">📈 Churn Probability</div>',
        unsafe_allow_html=True
    )

    st.progress(float(probability))

    st.write(
        f"The model estimates a **{probability_percent:.2f}% probability** "
        f"that this customer will churn."
    )


    # ==========================
    # RESULT MESSAGE
    # ==========================

    if prediction == 1:

        st.error(
            "⚠️ Attention required: This customer is predicted to churn."
        )

    else:

        st.success(
            "✅ This customer is currently predicted to remain with the company."
        )


    # ==========================
    # CUSTOMER SUMMARY
    # ==========================

    st.markdown(
        '<div class="section-title">👤 Customer Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Tenure",
            f"{tenure} months"
        )

    with col2:
        st.metric(
            "Monthly Charges",
            f"${monthly_charges:.2f}"
        )

    with col3:
        st.metric(
            "Contract",
            contract
        )

    with col4:
        st.metric(
            "Internet",
            internet_service
        )


    # ==========================
    # RISK FACTORS
    # ==========================

    st.markdown(
        '<div class="section-title">⚠️ Potential Risk Factors</div>',
        unsafe_allow_html=True
    )

    factors = []


    if contract == "Month-to-month":
        factors.append(
            "Customer has a month-to-month contract."
        )

    if tenure < 12:
        factors.append(
            "Customer has a relatively short tenure."
        )

    if monthly_charges > 70:
        factors.append(
            "Monthly charges are relatively high."
        )

    if payment_method == "Electronic check":
        factors.append(
            "Customer uses electronic check payment."
        )

    if tech_support == "No":
        factors.append(
            "Customer does not have technical support."
        )

    if online_security == "No":
        factors.append(
            "Customer does not have online security."
        )

    if internet_service == "Fiber optic":
        factors.append(
            "Customer uses fiber optic internet service."
        )


    if len(factors) == 0:

        factors.append(
            "No major rule-based risk factors identified."
        )


    for factor in factors:

        st.markdown(
            f"""
            <div class="info-card">
                ⚠️ {factor}
            </div>
            """,
            unsafe_allow_html=True
        )


    # ==========================
    # RETENTION RECOMMENDATIONS
    # ==========================

    st.markdown(
        '<div class="section-title">💡 Recommended Retention Actions</div>',
        unsafe_allow_html=True
    )

    recommendations = []


    if contract == "Month-to-month":

        recommendations.append(
            "Offer an attractive annual or two-year contract."
        )


    if monthly_charges > 70:

        recommendations.append(
            "Consider offering a personalized pricing plan or discount."
        )


    if tenure < 12:

        recommendations.append(
            "Provide a new-customer loyalty offer."
        )


    if tech_support == "No":

        recommendations.append(
            "Offer technical support as an additional service."
        )


    if online_security == "No":

        recommendations.append(
            "Consider offering an online security package."
        )


    if payment_method == "Electronic check":

        recommendations.append(
            "Encourage automatic payment methods."
        )


    if len(recommendations) == 0:

        recommendations.append(
            "Continue monitoring the customer and maintain engagement."
        )


    for recommendation in recommendations:

        st.markdown(
            f"""
            <div class="info-card">
                💡 {recommendation}
            </div>
            """,
            unsafe_allow_html=True
        )


    # ==========================
    # CUSTOMER DATA
    # ==========================

    with st.expander("📋 View Customer Input Data"):

        st.dataframe(
            customer,
            use_container_width=True,
            hide_index=True
        )


else:

    st.info(
        "👈 Enter customer information from the sidebar and click "
        "**Analyze Customer** to generate a prediction."
    )


# ==============================
# FOOTER
# ==============================

st.markdown("---")

st.caption(
    "ChurnGuard AI | Machine Learning Customer Retention System"
)