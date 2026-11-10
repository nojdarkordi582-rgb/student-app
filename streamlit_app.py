import streamlit as st
import google.generativeai as genai

# 1. ڕێکخستنا سەرەکی پەڕەی
st.set_page_config(
    page_title="زکر | پەناگەها دەروونی و ڕۆحانی", 
    page_icon="🌿", 
    layout="centered"
)

# 💡 لێرە لە جهێ "LIRE_KILIL_XI_LERE_DANUR" کلیلێ خۆ یێ AI دابنە
GOOGLE_API_KEY = "AQ.Ab8RN6Lmm0CPbiKl3JWu4jnUS0jMTQ0_5NBNjBYKfFptf2VaKQ

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    model = None

# 2. دیزاینا تایبەت و گڵۆپێ کەسک (Glowing Animation)
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
    
    /* گڵۆپێ کەسک یێ بوەست و دڤەمرێت (Glow Animation) */
    @keyframes glowing {
        0% { color: #059669; text-shadow: 0 0 2px rgba(52, 211, 153, 0.2); }
        50% { color: #34d399; text-shadow: 0 0 15px rgba(52, 211, 153, 0.9), 0 0 25px rgba(16, 185, 129, 0.6); }
        100% { color: #059669; text-shadow: 0 0 2px rgba(52, 211, 153, 0.2); }
    }
    
    .glow-name {
        text-align: center;
        font-size: 17px;
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 15px;
        animation: glowing 2.5s infinite;
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

# 3. سەرۆکی پڕۆژەی
st.markdown("<h1 style='text-align: center; color: #34d399;'>🌿 زکر • پەناگەها دەروونی و ڕۆحانی</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 15px;'>ڕێبەرێ ڕۆحانی؛ هەر پرسیارەکا دەروونی یان ئاینی بنڤیسە تاوەکو بەرسڤەکا تایبەت و ب ئایەت و دوعا بۆ تە ئامادە بکەت.</p>", unsafe_allow_html=True)

# ناڤێ تە یێ گڵۆپێ (ل جهێ خطە سور)
st.markdown("<div class='glow-name'>✨ دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی 🌿</div>", unsafe_allow_html=True)
st.markdown("---")

# سیستەمێ تابان (Tabs) - بێ ناڤێ AI
tab1, tab2 = st.tabs(["🌿 ڕێبەرێ ڕۆحانی", "📿 مسبحەیا ئەلیکترۆنی"])

# --- بەشێ یەکەم: بەرسڤدانا دەروونی و ئاینی ---
with tab1:
    st.markdown("<p style='text-align: right; direction: rtl; color: #34d399; font-weight: bold;'>🧠 پرسیار، کێشە یان هەستێ خۆ لێرە بنڤیسە:</p>", unsafe_allow_html=True)
    user_prompt = st.text_area("", placeholder="بۆ نموونە: ئەز ترسا ژ پاشەڕۆژێ هەم، چ بکەم تا دلێ من ئارام ببێت؟ یان پرسیارەکێ ئاینی بپرسە...", height=120)

    if st.button("✨ ڤەکۆلین و وەرگرتنا بەرسڤێ", use_container_width=True):
        if not user_prompt.strip():
            st.warning("تکایە دەستپێکێ پرسیار یان هەستێ خۆ ل خانەیێ بنڤیسە!")
        elif model is None:
            st.error("تکایە پێشەکی کلیلا API لە کۆدی دابنە.")
        else:
            with st.spinner("⏳ مژوولی دروستکرنا بەرسڤێیە..."):
                try:
                    system_instruction = (
                        "تو ڕێبەرەکێ شارەزا و هۆشمەند‌ی لە بوارێ دەروونی، ئاینی ئیسلامی و قورئانا پیرۆز. "
                        "هەر دەما بەکارهێنەر پرسیارەک یان کێشەیەک بنڤیسێت، بەرسڤەکا گەلەک نەرم، ئارامکەر، "
                        "زانستی و ئیسلامی ب زمانێ کوردی (بادینی یان سۆرانی یا پاک) بدە، و گونجایترین ئایەتێن قورئانێ "
                        "یان دوعایێن پڕۆتۆکۆلی لەگەڵ ئامۆژگاریێن دەروونی تێدا بونەویسە. بەرسڤا تە نەبی هەمان تشت بۆ هەمی کەسان، بەلکو تایبەت ب وێ پرسیارێ بێت."
                    )
                    
                    full_query = f"{system_instruction}\n\nپرسیاڕا بەکارهێنەری: {user_prompt}"
                    response = model.generate_content(full_query)
                    
                    st.markdown(
                        f"""
                        <div class="ai-card">
                            <div style="font-size: 16px; color: #34d399; font-weight: bold; margin-bottom: 12px;">💡 ڕێنماییا ڕۆحانی:</div>
                            <div style="font-size: 16px; color: #ffffff; line-height: 1.8; direction: rtl; text-align: right;">
                                {response.text}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                except Exception as ex:
                    st.error(f"تکایە پشکست ڕوودا یان کلیلا API نە دروستە: {ex}")

# --- بەشێ دووەم: مسبحەیا ئەلیکترۆنی ---
with tab2:
    st.markdown("<h3 style='text-align: center; color: #34d399;'>📿 مسبحەیا ئەلیکترۆنی یا زکران</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 14px;'>هەر دەمەکێ تو زکرەکێ دکەی، ل دوگمەیێ بکوتە تاوەکو هژمار پاشەکەوت بێت.</p>", unsafe_allow_html=True)
    
    if 'zikr_count' not in st.session_state:
        st.session_state.zikr_count = 0

    st.markdown(f"<div class='counter-display'>{st.session_state.zikr_count}</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ زکرەک بکە", use_container_width=True):
            st.session_state.zikr_count += 1
            st.rerun()
    with col2:
        if st.button("🔄 ژمارەی سفڕ بکە", use_container_width=True):
            st.session_state.zikr_count = 0
            st.rerun()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #64748b; font-size: 12px;'>پڕۆژەی زکر • گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
