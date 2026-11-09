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
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    /* دیزاینی شاشەیا قفل یا موبایلێ (Interactive Lock Screen Container) */
    .lockscreen-container {
        background: linear-gradient(180deg, rgba(3, 30, 20, 0.95) 0%, rgba(1, 15, 10, 0.98) 100%);
        border: 3px solid rgba(74, 222, 128, 0.4);
        padding: 30px;
        border-radius: 35px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
        text-align: center;
        margin-top: 20px;
        position: relative;
    }

    .clock-display {
        font-size: 42px;
        font-weight: 300;
        color: #ffffff;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }

    .date-display {
        font-size: 14px;
        color: #a7f3d0;
        margin-bottom: 25px;
    }

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
        <div style="font-size: 13px; color: #a7f3d0;">سیستەمێ شاشەیا قفل (ب حەزا دلێ خۆ جهی دیار بکە) • بەرەو خودێ</div>
    </div>
    """,
    unsafe_allow_html=True
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.markdown("### 📱 دیزاینکرنا شاشەیا قفلا موبایلێ")
    
    duaa_category = st.selectbox("جۆرێ زکر یان دوعایێ هەلبژێرە:", [
        "دوعایێن ئارامیا دلان و ڕووناکیا ناخی",
        "زکرێن پاراستنێ ل دەمێ قفلکرنا موبایلێ",
        "دوعایێن رزق، برەکەت و ڤەکرنا دەرگەهان",
        "ئایەتێن قورئانی یێن کورتی کاریگەر"
    ])

    # لێرە بەکارهێنەر ب حەزا دلێ خۆ ئەو جهێ دڤێت لسەر شاشەی هەلبژێرێت
    chosen_position = st.selectbox("🎯 ئەو جهێ دڤێت دوعا لەسەر شاشەیا قفل بهێتە دانان هەلبژێرە:", [
        "جهێ سەرەوە (ژووریا کاتی / ل بن دەمژمێرێ)",
        "جهێ ناڤەڕаст (ناڤەندا شاشەی / جهێ سەرەکی)",
        "جهێ خوارێ (نێزیکی ئاماژەیا ڤەکرنا موبایلێ)",
        "جهێ تایبەت (سەر شاشەی ب دیمەنەکێ ئازاد)"
    ])

    if st.button("✨ چێکرنا زکری بۆ شاشەیا قفل (ب ٣ چرکان)"):
        prompt = f"ب زمانێ بادینی، دوعایەکی زۆر کورت، پڕ مانا و کاریگەر بۆ شاشەیا قفلێ د پشکا ({duaa_category}) بنووسە، گۆیا ل جهێ ({chosen_position}) ل سەر شاشەی هاتبیتە دانان."
        
        response = model.generate_content(prompt)
        
        # نیشادانا شاشەیا قفل یا پڕۆتۆتایپ ب کات و دیمەنێ ڕاستەقینە
        st.markdown(
            f"""
            <div class="lockscreen-container">
                <div class="clock-display">٠٩:٤١</div>
                <div class="date-display">دووشەممە، ٩ێ چرییا دووماهیێ</div>
                
                <div style="font-size: 11px; color: #34d399; margin-bottom: 10px; background: rgba(5,150,105,0.2); padding: 5px 10px; border-radius: 8px; display: inline-block;">
                    📍 جھێ هاتیە هەلبژارتن: {chosen_position}
                </div>

                <div style='line-height: 1.8; font-size: 16px; color: #ecfdf5; background: rgba(0,0,0,0.5); padding: 20px; border-radius: 16px; border: 1px solid rgba(74,222,128,0.3); margin-top: 10px;'>
                    {response.text.replace(chr(10), '<br>')}
                </div>
                
                <div style="margin-top: 20px; font-size: 12px; color: #9ca3af;">🔒 شاشەیا قفلا موبایلێ ب سەرکەفتن هاتە ڕێکخستن!</div>
            </div>
            """,
            unsafe_allow_html=True
        )

except Exception as e:
    st.error(f"⚠️ هەڵە ڕووی دا: {e}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #6ee7b7; font-size: 12px;'>پڕۆژەی بەرەو خودێ (شاشەیا قفل) • دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
