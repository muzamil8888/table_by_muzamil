import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Table Generator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling with updated stepper button and equals sign colors
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(90deg, #BB86FC, #03DAC6);
        color: #000000;
    }
    .header-container {
        background: linear-gradient(90deg, #BB86FC, #03DAC6);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
    }
    .main-header {
        font-family: 'Arial', sans-serif;
        color: #000000;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    .sub-header {
        font-family: 'Arial', sans-serif;
        color: #000000;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        font-size: 1.8rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    .multiplication-item {
        background-color: rgba(30, 30, 30, 0.8);
        padding: 14px 20px;
        border-radius: 8px;
        margin-bottom: 12px;
        font-size: 20px;
        font-family: 'Arial', sans-serif;
        border-left: 5px solid #BB86FC;
        color: #000000;
        box-shadow: 0 2px 5px rgba(0,0,0,0.4);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .calculation {
        display: inline-block;
        width: 33%;
        text-align: right;
        font-size: 26px;
        font-weight: bold;
        color: #03DAC6;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .equals {
        display: inline-block;
        width: 33%;
        text-align: center;
        font-size: 24px;
        color: #BB86FC;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    .result {
        display: inline-block;
        width: 33%;
        text-align: left;
        font-size: 26px;
        font-weight: bold;
        color: #03DAC6;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .stNumberInput label {
        font-size: 1.5rem;
        font-weight: bold;
        color: #000000;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .stNumberInput div[data-baseweb="input"] input {
        background-color: rgba(40, 40, 40, 0.8);
        color: #03DAC6;
        border-color: #000000;
        font-size: 1.8rem;
        height: 80px;
        border-radius: 8px;
        width: 100%;
    }
    /* Style for + and - buttons */
    div[data-testid="stNumberInput-Stepper"] button {
        background-color: rgba(40, 40, 40, 0.8);
        border-color: #000000;
        color: #03DAC6;
        border-radius: 4px;
        padding: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    div[data-testid="stNumberInput-Stepper"] button:hover {
        background-color: rgba(60, 60, 60, 0.8);
        color: #03DAC6;
    }
    div[data-testid="stNumberInput-Stepper"] button svg {
        fill: #03DAC6;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #BB86FC;
        color: #000000;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    .app-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 15px;
    }
    @media (max-width: 600px) {
        .multiplication-item {
            font-size: 16px;
            padding: 10px;
        }
        .calculation, .equals, .result {
            font-size: 20px;
        }
        .stNumberInput div[data-baseweb="input"] input {
            font-size: 1.5rem;
            height: 60px;
        }
        div[data-testid="stNumberInput-Stepper"] button {
            font-size: 1.2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# App container
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# Custom header
st.markdown("""
<div class="header-container">
    <h1 class="main-header">Table Generator</h1>
</div>
""", unsafe_allow_html=True)

# Number input
number = st.number_input("Enter a number:", min_value=1, max_value=1000, value=5, step=1, key="number_input")

# Table range input
table_range = st.number_input("Table range (1 to 100):", min_value=1, max_value=100, value=20, step=1, key="range_input")

# Display table header
st.markdown(f'<h2 class="sub-header">Multiplication Table for {number}</h2>', unsafe_allow_html=True)

# Generate and display the multiplication table
table_html = '<div>'
for i in range(1, int(table_range) + 1):
    result = i * number
    table_html += f"""
        <div class="multiplication-item">
            <span class="calculation">{i} × {number}</span>
            <span class="equals">=</span>
            <span class="result">{result}</span>
        </div>"""
table_html += '</div>'
st.markdown(table_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close app container

# Footer
st.markdown("""
<div class="footer">
    Created by MUZAMIL MEO
</div>
""", unsafe_allow_html=True)