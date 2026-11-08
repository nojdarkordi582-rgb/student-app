import streamlit as st
import google.generativeai as genai

# ڕێکخستنی لاپەڕە و دیزاینی فول مودرێن
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

    .content-box {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        margin-top: 20px;
    }

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

    if st.button("وەرگرتنی وەڵامی قووڵ"):
        if life_question:
            with st.spinner("خەریکی شرۆڤەکرن و ئامادەکرنا وەڵامێیە..."):
                try:
                    query_keyword = "nature space galaxy light philosophy"
                    if "خوێن" in life_question or "خویندن" in life_question or "دخول" in life_question:
                        query_keyword = "library books studying education dark academia"
                    elif "خودێ" in life_question or "باوەر" in life_question or "ئاین" in life_question:
                        query_keyword = "cosmos night sky stars universe spiritual"
                    elif "مرۆڤ" in life_question or "ژیان" in life_question or "دژیم" in life_question:
                        query_keyword = "deep ocean mountain horizon landscape cinematic"

                    bg_image_url = f"https://source.unsplash.com/1600x900/?{query_keyword}"

                    st.markdown(
                        f"""
                        <style>
                        .stApp {{
                            background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.92)), url('{bg_image_url}');
                            background-size: cover;
                            background-position: center;
                            background-attachment: fixed;
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                    )

                    prompt = f"""
                    تو زانا، فەیلەسوف و شارەزایەکی مەزن لە بواری ئاینی، دەروونناسی و وەڵامدانی پرسیارە قووڵەکانی ژیان.
                    کەسێک ئەم پرسیارەی هەیە: '{life_question}'
                    تکایە وەڵامێکی زۆر لۆژیکی، ئارامبەخش، لەسەر بنەمای قورئان، حیکمەتی دروستبوون و زانستی سەردەم بە زمانی کوردی پێشکەش بکە.
                    """
                    
                    response = model.generate_content(prompt)
                    
                    st.markdown(
                        f"""
                        <div class="content-box">
                            <h3 style='color: #38bdf8; margin-bottom: 15px;'>📌 وەڵام و شرۆڤەی قووڵ:</h3>
                            <div style='line-height: 1.8; font-size: 16px; color: #e2e8f0;'>
                                {response.text.replace(chr(10), '<br>')}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                except Exception as e:
                    st.error(f"⚠️ هەڵە ڕووی دا: {e}")
        else:
            st.warning("⚠️ تکایە پێشەکی پرسیارەک خۆ ل ڤێرە بنڤیسە.")

except Exception as e:
    st.error("⚠️ تکایە دڵنیابە کە کلیلێ سیستەمی لە بەشی Secretsـی Streamlit بە ڕێکی دانراوە.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #94a3b8; font-size: 13px;'>دیزاینی فول مودرێن • دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
