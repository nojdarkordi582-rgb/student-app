import streamlit as st
import google.generativeai as genai

# ڕێکخستنا سەرەکی
st.set_page_config(page_title="بەرەو خودێ", page_icon="🤲", layout="centered")

st.markdown("<h2 style='text-align: right; direction: rtl; color: #059669;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: right; direction: rtl;'>سلاڤ، نوژدار - سیستەمێ دوعایێن شاشەیا قفل</h3>", unsafe_allow_html=True)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # بەکارئینانا st.selectbox و st.radio ب شێوازەکێ سادە بێ کێشە
    duaa_category = st.selectbox("جۆرێ زکر یان دوعایێ هەلبژێرە:", [
        "دوعایێن ئارامیا دلان و ڕووناکیا ناخی",
        "زکرێن پاراستنێ ل دەمێ قفلکرنا موبایلێ",
        "دوعایێن رزق، برەکەت و ڤەکرنا دەرگەهان",
        "ئایەتێن قورئانی یێن کورتی کاریگەر"
    ])

    chosen_position = st.radio("🎯 جھێ دوعایێ لەسەر شاشەیا قفلێ:", [
        "جهێ سەرەوە (ژووریا کاتی)",
        "جهێ ناڤەڕаст (ناڤەندا شاشەی)",
        "جهێ خوارێ (نێزیکی ڤەکرنێ)"
    ])

    # دوگمەیا سەرەکی ب بێ هیچ دیزاینەکی ئالۆز تاوەکو سەد دەرسەد ل سەر مۆبایلا کلیک لێ بێت
    if st.button("✨ چێکرنا زکری بۆ شاشەیا قفل"):
        with st.spinner("خەریکی ئامادەکرنێیە..."):
            prompt = f"ب زمانێ بادینی، دوعایەکی زۆر کورت، پڕ مانا و کاریگەر بۆ شاشەیا قفلێ د پشکا ({duaa_category}) و جهێ ({chosen_position}) بنووسە."
            response = model.generate_content(prompt)
            
            st.success("🔒 دوعا ب سەرکەفتن هاتە چێکرن:")
            st.info(response.text)

except Exception as e:
    st.error(f"⚠️ کێشە هەەیە: {e}")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray; font-size: 12px;'>پڕۆژەی بەرەو خودێ • نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
