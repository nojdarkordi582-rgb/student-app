import streamlit as st
import random

# ڕێکخستنا سەرەکی
st.set_page_config(page_title="بەرەو خودێ", page_icon="🤲", layout="centered")

# گەنجینەیا دوعا و زکران
duaa_database = {
    "دوعایێن ئارامیا دلان و ڕووناکیا ناخی": [
        "أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ (ب یادا خودێ دل ئارام دبن).",
        "يا حي يا قيوم برحمتك أستغيث، أصلح لي شأني كله.",
        "اللهم اني أسألك قلباً خاشعاً وعلماً نافعاً.",
        "حسبنا الله ونعم الوكيل، نعم المولى ونعم النصير."
    ],
    "زکرێن پاراستنێ ل دەمێ قفلکرنا موبایلێ": [
        "بِسْمِ اللَّهِ الَّذِي لَا يَضُرِّمعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ.",
        "أعوذ بكلمات الله التامات من شر ما خلق.",
        "اللهم احفظني من بين يدي ومن خلفي.",
        "لا حول ولا قوة إلا بالله العلي العظيم."
    ],
    "دوعایێن رزق، برەکەت و ڤەکرنا دەرگەهان": [
        "اللهم إني أسألك رزقاً حلالاً طيباً مبارکاً فيه.",
        "رب اني لما أنزلت إلي من خير فقير.",
        "يا رزاق يا كریم، ارزقني من حيث لا احتسب."
    ],
    "ئایەتێن قورئانی یێن کورتی کاریگەر": [
        "فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي.",
        "وَمَنْ يَتَّقِ اللَّهَ يَجْعَلْ لَهُ مَخْرَجًا.",
        "رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي."
    ]
}

st.markdown("<h2 style='text-align: right; direction: rtl; color: #059669;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: right; direction: rtl; color: #ffffff;'>سلاڤ، نوژدار - نموونەیا شاشەیا قفل (Lock Screen Notification)</h3>", unsafe_allow_html=True)

duaa_category = st.selectbox("جۆرێ زکر یان دوعایێ هەلبژێرە:", list(duaa_database.keys()))

# دوگمەیا چێکرنێ ب لەزا مەزن
if st.button("✨ نیشادانا دوعایێ وەک اشعار لسەر شاشەیا قفل"):
    selected_duaa = random.choice(duaa_database[duaa_category])
    
    # دیزاینا اشعاری وەک وێنەیا تو نیشا من دای (تەقلیدکرنا اشعارا موبایلێ ل ناڤەڕاستا شاشەی)
    st.markdown(
        f"""
        <div style="background: rgba(20, 20, 20, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255, 255, 255, 0.15); padding: 18px 22px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.8); text-align: right; direction: rtl; margin-top: 25px;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                <div style="font-size: 13px; color: #34d399; font-weight: bold;">🤲 بەرەو خودێ • زکرێ نوو</div>
                <div style="font-size: 11px; color: #9ca3af;">نووکی</div>
            </div>
            <div style='line-height: 1.6; font-size: 15px; color: #ffffff; font-weight: 500;'>
                {selected_duaa}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray; font-size: 12px;'>پڕۆژەی بەرەو خودێ • نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
