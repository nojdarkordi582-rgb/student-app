import streamlit as st

# ڕێکخستنا سەرەکی پەڕەی
st.set_page_config(
    page_title="زکر", 
    page_icon="📿", 
    layout="centered"
)

# دیزاینی تایبەت و سیستەمی CSSـی جوان لەگەڵ ئەنیمیەیشنا گلوپا ئایەتێ
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #090d16 0%, #1e293b 100%);
        color: #ffffff;
    }
    @keyframes glowPulse {
        0% { color: #34d399; text-shadow: 0 0 5px #34d399, 0 0 10px #34d399; }
        50% { color: #ef4444; text-shadow: 0 0 20px #ef4444, 0 0 30px #ef4444; }
        100% { color: #34d399; text-shadow: 0 0 5px #34d399, 0 0 10px #34d399; }
    }
    .glow-verse {
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        direction: rtl;
        animation: glowPulse 3s infinite;
        margin-bottom: 15px;
        padding: 10px;
    }
    .zikr-card {
        background: rgba(15, 23, 42, 0.9);
        border-right: 4px solid #34d399;
        border-top: 1px solid rgba(52, 211, 153, 0.2);
        border-left: 1px solid rgba(52, 211, 153, 0.2);
        border-bottom: 1px solid rgba(52, 211, 153, 0.2);
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 15px;
        text-align: right;
        direction: rtl;
    }
    .developer-box {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 30px;
        padding: 10px;
        border-top: 1px dashed rgba(52, 211, 153, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# داتابەیسا دوعا، زکر و قورئانێ
database = {
    "🏠 زکرێن مال ڤەدکرن و تێدا چوونێ": [
        "بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى رَبِّنَا تَوَكَّلْنَا (دەما مروڤ دچیتە ژوورڤە بۆ مالێ).",
        "اللَّهُمَّ إِنِّى أَسْأَلُكَ خَيْرَ المَوْلِجِ وَخَيْرَ المَخْرَجِ، بِسْمِ اللَّهِ وَلَجْنَا وبِسْمِ اللَّهِ خَرَجْنَا.",
        "بِسْمِ اللَّهِ تَوَكَّلْتُ عَلَى اللَّهِ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ (دەما مروڤ ژ مال دکەتە دەر).",
        "أعوذ بكلمات الله التامات من شر ما خلق (بۆ پاراستنا مال و خێزانێ)."
    ],
    "📖 ئایەتێن قورئانا پیرۆز": [
        "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ (سورة الرعد: 28) - (ب یادا خودێ دل ئارام دبن).",
        "فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي وَلَا تَكْفُرُونِ (سورة البقرة: 152).",
        "رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي (سورة طه: 25-26)."
    ],
    "🌅 زکرێن بەیانی و ئێڤاری": [
        "أصبحنا وأصبح الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له.",
        "اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك النشور.",
        "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، عَدَدَ خَلْقِهِ، وَرِضَا نَفْسِهِ، وَزِنَةَ عَرْشِهِ، وَمِدَادَ كَلِمَاتِهِ."
    ],
    "🛡️ دوعایێن پاراستن و قەڵایا مەزن": [
        "بِسْمِ اللَّهِ الَّذِي لَا يَضُرِّمعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيعُ الْعَلِيمُ.",
        "أعوذ بكلمات الله التامات من شر ما خلق.",
        "حسبي الله لا إله إلا هو عليه توكلت وهو رب العرش العظيم."
    ],
    "💖 دوعایێن ئارامیا دل و ژیانێ": [
        "يا حي يا قيوم برحمتك أستغيث، أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عين.",
        "اللهم اني أسألك قلباً خاشعاً، ولساناً ذاكراً، وعلماً نافعاً، ورزقاً واسعاً."
    ]
}

# سیستەمێ گۆڕینا لاپەڕەکان (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None

# --- لاپەڕەی یەکەم: سەرەکی (لیستا بەشان) ---
if st.session_state.page == 'home':
    
    # 1. ئایەتا پیرۆز یا حەمدا خودێ ب شێوێ گلوپەکا هەڵبژارتی (کەسک و سور)
    st.markdown("""
        <div class="glow-verse">
            الحَمْدُ للهِ رَبِّ العَالَمِينَ • ٱللَّهُ لَا إِلَٰهَ إِلَّا هُوَ ٱلْحَيُّ ٱلْقَيُّومُ
        </div>
    """, unsafe_allow_html=True)
    
    # 2. ب خێرهاتنا بەکارهێنەری و ناڤێ بەرنامەی
    st.markdown("<h1 style='text-align: center; color: #34d399;'>📿 ئەپلیکەیشنا زکر</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 16px;'>بەخێر هاتن بۆ ژوورەوە! ڕێبەرێ ڕۆژانە یێ دوعا و زکرێن پاک.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<p style='text-align: right; direction: rtl; color: #34d399; font-weight: bold;'>بژاردەیەکێ هەڵبژێرە:</p>", unsafe_allow_html=True)
    
    for category in database.keys():
        if st.button(category, use_container_width=True):
            st.session_state.page = 'detail'
            st.session_state.selected_category = category
            st.rerun()
            
    # 3. ناڤێ دروستکەر و گەشەپێدەرێ ئەپلیکەیشنی
    st.markdown("""
        <div class="developer-box">
            دروستکەر و گەشەپێدەر: <b>نوژدار دژوار دۆسکی</b><br>
            پڕۆژەی زکر • Global Edition
        </div>
    """, unsafe_allow_html=True)

# --- لاپەڕەی دووەم: نیشاندانا زکرێن ناو بەشێ هەڵبژارتی ---
elif st.session_state.page == 'detail':
    cat = st.session_state.selected_category
    
    # دوگمەیا گەڕانەوە
    if st.button("⬅️ ڤەڕەقە بۆ پشکا سەرەکی", use_container_width=True):
        st.session_state.page = 'home'
        st.session_state.selected_category = None
        st.rerun()
        
    st.markdown(f"<h2 style='text-align: right; direction: rtl; color: #34d399; margin-top: 15px;'>{cat}</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='margin-bottom: 20px;'>", unsafe_allow_html=True)
    
    # نیشاندانا هەمی زکرێن ئەو بەشە به شێوەی کارت
    items = database[cat]
    for i, zikr in enumerate(items, 1):
        st.markdown(
            f"""
            <div class="zikr-card">
                <div style="font-size: 12px; color: #34d399; margin-bottom: 6px; font-weight: bold;">ژمارە ({i})</div>
                <div style="font-size: 16px; color: #ffffff; line-height: 1.7;">{zikr}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔙 ڤەڕەقە بو سەرەکی", use_container_width=True):
        st.session_state.page = 'home'
        st.session_state.selected_category = None
        st.rerun()
        
