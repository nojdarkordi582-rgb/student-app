import streamlit as st
import streamlit.components.v1 as components
import random

# ڕێکخستنی سەرەکی
st.set_page_config(page_title="بەرەو خودێ", page_icon="🤲", layout="centered")

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
st.markdown("<h3 style='text-align: right; direction: rtl; color: #ffffff;'>سلاڤ، نوژدار - سیستەمێ ئاگادارییێن شاشەیا قفل</h3>", unsafe_allow_html=True)

duaa_category = st.selectbox("جۆرێ زکر یان دوعایێ هەلبژێرە:", list(duaa_database.keys()))

if st.button("🔔 ناردنا دوعایێ بۆ سەر شاشەیا قفلا مۆبایلێ"):
    selected_duaa = random.choice(duaa_database[duaa_category])
    
    # نیشاندانی شێوازی پێشاندانی ناو ئەپەکە
    st.markdown(
        f"""
        <div style="background: rgba(20, 20, 20, 0.85); border: 1px solid rgba(255, 255, 255, 0.15); padding: 18px; border-radius: 20px; text-align: right; direction: rtl; margin-top: 15px;">
            <div style="font-size: 13px; color: #34d399; font-weight: bold; margin-bottom: 5px;">🤲 بەرەو خودێ • زکرێ نوو</div>
            <div style='font-size: 15px; color: #ffffff;'>{selected_duaa}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # کۆدی JavaScript بۆ پێدانی مۆڵەت و ناردنی ئاگاداری ڕاستەوخۆ بۆ شاشەی قفل
    js_code = f"""
    <script>
    if ("Notification" in window) {{
        if (Notification.permission === "granted") {{
            new Notification("🤲 بەرەو خودێ", {{
                body: "{selected_duaa}",
                icon: "https://cdn-icons-png.flaticon.com/512/2904/2904843.png"
            }});
        }} else if (Notification.permission !== "denied") {{
            Notification.requestPermission().then(function (permission) {{
                if (permission === "granted") {{
                    new Notification("🤲 بەرەو خودێ", {{
                        body: "{selected_duaa}",
                        icon: "https://cdn-icons-png.flaticon.com/512/2904/2904843.png"
                    }});
                }}
            }});
        }}
    }}
    </script>
    """
    components.html(js_code, height=0)

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray; font-size: 12px;'>پڕۆژەی بەرەو خودێ • نوژدار دژوار دۆسکی</div>", unsafe_allow_html=True)
