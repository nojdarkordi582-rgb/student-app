import streamlit as st
from PIL import Image
import google.generativeai as genai

# ڕێکخستنی پەڕە بۆ RTL (ڕاست بۆ چەپ) و دیزاینی کارت
st.markdown(
    """
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        background-color: #0e1117;
        color: #ffffff;
    }
    
    .header-card {
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 14px;
        font-weight: bold;
        height: 55px;
        background: linear-gradient(135deg, #1f2937, #111827);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        border-color: #4caf50;
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="header-card">
        <div style="font-size: 16px; opacity: 0.9;">🌙 شەف باش</div>
        <h2 style="margin: 5px 0;">سلاڤ، نوژدار</h2>
        <div style="font-size: 14px; opacity: 0.8;">بەرنامەیێ قوتابیان - هەمی بابەتێن پرۆفیشناڵ</div>
    </div>
    """,
    unsafe_allow_html=True
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.markdown("### 🗂️ خزمەتگوزاریێن قوتابیان")

    col1, col2, col3 = st.columns(3)

    with col1:
        btn_classes = st.button("🎓 شیکارکرنا پرسیاران")
    with col2:
        btn_schedule = st.button("📅 خشتەیا رۆژی")
    with col3:
        btn_advice = st.button("💡 ئامۆژگاریێن خوەیندنێ")

    col4, col5 = st.columns(2)
    with col4:
        btn_notes = st.button("📝 تێبینیێن من")

    st.markdown("---")

    selected_service = "شیکارکرنا پرسیاران"
    if btn_classes:
        selected_service = "شیکارکرنا پرسیاران"
    elif btn_schedule:
        selected_service = "خشتەیا رۆژی"
    elif btn_advice:
        selected_service = "ئامۆژگاریێن خوەیندنێ"
    elif btn_notes:
        selected_service = "تێبینیێن من"

    if selected_service == "شیکارکرنا پرسیاران":
        st.subheader("--- شیکارکەرێ پرسیارێن پەڕتووکی ---")
        
        subject_category = st.selectbox("تکایە بابەتی هەلبژێرە:", [
            "بیرکاری (Mathematics)",
            "فیزیا و کیمیا (Physics & Chemistry)",
            "مێژوو و جۆگرافیا (History & Geography)",
            "زمان و وێژە (Literature & Languages)",
            "زینده‌وه‌رزانی (Biology)"
        ])

        uploaded_file = st.file_uploader("وێنەیەکێ پرسیارێ باربکە:", type=["jpg", "jpeg", "png"])
        question_text = st.text_input("یان دەقێ پرسیارێ (نڤیسین) لێرە بنڤیسە:")

        if st.button("دەرئێخستنا شیکاریا تەواو"):
            if uploaded_file is not None or question_text:
                with st.spinner("خەریکی خوەندنا وێنە و پرسیارێیە و شیکاریا پشک بە پشک دکەت..."):
                    try:
                        image = Image.open(uploaded_file) if uploaded_file else None
                        
                        prompt = f"""
                        تو مامۆستایەکی تایبەت و شارەزای لە بوارەی ({subject_category}). 
                        تکایە ئەم پرسیارە یان ئەم وێنەیە بە شێوازێکی پشک بە پشک، ژمارەیی، زانستی و ورد شیکار بکە. 
                        هەموو هەنگاوەکانی حلکردن، یاساکان و ئەنجامی کۆتایی بە ڕێکوپێکی بنووسە.
                        دەقێ زێدە: {question_text}
                        """
                        
                        contents = [prompt]
                        if image:
                            contents.append(image)

                        response = model.generate_content(contents)
                        
                        st.success("✅ شیکاریا پرسیارێ ب سەرکەفتن هاتە ئەنجامدان!")
                        st.markdown("### 📌 شیکاریا پەڕتووکی:")
                        st.write(response.text)
                        
                    except Exception as e:
                        st.error(f"⚠️ ئەنجامدانا شیکاریێ سەرکەفتن نەبوو: {e}")
            else:
                st.warning("⚠️ تکایە پێشەکی وێنەیەک باربکە یان پرسیارەک بنڤیسە.")
    
    elif selected_service == "خشتەیا رۆژی":
        st.subheader("--- خشتەیا وانەیێن هەفتەیی 📅 ---")
        st.write("• **شەممە:** بیرکاری و زانست")
        st.write("• **دووشەممە:** فیزیا و کیمیا")
        st.write("• **سێشەممە:** مێژوو و وێژە")
        st.write("• **چارشەممە:** زمان و زیندەوەرورزانی")
        st.write("• **پێنجشەممە:** تاقیکردنەوە و پشوو")

    elif selected_service == "ئامۆژگاریێن خوەیندنێ":
        st.subheader("--- ئامۆژگاریێن خوەیندنێ و خۆشیێ 💡 ---")
        st.markdown("1. هەمیشە دەمێ خۆ ڕێکخە و پۆمۆدۆرۆ تاقی بکە.")
        st.markdown("2. باوەریا تە ب خۆ هەبێت، تو دشکەی سەرکەفتنی بدەستی!")

    elif selected_service == "تێبینیێن من":
        st.subheader("--- پشکا تێبینیان 📝 ---")
        note = st.text_input("تێبینیا خۆ ل ڤێرە بنڤیسە:")
        if st.button("پاشەکەوتکرنا تێبینیێ"):
            if note:
                st.success(f'✅ پەیاما تە وەرگرت: "{note}"')

except Exception as e:
    st.error("⚠️ تکایە دڵنیابە کە کلیلێ سیستەمی لە بەشی Secretsـی Streamlit بە ڕێکی دانراوە.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #888; font-size: 14px;'>دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
