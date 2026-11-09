import streamlit as st
import google.generativeai as genai

# رێکخستنا لاپەڕەی بۆ RTL و دیزاینی فول مۆدێرن (Glassmorphism & Dynamic Background)
st.markdown(
    """
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        background: radial-gradient(circle at center, #064e3b 0%, #022c22 100%);
        color: #f0fdf4;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .header-card {
        background: rgba(6, 78, 59, 0.7);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 25px;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        margin-bottom: 30px;
    }

    .content-box {
        background: rgba(2, 44, 34, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(74, 222, 128, 0.3);
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
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(5, 150, 105, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(5, 150, 105, 0.6);
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    }

    .stTextInput textarea, .stTextArea textarea {
        background-color: rgba(6, 78, 59, 0.6) !important;
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
        <div style="font-size: 16px; color: #6ee7b7; font-weight: 600;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        <h2 style="margin: 8px 0; color: #ffffff;">سلاڤ، نوژدار</h2>
        <div style="font-size: 14px; color: #a7f3d0;">پڕۆژەی **بەرەو خودێ** - رێڕەوێ ناسینا پەروەردگاری و ئارامیا دلان</div>
    </div>
    """,
    unsafe_allow_html=True
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # دروستکرنا دوگمە و پشکێن سەرەکی یێن بەرنامەی ب شێوازێ کارت
    st.markdown("### 🗂️ پشکێن سەرەکی یێن بەرنامەی")

    col1, col2, col3 = st.columns(3)

    with col1:
        btn_deep = st.button("🌌 پرسیارێن قووڵ و خوداناسی")
    with col2:
        btn_quran = st.button("📖 قورئانا پیرۆز و ئارامی")
    with col3:
        btn_zekr = st.button("☀️ زکر و یادی خودا")

    col4, col5 = st.columns(2)
    with col4:
        btn_duaa = st.button("🤲 دوعا و مناجات")
    with col5:
        btn_notes = st.button("📝 تێبینیێن ڕۆحی")

    st.markdown("---")

    # دیارکرنا پشکا هاتھیە هەلبژارتن
    selected_service = "پرسیارێن قووڵ و خوداناسی"
    if btn_deep:
        selected_service = "پرسیارێن قووڵ و خوداناسی"
    elif btn_quran:
        selected_service = "قورئانا پیرۆز و ئارامی"
    elif btn_zekr:
        selected_service = "زکر و یادی خودا"
    elif btn_duaa:
        selected_service = "دوعا و مناجات"
    elif btn_notes:
        selected_service = "تێبینیێن ڕۆحی"

    # ١. پرسیارێن قووڵ و خوداناسی
    if selected_service == "پرسیارێن قووڵ و خوداناسی":
        st.markdown("### 🧠 وەڵامدانەوەیا پرسیارێن قووڵ یێن ژیانێ و باوەڕێ")
        st.write("هەر پرسیارەک، گومانەک یان هەستەک د ناخێ تە دا هەبێت (وەک: بۆچی ئەز دژیم؟ خودێ کیە؟) لێرە بنڤیسە:")

        life_question = st.text_area("پرسیار یان بابەتی خۆ ل ڤێرە بنڤیسە:", placeholder="لێرە بنڤیسە...")

        if st.button("وەرگرتنا وەڵامەکا دلنشین"):
            if life_question:
                with st.spinner("خەریکی ڤەکۆلین و ئامادەکرنا وەڵامەکا پڕ لە ڕووناکیێیە..."):
                    try:
                        query_keyword = "islamic mosque spiritual light quran nature serene"
                        if "خودێ" in life_question or "خوا" in life_question:
                            query_keyword = "cosmos stars universe divine light spiritual"
                        elif "دل" in life_question or "ئارام" in life_question:
                            query_keyword = "peaceful nature sunset meditation calm water"

                        bg_image_url = f"https://source.unsplash.com/1600x900/?{query_keyword}"

                        st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background: linear-gradient(rgba(2, 44, 34, 0.88), rgba(2, 44, 34, 0.94)), url('{bg_image_url}');
                                background-size: cover;
                                background-position: center;
                                background-attachment: fixed;
                            }}
                            </style>
                            """,
                            unsafe_allow_html=True
                        )

                        prompt = f"""
                        تو زانایەکی دیندار، شارەزا و پڕ لە حیکمەت لە بواری قورئانی پیرۆز، ناسینی خودا (معرفة الله) و پەروەردەی ڕۆحی.
                        کەسێک ئەم پرسیارەی هەیە: '{life_question}'
                        تکایە وەڵامێکی زۆر ئارامبەخش، دڵنشین، لەسەر بنەمای قورئان، فەرموودە و گەورەیی خودای مەزن بە زمانی کوردی (بادینی / سۆرانى نزیک و ڕوون) پێشکەش بکە.
                        """
                        response = model.generate_content(prompt)
                        
                        st.markdown(
                            f"""
                            <div class="content-box">
                                <h3 style='color: #6ee7b7; margin-bottom: 15px;'>🌿 وەڵام و ڕێنماییا ڕۆحی:</h3>
                                <div style='line-height: 1.9; font-size: 16px; color: #ecfdf5;'>
                                    {response.text.replace(chr(10), '<br>')}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    except Exception as e:
                        st.error(f"⚠️ هەڵە ڕووی دا: {e}")
            else:
                st.warning("⚠️ تکایە پرسیارەک خۆ ل ڤێرە بنڤیسە.")

    # ٢. قورئانا پیرۆز و ئارامی
    elif selected_service == "قورئانا پیرۆز و ئارامی":
        st.markdown("### 📖 قورئانا پیرۆز و ئایەتێن ئارامبەخش")
        st.write("• **سورة البقرة:** (لا يكلف الله نفساً إلا وسعها)")
        st.write("• **سورة الرعد:** (ألا بذكر الله تطمئن القلوب)")
        st.write("• **سورة الشرح:** (فإن مع العسر يسراً، إن مع العسر يسراً)")
        st.markdown("<div class='content-box'>قورئان دل و دەروونی پاک دکەتەوە و هێمنیێ ددەتە مرۆڤی. هەمیشە بخوێنە بۆ ئەوەی لە خودای مەزن نزیکتر ببیتەوە.</div>", unsafe_allow_html=True)

    # ٣. زکر و یادی خودا
    elif selected_service == "زکر و یادی خودا":
        st.markdown("### ☀️ زکرێن ڕۆژانە بۆ نزیکبوونەڤە ژ خودایێ مەزن")
        st.markdown("1. **سُبْحَانَ اللَّهِ وَبِحَمْدِهِ** (١٠٠ جار)")
        st.markdown("2. **لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ**")
        st.markdown("3. **أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ**")

    # ٤. دوعا و مناجات
    elif selected_service == "دوعا و مناجات":
        st.markdown("### 🤲 دوعایێن دلسۆزانە و نزابوون")
        duaa_text = st.text_input("دوعایەکی خۆ ل ڤێرە بنووسە:")
        if st.button("ناردنا دوعای و وەرگرتنا ئارامیێ"):
            st.success("✅ (رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي) - خودایێ مەزن دوعایێن تە دبیستێت و ئارامیێ ددەتە تە.")

    # ٥. تێبینیێن ڕۆحی
    elif selected_service == "تێبینیێن ڕۆحی":
        st.markdown("### 📝 تێبینی و خاڵێن گرنگ بۆ ژیانا ڕۆحی")
        note = st.text_input("تێبینیا خۆ ل ڤێرە بنڤیسە:")
        if st.button("پاشەکەوتکرنا تێبینیێ"):
            if note:
                st.success(f'✅ تێبینیا تە هاتە وەرگرتن: "{note}"')

except Exception as e:
    st.error("⚠️ تکایە دڵنیابە کە کلیلێ سیستەمی لە بەشی Secretsـی Streamlit بە ڕێکی دانراوە.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #6ee7b7; font-size: 13px;'>پڕۆژەی بەرەو خودێ • دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
