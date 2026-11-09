import streamlit as st
import google.generativeai as genai

# رێکخستنا لاپەڕەی بۆ RTL و دیزاینی فول مۆدێرن و سەرنجڕاکێش
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

    .content-box {
        background: rgba(2, 44, 34, 0.88);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(74, 222, 128, 0.4);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
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

    .stTextInput textarea, .stTextArea textarea {
        background-color: rgba(6, 78, 59, 0.6) !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
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
        <div style="font-size: 14px; color: #a7f3d0;">گەنجینەیا مەزنیا **بەرەو خودێ** - پڕ ب ملیۆنان زکر، دوعا، مناجات و وەڵامێن ڕۆحی</div>
    </div>
    """,
    unsafe_allow_html=True
)

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # دروستکرنا پشکێن سەرەکی یێن ڤێ گەنجینەیا مەزن
    st.markdown("### 🗂️ گەنجینەیا ب ملیۆنان زکر و دوعا")

    col1, col2, col3 = st.columns(3)

    with col1:
        btn_million_duaa = st.button("🤲 ب ملیۆنان دوعا و مناجات")
    with col2:
        btn_million_zekr = st.button("☀️ زکرێن سبەهی و ئێڤاری")
    with col3:
        btn_deep_q = st.button("🌌 پرسیارێن قووڵ و خوداناسی")

    col4, col5 = st.columns(2)
    with col4:
        btn_quran_heal = st.button("📖 ئایەتێن شفاکەر و ئارامیێ")
    with col5:
        btn_custom = st.button("🔍 گەڕینا بێ سنور (زکر یان دوعا)")

    st.markdown("---")

    # دیارکرنا پشکا هاتھیە هەلبژارتن
    selected_service = "ب ملیۆنان دوعا و مناجات"
    if btn_million_duaa:
        selected_service = "ب ملیۆنان دوعا و مناجات"
    elif btn_million_zekr:
        selected_service = "زکرێن سبەهی و ئێڤاری"
    elif btn_deep_q:
        selected_service = "پرسیارێن قووڵ و خوداناسی"
    elif btn_quran_heal:
        selected_service = "ئایەتێن شفاکەر و ئارامیێ"
    elif btn_custom:
        selected_service = "گەڕینا بێ سنور (زکر یان دوعا)"

    # ١. ب ملیۆنان دوعا و مناجات
    if selected_service == "ب ملیۆنان دوعا و مناجات":
        st.markdown("### 🤲 گەنجینەیا ب ملیۆنان دوعایێن جۆراوجۆر")
        st.write("ل ڤێرە، ب ڕێکا گەنجینەیا زیرەک، تو دشکەی داخوازا هەمی جۆرێن دوعایان بکەی (دوعایێن ژیانێ، رزقی، پاراستنێ، توبێ، لێخۆشبوونێ و ...):")

        duaa_type = st.selectbox("تکایە جۆرێ دوعایێ هەلبژێرە:", [
            "دوعایێن ژیانۆکی و ئارامیا دەروونی (بێ سنور)",
            "دوعایێن رزق، برەکەت و ڤەکرنا دەرگەهان",
            "دوعایێن پاراستنێ ژ هەمی نەخۆشی و کێشەکان",
            "دوعایێن لێخۆشبوون و توبەکردنا راستەقینە",
            "مناجاتێن شەڤێ و نزابوون ژ خودایێ مەزن"
        ])

        if st.button("دەرئێخستنا دوعا و مناجاتان"):
            with st.spinner("خەریکی ئامادەکرنا دوعا و مناجاتێن پڕ ڕووناکیێیە..."):
                try:
                    bg_image_url = "https://source.unsplash.com/1600x900/?islamic,duaa,mosque,spiritual,pray"
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
                    تو زانایەکێ دیندار و شارەزای لە بواری دوعا، مناجات و گەنجینەیا فەرموودە و قورئانێ.
                    بۆ بابەتی ({duaa_type})، تکایە کۆمەلەک ژ جوانترین، مەزنترین و کاریگەرترین دوعا و مناجاتێن ئاینی ب زمانێ کوردی (بادینی و سۆرانی) ب شێوازەکێ زۆر پڕ هەست و ئارامبەخش بینە دەر، گۆیا مروڤ د گەنجینەیەکێ دا گەڕابیت.
                    """
                    response = model.generate_content(prompt)
                    
                    st.markdown(
                        f"""
                        <div class="content-box">
                            <h3 style='color: #6ee7b7; margin-bottom: 15px;'>🤲 گەنجینەیا دوعا و مناجاتان:</h3>
                            <div style='line-height: 1.9; font-size: 16px; color: #ecfdf5;'>
                                {response.text.replace(chr(10), '<br>')}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                except Exception as e:
                    st.error(f"⚠️ هەڵە ڕووی دا: {e}")

    # ٢. زکرێن سبەهی و ئێڤاری
    elif selected_service == "زکرێن سبەهی و ئێڤاری":
        st.markdown("### ☀️ زکرێن سبەهی و ئێڤاری (ب ملیۆنان جار خێر و پاداشت)")
        st.write("ل ڤێرە هەمی زکرێن سەرەکی و سوننەت یێن ڕۆژانە ب هزرا خودا تێدان:")
        st.markdown("• **سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، سُبْحَانَ اللَّهِ العَظِيمِ** (ئەڤە ب زمانێ مروڤی سڤکە، ل تەرازیێ گەلەک گرانە).")
        st.markdown("• **لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ** (گەنجەکە ژ گەنجینەیێن بهەشتێ).")
        st.markdown("• **يَا حَيُّ يَا قَيُّومُ بِرَحْمَتِكَ أَسْتَغِيثُ** (دوعایا ئارامیا ئێکجار مەزن).")
        st.markdown("<div class='content-box'>د بوارێ زکران دا، گەنجینەیا تە بێ سنورە؛ هەمیشە زمانێ خۆ ب یادی خودا بڕازێنە.</div>", unsafe_allow_html=True)

    # ٣. پرسیارێن قووڵ و خوداناسی
    elif selected_service == "پرسیارێن قووڵ و خوداناسی":
        st.markdown("### 🌌 پرسیارێن قووڵ، خوداناسی و ژیانێ")
        life_q = st.text_input("هەر پرسیارەکا قووڵ د مێشکێ تە دا هەیە بنڤیسە (وەک: خودێ کیە؟ بۆچی ئەز هەم؟):")
        if st.button("وەرگرتنا وەڵامەکا ڕۆحی"):
            if life_q:
                with st.spinner("خەریکی شیکارکرنا پرسیارێیە..."):
                    prompt = f"تکایە وەڵامەکا پڕ زانست و ئارامی لەسەر ئەم پرسیارە بدە ب زمانێ کوردی: {life_q}"
                    res = model.generate_content(prompt)
                    st.markdown(f"<div class='content-box'>{res.text}</div>", unsafe_allow_html=True)

    # ٤. ئایەتێن شفاکەر و ئارامیێ
    elif selected_service == "ئایەتێن شفاکەر و ئارامیێ":
        st.markdown("### 📖 ئایەتێن شفاکەر و ئارامیا دلان")
        st.write("• **وَنُنَزِّلُ مِنَ الْقُرْآنِ مَا هُوَ شِفَاءٌ وَرَحْمَةٌ لِلْمُؤْمِنِينَ**")
        st.write("• **أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ**")
        st.markdown("<div class='content-box'>قورئان شفایە بۆ هەمی نەخۆشیێن دەروونی و جەستەیی.</div>", unsafe_allow_html=True)

    # ٥. گەڕینا بێ سنور (زکر یان دوعا)
    elif selected_service == "گەڕینا بێ سنور (زکر یان دوعا)":
        st.markdown("### 🔍 گەڕینا بێ سنور د ناڤ ملیۆنان بابەتیێن ئاینی دا")
        search_term = st.text_input("بەرەڤ کیش جۆرە زکر، دوعا یان بابەتی دچى؟ (بۆ نموونە: دوعا بۆ باب و دایکی، زکرێ پاراستنێ):")
        
        if st.button("ئەنجامدانا گەڕینێ"):
            if search_term:
                with st.spinner("ل گەنجینەیا ب ملیۆنان زکر و دوعایان دگەڕێت..."):
                    try:
                        bg_image_url = "https://source.unsplash.com/1600x900/?quran,nature,sky,light,galaxy"
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
                        تو گەنجینەدارەکێ زانا و گەورەی لە هەمی زکر، دوعا، فەرموودە و ئایەتێن پیرۆز.
                        کەسەکی دەیەوێت ئەم بابەتە بدۆزێتەوە یان بخوێنێت: '{search_term}'
                        تکایە هەمی زکر، دوعا، ئایەت و مناجاتێن پەیوەندیدار ب ڤی بابەتی ڤە ب شێوازەکێ زۆر پڕ، فراوان و ب ملیۆنان خێر و پاداشت ب زمانێ کوردی (بادینی / سۆرانی) بۆ دیار بکە.
                        """
                        response = model.generate_content(prompt)
                        st.markdown(
                            f"""
                            <div class="content-box">
                                <h3 style='color: #6ee7b7; margin-bottom: 15px;'>✨ ئەنجامێن گەڕینا گەنجینەیێ:</h3>
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
                st.warning("⚠️ تکایە تشتەکی بنڤیسە دا تێدا بگەرێین.")

except Exception as e:
    st.error("⚠️ تکایە دڵنیابە کە کلیلێ سیستەمی لە بەشی Secretsـی Streamlit بە ڕێکی دانراوە.")

st.markdown("---")
st.markdown("<div style='text-align: center; color: #6ee7b7; font-size: 13px;'>گەنجینەیا بەرەو خودێ (ب ملیۆنان زکر و دوعا) • دروستکەر و گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
    
