import streamlit as st
import google.generativeai as genai

# ڕێکخستنی لاپەڕە و دیزاینی فول مودرێن (Glassmorphism & Dynamic UI)
st.markdown(
    """
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        color: #f8fafc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* سەرپەڕەی فول مودرێن */
    .header-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        margin-bottom: 30px;
    }

    /* سندوقی وەڵام و ناوەرۆک بە دیزاینی شوشەیی */
    .content-box {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        margin-top: 20px;
    }

    /* دوگمە مودرێنەکان */
    .stButton>button {
        width: 100%;
        border-radius: 16px;
        font-weight: bold;
        height: 55px;
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.6);
        background: linear-gradient(135deg, #60a5fa 0%, #2563eb 100%);
    }

    /* خانەی نووسین */
    .stTextInput textarea, .stTextArea textarea {
        background-color: rgba(30, 41, 59, 0.6) !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# سەرپەڕەی سەرەکی
st.markdown(
    """
    <div class="header-card">
        <div style="font-size: 15px; color: #38bdf8; font-weight: 600;">✨ پلاتفۆرمی زیرەک و قووڵی ژیان</div>
        <h2 style="margin: 8px 0; color: #ffffff;">سلاڤ، نوژدار</h2>
        <div style="font-size: 13px; color: #94a3b8;">وەڵامدانەوەی پرسیارێن فەلسەفی، دەروونی و باوەڕێ ب کوالیتیەکا بلندا مۆدێرن</div>
    </div>
    """,
    unsafe_allow_html=True
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.markdown("### 🌌 ناڤەندا پرسیارێن قووڵ و ژیانێ")
    st.write("پسیارا خو ل ڤێرە بنڤیسە (بۆ نموونە: بۆچی ئەز دژیم؟ خودێ کیە؟ ئەز بۆ چ دخوینم؟)")

    life_question = st.text_area("پرسیار یان بابەتێ خۆ ل ڤێرە بنڤیسە:", placeholder="لێرە بنووسە...")

    if st.button("وەرگرتنی وەڵامی فول مودرێن و ق
                 
