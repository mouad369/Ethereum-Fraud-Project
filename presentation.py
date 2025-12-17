import streamlit as st
import pandas as pd
import joblib

# ==========================================
# 1. Page Config & CSS Styling
# ==========================================
st.set_page_config(page_title="Project Presentation - Mouad GHALLAB", page_icon="🎤", layout="wide")

# Theme Colors
PRIMARY_COLOR = "#FF9F1C"  # Orange
BG_COLOR = "#011627"       # Dark Blue
TEXT_COLOR = "#FDFFFC"     # White

# Custom CSS for Professional Design
st.markdown(f"""
    <style>
    /* Main App Background */
    .stApp {{
        background-color: {BG_COLOR};
        color: {TEXT_COLOR};
    }}
    
    /* Headings */
    h1, h2, h3 {{
        color: {PRIMARY_COLOR} !important;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
    }}
    
    /* General Text */
    p, li, div {{
        font-size: 20px !important;
        color: {TEXT_COLOR};
        line-height: 1.6;
    }}
    
    /* Footer Styling (Made with love) */
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: {BG_COLOR};
        color: {PRIMARY_COLOR};
        text-align: center;
        padding: 10px;
        font-size: 14px !important;
        border-top: 1px solid #333;
        z-index: 100;
    }}
    
    /* Navigation Buttons */
    div.stButton > button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        font-size: 20px;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        width: 100%;
        transition: 0.3s;
    }}
    div.stButton > button:hover {{
        background-color: #E08E00;
        color: white;
        transform: scale(1.02);
    }}
    
    /* Centered Containers */
    .centered-content {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify_content: center;
        text-align: center;
        margin-top: 20px;
    }}
    
    /* Big Stats Numbers */
    .big-number {{
        font-size: 70px !important;
        font-weight: bold;
        color: {PRIMARY_COLOR};
    }}
    
    /* Custom Info Boxes */
    .info-box {{
        background-color: #022c4d;
        padding: 20px;
        border-radius: 10px;
        border-left: 8px solid {PRIMARY_COLOR};
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. Navigation Logic (Session State)
# ==========================================
if 'slide' not in st.session_state:
    st.session_state.slide = 0

def next_slide():
    if st.session_state.slide < 7: # Total slides - 1
        st.session_state.slide += 1

def prev_slide():
    if st.session_state.slide > 0:
        st.session_state.slide -= 1

# ==========================================
# 3. Slides Content
# ==========================================

# --- SLIDE 0: Title ---
if st.session_state.slide == 0:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"<h1>🛡️ Ethereum Fraud Detection</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:white !important;'>Using Ensemble Machine Learning</h3>", unsafe_allow_html=True)
    st.markdown("<br><hr style='border-color:#FF9F1C; width: 50%; margin: auto;'><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class='centered-content'>
            <h2>Presented By: <span style='color:{PRIMARY_COLOR}'>Mouad GHALLAB</span></h2>
            <p>Project Class of 2025</p>
        </div>
    """, unsafe_allow_html=True)

