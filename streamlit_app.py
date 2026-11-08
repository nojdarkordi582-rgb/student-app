import streamlit as st
from PIL import Image
import google.generativeai as genai

# دابینکری بۆ ڕێکوپێکرنا نڤیسینێ ژ ڕاست بۆ چەپ (RTL) و لێدانا ڕووناکییا گەش (Glow Animation)
st.markdown(
    """
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
    }
    
    @keyframes glowEffect {
        0% {
            color: #1b5e20;
            text-shadow: 0 0 2px rgba(76, 175, 80, 0.3);
        }
        50% {
            color: #66bb6a;
            text-shadow: 0 0 15px rgba(76, 175, 80, 0.9), 0 0 25px rgba(129, 199, 132, 0.7);
        }
        100% {
            color: #1b5e20;
            text-shadow: 0 0 2px rgba(76, 175, 80, 0.3);
        }
    }

    .glowing-box {
        animation: glowEffect 2.5s infinite ease-in-out;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# حەمد و شوکر بوو خودایێ مەزن بن (ب ڕەنگێ سەوزێ گەشاوە و بروسکەدار)
st.markdown("<h3 class='glowing-box'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</h3>", unsafe_allow_html=True)
st.markdown("<h4 class='glowing-box'>« الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ »</h4>", unsafe_allow_html=True)
st.markdown("---")

# ناونیشانی سەرەکی بەرنامە
st.title("📚 بەرنامەیێ قوتابیان - هەمی بابەتێن پرۆفیشناڵ (ب AI)")

# وەرگرتنا کلیلێ API لە بەکارهێنەر بۆ کارپێکرنا AI
api_key = st.text_input("کلیلێ API (Google Gemini API Key) لێرە بنڤیسە بۆ کارپێکرنا AI:", type="password")

# دیارکردنی دروستکەری بەرنامە (بە هەمان ڕووناکییا گەش)
st.markdown("---")
st.markdown("<div class='glowing-box' style='font-size: 18px;'>👨‍💻 دروستکەر و گەشەپێدەری بەرنامەی: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
st.markdown("---")

if api_key:
    # ڕێکخستنا API
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    nav = st.text_input("تکایە ناڤێ خۆ بنڤیسە:")

    if nav:
        st.success(f"سلاڤ، {nav}! بەرنامە نوکە بە تەواوی ل ژێر دەستهەڵاتا AI دکار دکەت.")

    menu = st.selectbox("تکایە خزمەتگوزارییەکێ هەلبژێرە:", [
        "شیکارکرنا پرسیاران ب ڕێکا AI (پشک بە پشک) 🤖",
        "دیتنا خشتەیا رۆژی (وانە) 📅",
        "ئامۆژگاریێن خوەیندنێ و خۆشیێ 💡",
        "نڤیسین و پاشەکەوتکرنا تێبینیەکێ 📝"
    ])

    if menu == "شیکارکرنا پرسیاران ب ڕێکا AI (پشک بە پشک) 🤖":
        st.subheader("--- شیکارکەرێ پرسیارێن پرۆفیشناڵ ب ڕێکا AI 🤖 ---")
        
        subject_category = st.selectbox("تکایە بابەتی هەلبژێرە:", [
            "بیرکاری (Mathematics)",
            "فیزیا و کیمیا (Physics & Chemistry)",
            "مێژوو و جۆگرافیا (History & Geography)",
            "زمان و وێژە (Literature & Languages)",
            "زینده‌وه‌رزانی (Biology)"
        ])

        uploaded_file = st.file_uploader("وێنەیەکێ پرسیارێ باربکە:", type=["jpg", "jpeg", "png"])
        question_text = st.text_input("یان دەقێ پرسیارێ (نڤیسین) لێرە بنڤیسە:")

        if st.button("ناردن بۆ AI و دەرئێخستنا شیکاریا تەواو"):
            if uploaded_file is not None or question_text:
                with st.spinner("AI خەریکی خوەندنا وێنە و پرسیارێیە و شیکاریا پشک بە پشک دکەت..."):
                    try:
                        image = Image.open(uploaded_file) if uploaded_file else None
                        
                        prompt = f"""
                        تو مامۆستایەکی تایبەت و شارەزای لە بوارەی ({subject_category}). 
                        تکایە ئەم پرسیارە یان ئەم وێنەیە بە شێوازێکی پشک بە پشک، ژمارەیی، زانستی و ورد 
                        (وەک شێوازی پەڕتووکی قوتابخانە) شیکار بکە. هەموو هەنگاوەکانی حلکردن، یاساکان و ئەنجامی کۆتایی بە ڕێکوپێکی بنووسە.
                        دەقێ زێدە: {question_text}
                        """
                        
                        contents = [prompt]
                        if image:
                            contents.append(image)

                        response = model.generate_content(contents)
                        
                        st.success("✅ شیکاریا AI ب سەرکەفتن هاتە ئەنجامدان!")
                        st.markdown("### 📌 شیکاریا زیرەک:")
                        st.write(response.text)
                        
                    except Exception as e:
                        st.error(f"⚠️ پەیوەندی ب AI سەرکەفتن نەبوو. تکایە پشکنی دەقێ کلیلێ API: {e}")
            else:
                st.warning("⚠️ تکایە پێشەکی وێنەیەک باربکە یان پرسیارەک بنڤیسە.")

    elif menu == "دیتنا خشتەیا رۆژی (وانە) 📅":
        st.subheader("--- خشتەیا وانەیێن هەفتەیی ---")
        st.write("• **شەممە:** بیرکاری و زانست")
        st.write("• **دووشەممە:** فیزیا و کیمیا")
        st.write("• **سێشەممە:** مێژوو و وێژە")
        st.write("• **چارشەممە:** زمان و زیندەوەرورزانی")
        st.write("• **پێنجشەممە:** تاقیکردنەوە و پشوو")

    elif menu == "ئامۆژگاریێن خوەیندنێ و خۆشیێ 💡":
        st.subheader("--- ئامۆژگاریێن خوەیندنێ و خۆشیێ 💡 ---")
        st.markdown("1. هەمیشە دەمێ خۆ ڕێکخە و پۆمۆدۆرۆ تاقی بکە.")
        st.markdown("2. باوەریا تە ب خۆ هەبێت، تو دشکەی سەرکەفتنی بدەستی!")

    elif menu == "نڤیسین و پاشەکەوتکرنا تێبینیەکێ 📝":
        st.subheader("--- پشکا تێبینیان 📝 ---")
        note = st.text_input("تێبینیا خۆ ل ڤێرە بنڤیسە:")
        if st.button("پاشەکەوتکرنا تێبینیێ"):
            if note:
                st.success(f'✅ پەیاما تە وەرگرت: "{note}"')

else:
    st.info("📌 بۆ چالاککرنا AI، تکایە کلیلەکێ API (Gemini API Key) لە سەرەوەدا بنووسە تاوەکو بەرنامە ڕاستەوخۆ دەست بە کار بکات.")
    
