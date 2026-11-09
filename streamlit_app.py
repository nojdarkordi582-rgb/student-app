import streamlit as st
import google.generativeai as genai

# ڕێکخستنا لاپەڕەی بۆ RTL و دیزاینی فول مۆدێرن
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
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 25px;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
        margin-bottom: 25px;
    }

    .lockscreen-preview {
        background: rgba(2, 44, 34, 0.95);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(74, 222, 128, 0.5);
        padding: 30px;
        border-radius: 24px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.7);
        text-align: center;
        margin-top: 20px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 16px;
        font-weight: bold;
        height: 55px;
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(5, 150, 105, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(5, 150, 105, 0.7);
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="header-card">
        <div style="font-size: 16px; color: #6ee7b7; font-weight: 600;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        <h2 style="margin: 8px 0; color: #ffffff;">سلاڤ، نوژدار</h2>
        <div style="font-size: 14px; color: #a7f3d0;">سیستەمێ خێرا دوعایێن شاشەیا قفل (ب ٣ چرکان) • بەرەو خودێ</div>
    </div>
    """,
    unsafe_allow_html=True
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # بەکارئینانا مۆدێلا گەلەک خێرا flash
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.markdown("### 📱 زکر و دوعایێن شاشەیا قفلا موبایلێ (لەزەک)")
    
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

    if st.button("✨ چێکرنا ب لەز (د ٣ چرکان دا)"):
        # داكو ژ ١ بۆ ٣ چرکان وەڵام دەستبەجێ بهێت، پرۆمپت هاتە کورتکرن و خێرا مۆدێلی هاتە بلندکرن
        prompt = f"ب زمانێ بادینی، دوعایەکی زۆر کورت، پڕ مانا و کاریگەر بۆ شاشەیا قفلێ د پشکا ({duaa_category}) و جهێ ({screen_position}) بنووسە."
        
        response = model.generate_content(prompt)
        
        st.markdown(
            f"""
            <div class="lockscreen-preview">
                <div style="font-size: 13px; color: #34d399; margin-bottom: 10px;">🔒 نموونەیا شاشەیا قفل (Lock Screen Preview)</div>
                <div style="font-size: 20px; font-weight: bold; color: #ffffff; margin-bottom: 15px;">{screen_position}</div>
                <div style='line-height: 1.8; font-size: 17px; color: #ecfdf5; background: rgba(0,0,0,0.3); padding: 20px; border-radius: 12px;'>
                    {response.text.replace(chr(10), '<br>')}
                </div>
                <div style="margin-top: 15px; font-size: 12px; color: #9ca3af;">✅ د ۳ چرکان دا ب سەرکەفتن هاتە چێکرن!</div>
            </div>
            """,
            unsafe_allow_html=True
        )

except Exception as e:
    st.error(f"⚠️ هەڵە ڕووی دا: {e}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #6ee7b7; font-size: 13px;'>پڕۆژەی بەرەو خودێ (شاشەیا قفل) • دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