# --- SLIDE 1: The Problem ---
elif st.session_state.slide == 1:
    st.markdown("<h1>🤔 The Problem Statement</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        # Using a professional fraud icon
        st.image("https://cdn-icons-png.flaticon.com/512/9322/9322127.png", width=350)
    with col2:
        st.markdown(f"""
        <div style='margin-top: 40px;'>
            <ul style="list-style-type:none;">
                <li style="margin-bottom:20px;">
                    ❌ <b>Crypto Fraud is Escalating:</b> <br>Scams and illicit activities are increasing daily on the blockchain.
                </li>
                <li style="margin-bottom:20px;">
                    ❌ <b>Manual Review is Impossible:</b> <br>With millions of transactions per second, humans cannot keep up.
                </li>
                <li style="margin-bottom:20px;">
                    ❌ <b>The Need for Automation:</b> <br>We require an AI system that monitors 24/7 without fatigue.
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- SLIDE 2: The Data ---
elif st.session_state.slide == 2:
    st.markdown("<h1>📊 Data Overview & Challenges</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='centered-content'><span class='big-number'>9.8k</span><br>Transactions</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='centered-content'><span class='big-number'>50+</span><br>Features</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='centered-content'><span class='big-number' style='color:#ff4b4b !important'>Imbalanced</span><br>Rare Fraud Cases</div>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class='info-box' style='text-align: center;'>
            💡 <b>Technical Solution:</b> Used <code>StratifiedShuffleSplit</code> to ensure the training data is statistically representative.
        </div>
    """, unsafe_allow_html=True)

# --- SLIDE 3: The Pipeline ---
elif st.session_state.slide == 3:
    st.markdown("<h1>⚙️ The Solution Pipeline</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='info-box'>
        <h3>1. Data Cleaning 🧹</h3>
        <p>Removing noise (IDs, Addresses) & handling missing values intelligently using <b>KNN Imputer</b>.</p>
    </div>
    
    <div class='info-box'>
        <h3>2. Robust Scaling ⚖️</h3>
        <p>Using <b>RobustScaler</b> to manage outliers (Whales) which are common in financial datasets.</p>
    </div>
    
    <div class='info-box'>
        <h3>3. Feature Selection 🎯</h3>
        <p>Selecting the Top 20 most impactful features using <b>SelectKBest</b> to improve model speed.</p>
    </div>
    """, unsafe_allow_html=True)

# --- SLIDE 4: The Model ---
elif st.session_state.slide == 4:
    st.markdown("<h1>🧠 The Model Architecture</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white !important;'>Ensemble Learning Approach</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style='text-align:center; padding: 20px; background: #022c4d; border-radius: 15px;'>
            <h3 style='color:{PRIMARY_COLOR}'>Random Forest</h3>
            <p>Ensures Stability & Reduces Overfitting</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style='text-align:center; padding: 20px; background: #022c4d; border-radius: 15px;'>
            <h3 style='color:{PRIMARY_COLOR}'>Gradient Boosting</h3>
            <p>Focuses on Hard-to-Predict Cases</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='centered-content'><h1>= <span style='color:{PRIMARY_COLOR}'>Voting Classifier</span></h1><p>Combining both for maximum accuracy</p></div>", unsafe_allow_html=True)

# --- SLIDE 5: Results ---
elif st.session_state.slide == 5:
    st.markdown("<h1>🏆 Performance Results</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='centered-content'><span class='big-number'>99%</span><br><h2>ROC-AUC Score</h2></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <br>
    <div style='display:flex; justify-content:center; gap: 50px;'>
        <div style='text-align:center;'>✅ <b>High Precision</b><br>(Minimizing False Alarms)</div>
        <div style='text-align:center;'>✅ <b>Real-Time Speed</b><br>(Fast Execution)</div>
    </div>
    """, unsafe_allow_html=True)

# --- SLIDE 6: LIVE DEMO ---
elif st.session_state.slide == 6:
    st.markdown("<h1>🚀 Live Demonstration</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Interact with the model directly below:</p>", unsafe_allow_html=True)
    
    # Load resources for demo
    try:
        model = joblib.load('ethereum_fraud_detector.pkl')
        
        # Mini Interface
        with st.container():
            st.markdown(f"<div style='background-color: #022c4d; padding: 20px; border-radius: 10px; border: 1px solid {PRIMARY_COLOR};'>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                val_sent = st.number_input("Total Ether Sent", value=15.0)
                time_diff = st.number_input("Time Diff (Mins)", value=1000.0)
            with col2:
                sent_tnx = st.number_input("Sent Tnx Count", value=10)
                received_tnx = st.number_input("Received Tnx Count", value=5)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🔍 Analyze Transaction"):
                # Simulation Logic
                # Load header structure from CSV
                df_temp = pd.read_csv('transaction_dataset.csv', nrows=1)
                df_temp.columns = df_temp.columns.str.strip()
                cols_drop = ['Unnamed: 0', 'Index', 'Address', 'FLAG']
                df_temp = df_temp.drop(columns=[c for c in cols_drop if c in df_temp.columns], errors='ignore')
                
                # Create input row
                input_data = pd.DataFrame(0, index=[0], columns=df_temp.columns)
                input_data['total Ether sent'] = val_sent
                input_data['Time Diff between first and last (Mins)'] = time_diff
                input_data['Sent tnx'] = sent_tnx
                input_data['Received Tnx'] = received_tnx
                
                # Predict
                prediction = model.predict(input_data)[0]
                prob = model.predict_proba(input_data)[0][1]
                
                st.divider()
                if prediction == 1:
                    st.markdown(f"<h2 style='color:#ff4b4b'>🚨 FRAUD DETECTED</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align:center'>Probability: <b>{prob*100:.2f}%</b></p>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<h2 style='color:#00e676'>✅ SAFE TRANSACTION</h2>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align:center'>Safety Score: <b>{(1-prob)*100:.2f}%</b></p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Demo Error: Could not load model files. Details: {e}")

# --- SLIDE 7: Conclusion ---
elif st.session_state.slide == 7:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1>🎬 Conclusion</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='centered-content'>
        <div class='info-box' style='width: 80%;'>
            <p>✅ We successfully built a robust <b>AI Fraud Detector</b>.</p>
            <p>🚀 Next Step: <b>Deploy API on Cloud</b> for real-time wallet integration.</p>
        </div>
        <br><br>
        <h1 style='font-size: 60px !important;'>Thank You! ❤️</h1>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. Footer & Navigation Controls
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)

col_prev, col_num, col_next = st.columns([1, 2, 1])

with col_prev:
    if st.session_state.slide > 0:
        if st.button("⬅️ Previous"):
            prev_slide()
            st.rerun()

with col_num:
    st.markdown(f"<div style='text-align:center; color:#8d99ae; margin-top:10px; font-size:16px;'>Slide {st.session_state.slide + 1} / 8</div>", unsafe_allow_html=True)

with col_next:
    if st.session_state.slide < 7:
        if st.button("Next ➡️"):
            next_slide()
            st.rerun()

# Fixed Footer
st.markdown(f"""
    <div class='footer'>
        Made with love ❤️ by <b>Mouad GHALLAB</b> | 2025
    </div>
""", unsafe_allow_html=True)