import streamlit as st
import google.generativeai as genai

# ڕێکخستنا لاپەڕەی بۆ RTL و چارەسەرکرنا کێشا کلیککرنێ ل سەر مۆبایلا
st.markdown(
    """
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        background: radial-gradient(circle at center, #022c22 0%, #000000 100%);
        color: #f0fdf4;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .header-card {
        background: rgba(6, 78, 59, 0.75);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    .lockscreen-preview {
        background: rgba(2, 44, 34, 0.95);
        border: 2px solid rgba(74, 222, 128, 0.5);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
        text-align: center;
        margin-top: 20px;
    }

    /* پشتڕاستکرنا وێ چەندێ دوگمە ب ساناهی ل سەر مۆبایلا بهێتە کلیککرن */
    .stButton > button {
        width: 100% !important;
        border-radius: 16px !important;
        font-weight: bold !important;
        height: 55px !important;
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 0 4px 15px rgba(5, 150, 105, 0.5) !important;
        cursor: pointer !important;
        z-index: 9999 !important;
        position: relative !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="header-card">
        <div style="font-size: 15px; color: #6ee7b7; font-weight: 600;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        <h3 style="margin: 6px 0; color: #ffffff;">سلاڤ، نوژدار</h3>
        <div style="font-size: 13px; color: #a7f3d0;">سیستەمێ دوعایێن شاشەیا قفل • بەرەو خودێ</div>
    </div>
    """,
    unsafe_allow_html=True
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.markdown("### 📱 زکر و دوعایێن شاشەیا قفلا موبایلێ")
    
    duaa_category = st.selectbox("جۆرێ زکر یان دوعایێ بۆ شاشەیا قفل هەلبژێرە:", [
        "دوعایێن ئارامیا دلان و ڕووناکیا ناخی",
        "زکرێن پاراستنێ ل دەمێ قفلکرنا موبایلێ",
        "دوعایێن رزق، برەکەت و ڤەکرنا دەرگەهان",
        "ئایەتێن قورئانی یێن کورتی کاریگەر"
    ])

    screen_position = st.radio("تە دڤێت ڤی زکری لە کیژ جهـ ل سەر شاشەیا قفلێ دابنێی؟", [
        "📍 جهێ سەرەوەی شاشەی (سەرێ کاتی / Clock Area)",
        "📍 جهێ ناڤەڕаст (لە ناڤەندا شاشەی ب دیمەنەکێ جوان)",
        "📍 جهێ خوارێ (نێزیکی دوگمەیا ڤەکرنێ)"
    ])

    # دوگمەیا سەرەکی ب بێ ئاریشە و راستەوخۆ
    if st.button("✨ چێکرنا ب لەز (د ٣ چرکان دا)"):
        prompt = f"ب زمانێ بادینی، دوعایەکی زۆر کورت، پڕ مانا و کاریگەر بۆ شاشەیا قفلێ د پشکا ({duaa_category}) و جهێ ({screen_position}) بنووسە."
        
        response = model.generate_content(prompt)
        
        st.markdown(
            f"""
            <div class="lockscreen-preview">
                <div style="font-size: 12px; color: #34d399; margin-bottom: 8px;">🔒 نموونەیا شاشەیا قفل (Lock Screen Preview)</div>
                <div style="font-size: 18px; font-weight: bold; color: #ffffff; margin-bottom: 12px;">{screen_position}</div>
                <div style='line-height: 1.8; font-size: 16px; color: #ecfdf5; background: rgba(0,0,0,0.4); padding: 18px; border-radius: 12px;'>
                    {response.text.replace(chr(10), '<br>')}
                </div>
                <div style="margin-top: 12px; font-size: 11px; color: #9ca3af;">✅ ب سەرکەفتن هاتە چێکرن!</div>
            </div>
            """,
            unsafe_allow_html=True
        )

except Exception as e:
    st.error(f"⚠️ هەڵە ڕووی دا: {e}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #6ee7b7; font-size: 12px;'>پڕۆژەی بەرەو خودێ (شاشەیا قفل) • دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
