import streamlit as st
import random

# ڕێکخستنا سەرەکی پەڕەی جیهانی
st.set_page_config(
    page_title="بەرەو خودێ | Bero Xode", 
    page_icon="🤲", 
    layout="centered"
)

# دیزاینی تایبەت و سیستەمی CSSـی جیهانی (Glassmorphism)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
    }
    .stSelectbox label {
        color: #34d399 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# هەڵبژاردنی زمان (Multi-language Support)
lang = st.sidebar.selectbox("🌐 زمان / Language / اللغة", ["کوردی (بادینی)", "English", "العربية"])

# ناوەرۆک و داتابەیس بە پێی زمان
if lang == "کوردی (بادینی)":
    title_text = "بەرەو خودێ"
    subtitle_text = "ڕێبەرێ ڕۆژانە یێ دوعا و زکران"
    select_label = "جۆرێ زکر یان دوعایێ هەلبژێرە:"
    btn_text = "✨ نیشادانا دوعایێ"
    db = {
        "دوعایێن ئارامیا دلان": [
            "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ (ب یادا خودێ دل ئارام دبن).",
            "يا حي يا قيوم برحمتك أستغيث، أصلح لي شأني كله.",
            "اللهم اني أسألك قلباً خاشعاً وعلماً نافعاً."
        ],
        "زکرێن پاراستنێ": [
            "بِسْمِ اللَّهِ الَّذِي لَا يَضُرِّمعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ.",
            "أعوذ بكلمات الله التامات من شر ما خلق.",
            "اللهم احفظني من بين يدي ومن خلفي وعن يميني وعن شمالي."
        ],
        "دوعایێن رزق و برەکەتێ": [
            "اللهم إني أسألك رزقاً حلالاً طيباً مبارکاً فيه.",
            "رب اني لما أنزلت إلي من خير فقير.",
            "يا رزاق يا كریم، ارزقني من حيث لا احتسب."
        ]
    }
elif lang == "English":
    title_text = "Bero Xode"
    subtitle_text = "Daily Islamic Duas & Zikr Guide"
    select_label = "Select category:"
    btn_text = "✨ Show Dua"
    db = {
        "Peace of Heart": [
            "Verily, in the remembrance of Allah do hearts find rest.",
            "O Ever-Living, O Self-Existing, by Your mercy I seek help.",
        ],
        "Protection": [
            "In the name of Allah with Whose name nothing is harmed.",
            "I seek refuge in the Perfect Words of Allah.",
        ]
    }
else:
    title_text = "نحو الله"
    subtitle_text = "دليل الأدعية والأذكار اليومية"
    select_label = "اختر التصنيف:"
    btn_text = "✨ إظهار الدعاء"
    db = {
        "أدعية الطمأنينة": [
            "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ.",
            "يا حي يا قيوم برحمتك أستغيث."
        ]
    }

# نیشاندانا سەرەکی
st.markdown(f"<h1 style='text-align: center; color: #34d399;'>🤲 {title_text}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #94a3b8; font-size: 16px;'>{subtitle_text}</p>", unsafe_allow_html=True)
st.markdown("---")

# بەشی بژاردە و نیشاندان
category = st.selectbox(select_label, list(db.keys()))

if st.button(btn_text, use_container_width=True):
    chosen = random.choice(db[category])
    st.markdown(
        f"""
        <div style="background: rgba(15, 23, 42, 0.8); border: 2px solid #34d399; padding: 20px; border-radius: 16px; text-align: center; margin-top: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.3);">
            <p style='font-size: 18px; color: #ffffff; line-height: 1.8;'>{chosen}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 12px;'>Developed by Nozhdar Dzhwar Doski • Global Edition</p>", unsafe_allow_html=True)
