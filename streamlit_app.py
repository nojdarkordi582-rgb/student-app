import streamlit as st
import random

# 1. ڕێکخستنا سەرەکی پەڕەی
st.set_page_config(
    page_title="پەناگەها دەروونی و ڤەحەواندنا ڕۆحێ", 
    page_icon="🌿", 
    layout="centered"
)

# 2. دیزاینا تایبەت ب ڕەنگێن ئارامکەر (Dark Glassmorphism)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #091e18 0%, #0f172a 100%);
        color: #ffffff;
    }
    .soul-card {
        background: rgba(15, 23, 42, 0.85);
        border-right: 5px solid #34d399;
        border-top: 1px solid rgba(52, 211, 153, 0.3);
        border-left: 1px solid rgba(52, 211, 153, 0.3);
        border-bottom: 1px solid rgba(52, 211, 153, 0.3);
        padding: 22px;
        border-radius: 18px;
        text-align: right;
        direction: rtl;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .stSelectbox label, .stRadio label {
        color: #34d399 !important;
        font-weight: bold;
        direction: rtl;
    }
    .stTextArea textarea {
        background-color: rgba(30, 41, 59, 0.8) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

# 3. سەرۆکی پڕۆژەی
st.markdown("<h1 style='text-align: center; color: #34d399;'>🌿 پەناگەها دەروونی و ڤەحەواندنا ڕۆحێ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 15px;'>هاوڕێیەکی هۆشمەند بۆ ئارامکرنا دەروون و ڕۆحا تە ب قورئان و زکران.</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. داتابەیسا دەروونی و چاڕەسەریێن ئیسلامی
solutions_db = {
    "😔 خەمگینی و دڵتەنگی": {
        "verse": "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ (سورة الرعد: 28)",
        "duaa": "يا حي يا قيوم برحمتك أستغيث، أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عين.",
        "advice": "دلێ تە گەلەک مەزنە. ئاساییە هەست ب خەمگینیێ بکەی چونکی مروڤین، بەلێ بیرا خۆ بینە کو ژ دوای هەر تەنگانەیەکێ سەربەستییەک و ئارامییەک یا هەی."
    },
    "😴 تەمبەلیا عیبادەتێ و سستی": {
        "verse": "فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي وَلَا تَكْفُرُونِ (سورة البقرة: 152)",
        "duaa": "اللَّهُمَّ أَعِنِّى عَلَى ذِكْرِكَ، وَشُكْرِكَ، وَحُسْنِ عِبَادَتِكَ.",
        "advice": "هەر هەنگاوەکا بچووک دەستپێکەکا مەزنە. تێبکۆشە تا تەنها زکرەکێ بچووک بکەی، دەستبەجێ ڕۆحا تە دێ سووک بێت."
    },
    "😨 ترس و نیگەرانی ژ پاشەڕۆژێ": {
        "verse": "حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ (سورة آل عمران: 173)",
        "duaa": "اللَّهُمَّ إِنِّى أَعُوذُ بِكَ مِنَ الْهَمِّ وَالحَزَنِ، وَالْعَجْزِ وَالْكَسَلِ.",
        "advice": "پاشەڕۆژ ل ژێر دەستێ ڕەحمان و ڕەحیم دایە. ئەو تشتێ تو ژێ دترسی، بکە سپۆرت و توەکول ل سەر خودێ."
    },
    "🥀 بێ هێڤییبوون و ماندووبوونا دەروونی": {
        "verse": "لَا تَقْنَطُوا مِن رَّحْمَةِ اللَّهِ (سورة الزمر: 53)",
        "duaa": "رَبِّ إِنِّي لِمَا أَنزلتَ إِلَيَّ مِنْ خَيْرٍ فَقِيرٌ.",
        "advice": "دەرگەهێ ڕەحمەتا خودێ هەردەم ڤەکرییە. ماندووبوونا تە بەڵگەیە کە تو هەوڵ دەدەی، خودایێ مەزن تە پشتگوێ ناخات."
    }
}

# 5. هەڵبژاردنی هەست ب شێوەی خێرا
st.markdown("<p style='text-align: right; direction: rtl; color: #34d399; font-weight: bold;'>ئێستا هەست بە چی دکەی؟ (ئێک ژ ڤان هەڵبژێرە):</p>", unsafe_allow_html=True)
selected_mood = st.selectbox("", list(solutions_db.keys()))

user_custom_text = st.text_area("✍️ یان دەتوانیت لێرە روونکردنەوا پتر بنڤیسی (ئارەزوومەندانه):", placeholder="بۆ نموونە: ئەڤڕۆ ئەز زۆر ماندووم...")

if st.button("✨ چارەسەریا دەروونی و ڕۆحانی دەرخە", use_container_width=True):
    sol = solutions_db[selected_mood]
    
    st.markdown(
        f"""
        <div class="soul-card">
            <div style="font-size: 15px; color: #34d399; font-weight: bold; margin-bottom: 12px;">💡 دەرمانا ڕۆحانی بۆ حالەتێ: {selected_mood}</div>
            <p style="font-size: 17px; color: #ffffff; line-height: 1.8; margin-bottom: 12px;">📖 <b>ئایەت:</b> {sol['verse']}</p>
            <p style="font-size: 17px; color: #34d399; line-height: 1.8; margin-bottom: 12px;">🤲 <b>دوعا:</b> {sol['duaa']}</p>
            <p style="font-size: 15px; color: #cbd5e1; line-height: 1.7; border-top: 1px dashed rgba(255,255,255,0.2); padding-top: 12px;">🧠 <b>ئامۆژگاریا دەروونی:</b> {sol['advice']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #64748b; font-size: 12px;'>پڕۆژەی پەناگەها دەروونی • گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
