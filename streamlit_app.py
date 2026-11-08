import streamlit as st
from PIL import Image
import google.generativeai as genai

# دابینکری بۆ ڕێکوپێکرنا نڤیسینێ ژ ڕاست بۆ چەپ (RTL)
st.markdown(
    """
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📚 بەرنامەیێ قوتابیان - پڕ گرێدای ب AI (Gemini)")

# وەرگرتنا کلیلێ API لە بەکارهێنەر
api_key = st.text_input("کلیلێ API (Google Gemini API Key) لێرە بنڤیسە:", type="password")

if api_key:
    # ڕێکخستنا API
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    nav = st.text_input("تکایە ناڤێ خۆ بنڤیسە:")

    if nav:
        st.success(f"سلاڤ، {nav}! بەرنامە نوکە ب تەواوی ب AI ڤە هاتە گرێدان.")

    menu = st.selectbox("تکایە خزمەتگوزارییەکێ هەلبژێرە:", [
        "شیکارکرنا پرسیاران ب ڕێکا AI (پشک بە پشک) 🤖",
        "ئامۆژگاریێن خوەیندنێ و خۆشیێ 💡",
        "نڤیسین و پاشەکەوتکرنا تێبینیەکێ 📝"
    ])

    if menu == "شیکارکرنا پرسیاران ب ڕێکا AI (پشک بە پشک) 🤖":
        st.subheader("--- هاریکارێ زیرەکێ AI 🤖 ---")
        
        uploaded_file = st.file_uploader("وێنەیەکێ پرسیارێ باربکە:", type=["jpg", "jpeg", "png"])
        question_text = st.text_input("یان دەقێ پرسیارێ (نڤیسین) لێرە بنڤیسە:")

        if st.button("ناردن بۆ AI و دەرئێخستنا شیکاریا تەواو"):
            if uploaded_file is not None or question_text:
                with st.spinner("AI خەریکی خوەندنا وێنە و پرسیارێیە و شیکاریا پشک بە پشک دکەت..."):
                    try:
                        # ئامادەکرنا وێنەی ئەگەر هەبێت
                        image = Image.open(uploaded_file) if uploaded_file else None
                        
                        # دروستکرنا ڕێنمایێ بۆ AI بۆ ئەوەی بە ژمارە و شێوازی پەڕتووکی وەڵام بداتەوە
                        prompt = f"""
                        تو مامۆستایەکی تایبەت و شارەزای لە بوارە جیاوازەکاندا (بیرکاری، فیزیا، زانست، وێژە). 
                        تکایە ئەم پرسیارە یان ئەم وێنەیە بە شێوازێکی پشک بە پشک، ژمارەیی، زانستی و ورد 
                        (وەک شێوازی پەڕتووکی قوتابخانە) شیکار بکە. ئەگەر پرسیارەکە بیرکاری یان فیزیا بێت، 
                        هەموو هەنگاوەکانی حلکردن، یاساکان و ئەنجامی کۆتایی بە ڕێکوپێکی بنووسە.
                        دەقێ زێدە: {question_text}
                        """
                        
                        contents = [prompt]
                        if image:
                            contents.append(image)

                        # دەرئێخستنا وەڵامێ ژ مۆدێلا گوگڵ جیمینی
                        response = model.generate_content(contents)
                        
                        st.success("✅ شیکاریا AI ب سەرکەفتن هاتە ئەنجامدان!")
                        st.markdown("### 📌 شیکاریا زیرەک:")
                        st.write(response.text)
                        
                    except Exception as e:
                        st.error(f"⚠️ ئەنجامدانا پەیوەندیێ سەرکەفتن نەبوو. تکایە پشکنی دەقێ کلیلێ API: {e}")
            else:
                st.warning("⚠️ تکایە پێشەکی وێنەیەک باربکە یان پرسیارەک بنڤیسە.")

    elif menu == "ئامۆژگاریێن خوەیندنێ و خۆشیێ 💡":
        st.subheader("--- ئامۆژگاریێن خوەیندنێ 💡 ---")
        st.markdown("1. هەمیشە دەمێ خۆ ڕێکخە.")
        st.markdown("2. شوێنێ خوێندنێ گوهڕە یان قەلەمێن ڕەنگاوڕەنگ بەکاربینە.")

    elif menu == "نڤیسین و پاشەکەوتکرنا تێبینیەکێ 📝":
        st.subheader("--- پشکا تێبینیان 📝 ---")
        note = st.text_input("تێبینیا خۆ ل ڤێرە بنڤیسە:")
        if st.button("پاشەکەوتکرنا تێبینیێ"):
            if note:
                st.success(f'✅ پەیاما تە وەرگرت: "{note}"')

else:
    st.info("📌 بۆ چالاککرنا AI، تکایە کلیلەکێ API (Gemini API Key) لە گوگڵ وەرگرە و لە بۆشایی سەرەوەدا بنووسە تاوەکو بەرنامە ڕاستەوخۆ دەست بە کار بکات.")
    
