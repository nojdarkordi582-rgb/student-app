import streamlit as st
import random

# ڕێکخستنا سەرەکی پەڕەی
st.set_page_config(
    page_title="پەناگەها دەروونی و ڤەحەواندنا ڕۆحێ", 
    page_icon="🌿", 
    layout="centered"
)

# دیزاینا تایبەت (Glassmorphism & Calm Dark Theme)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #091e18 0%, #0f172a 100%);
        color: #ffffff;
    }
    .soul-card {
        background: rgba(15, 23, 42, 0.85);
        border: 2px solid rgba(52, 211, 153, 0.4);
        padding: 22px;
        border-radius: 18px;
        text-align: right;
        direction: rtl;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .stTextArea textarea {
        background-color: rgba(30, 41, 59, 0.8) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

# سەرۆکی پڕۆژەی
st.markdown("<h1 style='text-align: center; color: #34d399;'>🌿 پەناگەها دەروونی و ڤەحەواندنا ڕۆحێ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 15px;'>هەست و فشارێن خۆ ل خوارێ بنڤیسە، تاوەکو ڕێبەرێ ڕۆحانی دوعا و ئایەتێن گونجای بۆ تە بینیت.</p>", unsafe_allow_html=True)
st.markdown("---")

# داتابەیسا دەروونی و چاڕەسەریێن ئیسلامی
solutions_db = {
    "خەمگینی و دلتەنگی": {
        "verse": "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ (سورة الرعد: 28)",
        "duaa": "يا حي يا قيوم برحمتك أستغيث، أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عين.",
        "advice": "دلێ تە گەلەک مەزنە و ژ بەر کو مروڤ ل جیهانەکا تژی تاقیکردن ژیان دکەت، ئاساییە خەمگین ببی. بەلێ بیرا خۆ بینە کو خودایێ مەزن هەر دەم ل گەل تە یە."
    },
    "تەمبەلیا عیبادەتێ": {
        "verse": "فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي وَلَا تَكْفُرُونِ (سورة البقرة: 152)",
        "duaa": "اللَّهُمَّ أَعِنِّى عَلَى ذِكْرِكَ، وَشُكْرِكَ، وَحُسْنِ عِبَادَتِكَ.",
        "advice": "ڕۆحا مروڤی گەلەک جار پێدڤی ب پشکەکا بچووک یا هاندەر هەیە. هەر دەست پێکرنەکا بچووک، دەرگەهەکێ مەزن یێ ڤەحەواندنێ بۆ تە ڤەدکەت."
    },
    "ترس و نیگەرانی": {
        "verse": "حَسْبُنَا اللَّهُ وَنِعْمَ الْوَكِيلُ (سورة آل عمران: 173)",
        "duaa": "اللَّهُمَّ إِنِّى أَعُوذُ بِكَ مِنَ الْهَمِّ وَالحَزَنِ، وَالْعَجْزِ وَالْكَسَلِ.",
        "advice": "ئەو تشتێ تو ژێ دترسی، هشکەکێ خودایی هەی. پشتڕاست بە کو تو د پاراستنا خودایێ مهزن دا مەدی."
    }
}

# خانەیا نڤیسینا هەستان ژ لایێ بەکارهێنەری ڤە
user_feeling = st.text_area("🧠 ئەڤڕۆ هەست بە چی دکەی؟ (بۆ نموونە: ئەز خەمگینم، یان ترسەکا من هەی...)", placeholder="لێرە هەستێن خۆ بنڤیسە...")

if st.button("✨ چارەسەریا دەروونی و ڕۆحانی ببينە", use_container_width=True):
    if user_feeling.strip() == "":
        st.warning("تکایە دەستپێکێ هەستێ خۆ ل خانەیێ بنڤیسە!")
    else:
        # هەلبژاردنا ئێک ژ چارەسەریان ب شێوەیەکێ زیرەک یان هەڕەمەکی ل گۆرەی تێکستی
        key_chosen = random.choice(list(solutions_db.keys()))
        sol = solutions_db[key_chosen]
        
        st.markdown(
            f"""
            <div class="soul-card">
                <div style="font-size: 14px; color: #34d399; font-weight: bold; margin-bottom: 10px;">💡 پەیاما تایبەت بۆ حالەتێ تە ({key_chosen}):</div>
                <p style="font-size: 16px; color: #ffffff; line-height: 1.7; margin-bottom: 12px;"><b>ئایەت:</b> {sol['verse']}</p>
                <p style="font-size: 16px; color: #34d399; line-height: 1.7; margin-bottom: 12px;"><b>دوعا:</b> {sol['duaa']}</p>
                <p style="font-size: 15px; color: #94a3b8; line-height: 1.6; border-top: 1px dashed rgba(255,255,255,0.2); padding-top: 10px;"><b>ڕێنماییا دەروونی:</b> {sol['advice']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #64748b; font-size: 12px;'>پڕۆژەی پەناگەها دەروونی • گەشەپێدەر: نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
