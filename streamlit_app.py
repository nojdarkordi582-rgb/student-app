import streamlit as st
import google.generativeai as genai

# 1. ڕێکخستنا سەرەکی پەڕەی
st.set_page_config(
    page_title="زکر | پەناگەها دەروونی و ڕۆحانی", 
    page_icon="🌿", 
    layout="centered"
)

# 💡 لێرە لە جهێ "LIRE_KILIL_XI_LERE_DANUR" کلیلێ خۆ یێ AI دابنە (لە دناڤ دوو نیشانێن نقلەیدا)
GOOGLE_API_KEY = "LIRE_KILIL_XI_LERE_DANUR"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    model = None

# 2. دیزاینا تایبەت (Dark Glassmorphism)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #091e18 0%, #0f172a 100%);
        color: #ffffff;
    }
    .ai-card {
        background: rgba(15, 23, 42, 0.9);
        border-right: 5px solid #34d399;
        border-top: 1px solid rgba(52, 211, 153, 0.3);
        border-left: 1px solid rgba(52, 211, 153, 0.3);
        border-bottom: 1px solid rgba(52, 211, 153, 0.3);
        padding: 22px;
        border-radius: 18px;
        text-align: right;
        direction: rtl;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .stTextArea textarea {
        background-color: rgba(30, 41, 59, 0.8) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        direction: rtl;
    }
    .counter-display {
        font-size: 45px;
        font-weight: bold;
        color: #34d399;
        text-align: center;
        background: rgba(30, 41, 59, 0.7);
        border: 2px solid #34d399;
        border-radius: 15px;
        padding: 15px;
        margin: 15px 0;
    }
    .developer-footer {
        text-align: center;
        color: #34d399;
        font-size: 15px;
        font-weight: bold;
        margin-top: 40px;
        padding: 15px;
        border-top: 1px dashed rgba(52, 211, 153, 0.3);
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. سەرۆکی پڕۆژەی
st.markdown("<h1 style='text-align: center; color: #34d399;'>🌿 زکر • پەناگەها دەروونی و ڕۆحانی</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 15px;'>ڕێبەرێ هۆشمەندێ ڕۆحانی؛ هەر پرسیارەکا دەروونی یان ئاینی بنڤیسە تاوەکو AI بەرسڤەکا تایبەت و ب ئایەت و دوعا بۆ تە ئامادە بکەت.</p>", unsafe_allow_html=True)
st.markdown("---")

# سیستەمێ تابان (Tabs)
tab1, tab2 = st.tabs(["🌿 ڕێبەرێ هۆشمەندێ AI", "📿 مسبحەیا ئەلیکترۆنی"])

# --- بەشێ یەکەم: زیرەکیا دەستکرد بۆ پرسێن دەروونی و ئاینی ---
with tab1:
    st.markdown("<p style='text-align: right; direction: rtl; color: #34d399; font-weight: bold;'>🧠 پرسیار، کێشە یان هەستێ خۆ لێرە بنڤیسە:</p>", unsafe_allow_html=True)
    user_prompt = st.text_area("", placeholder="بۆ نموونە: ئەز ترسا ژ پاشەڕۆژێ هەم، چ بکەم تا دلێ من ئارام ببێت؟ یان پرسیارەکێ ئاینی بپرسە...", height=120)

    if st.button("✨ ژ زیرەکیا
                 
