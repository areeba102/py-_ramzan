import streamlit as st
import requests
import datetime


st.set_page_config(page_title="Ramadan Companion 🌙", page_icon="🌙", layout="wide")

# Sidebar 
menu = st.sidebar.radio("📌 Select a Feature", ["Home 🏠", "Sehri & Iftar Timings ⏳", "Quran Tracker 📖", 
                                                "Salah Tracker 🕌", "Zakat Calculator 💰", "Dua Collection 🤲", 
                                                "40 Hadith 📜", "Tasbeeh Counter 📿"
                                                ])

# --- Home Section ---
if menu == "Home 🏠":
    st.title("🌙 Ramadan Companion: Your Digital Guide for Ramadan")
    st.write("""
    Welcome to **Ramadan Companion**! A complete guide to track your **Sehri & Iftar timings, Salah, Quran progress, Zakat, and more.**
    """)

    image_url = "https://marketplace.canva.com/EAFc8T7klhI/1/0/1600w/canva-green-modern-ramadan-mubarak-free-instagram-post-P0hRqLvxKA8.jpg"  # Use a reliable image hosting service
    st.image(image_url, caption="Ramadan Kareem", use_container_width=True)

    st.success("May Allah bless you this Ramadan! 🤲")

# --- Sehri & Iftar Timings ---
elif menu == "Sehri & Iftar Timings ⏳":
    st.header("⏳ Sehri & Iftar Timings")
    st.write("Write your city name to know its time.")

    city = st.text_input("Enter your city:", "Karachi")
    country =  st.text_input("Enter your country:", "pakistan")
    method = 1 

    if st.button("Get Timings"):
        try:
            api_url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}"
            response = requests.get(api_url).json()
            fajr = response['data']['timings']['Fajr']
            maghrib = response['data']['timings']['Maghrib']
            st.success(f"{city}:🌅 Sehri (Fajr) Time: {fajr} | 🌇 Iftar (Maghrib) Time: {maghrib}")
        except:
            st.error("⚠️ Unable to fetch timings. Please check the city name.")

# --- Quran Tracker ---
elif menu == "Quran Tracker 📖":
    st.header("📖 Quran Tracker")
    total_juz = 30
    completed_juz = st.number_input("Enter the number of Juz completed:", min_value=0, max_value=30, value=0)
    progress = (completed_juz / total_juz) * 100
    st.progress(progress / 100)
    st.write(f"📖 **Quran Completion Progress: {progress:.2f}%**")

# --- Salah Tracker ---
elif menu == "Salah Tracker 🕌":
    st.header("🕌 Salah Tracker")
    prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
    st.write("Mark the prayers you have performed today:")
    for prayer in prayers:
        st.checkbox(f"{prayer} Salah", key=prayer)
    st.success("Keep up with your prayers! May Allah accept them. 🤲")

# --- Zakat Calculator ---
elif menu == "Zakat Calculator 💰":
    st.header("💰 Zakat Calculator")
    gold_savings = st.number_input("Gold/Silver Value (in local currency):", min_value=0.0, value=0.0)
    cash_savings = st.number_input("Cash Savings:", min_value=0.0, value=0.0)
    other_assets = st.number_input("Other Assets:", min_value=0.0, value=0.0)
    total_wealth = gold_savings + cash_savings + other_assets
    zakat_due = 0.025 * total_wealth if total_wealth >= 595 else 0
    st.write(f"💰 **Total Wealth:** {total_wealth}")
    st.write(f"📌 **Zakat Due:** {zakat_due:.2f}")

# --- Dua Collection with User-Saved Duas ---
elif menu == "Dua Collection 🤲":
    st.header("🤲 Dua Collection (English + Urdu)")

    default_duas = [
        "اللَّهُمَّ إنِّي أَسْأَلُكَ الْجَنَّةَ وَأَعُوذُ بِكَ مِنَ النَّارِ \nO Allah! I ask You for Paradise and seek refuge from the Fire.",
        "اللَّهُمَّ اجعل لي في قَلْبِي نُورًا، وَفِي لِسَانِي نُورًا \nO Allah! Place light in my heart and light upon my tongue.",
        "اللَّهُمَّ اجْعَلْني مِنَ التَّوَّابِينَ، وَاجْعَلْنِي مِنَ الْمُتَطَهِّرِينَ \nO Allah! Make me among those who repent and those who purify themselves."
    ]

    if "saved_duas" not in st.session_state:
        st.session_state.saved_duas = []

    st.subheader("📜 Default Duas")
    for dua in default_duas:
        st.write(f"📖 {dua}")

    st.subheader("✍️ Add Your Own Dua")
    user_dua = st.text_area("Write your dua here:", placeholder="Type your dua and save...")

    if st.button("Save Dua"):
        if user_dua.strip():
            st.session_state.saved_duas.append(user_dua.strip())  
            st.success("✅ Your dua has been saved!")
        else:
            st.warning("⚠️ Please enter a valid dua before saving.")

    st.subheader("📜 Your Saved Duas")
    if st.session_state.saved_duas:
        for i, dua in enumerate(st.session_state.saved_duas):
            col1, col2 = st.columns([8, 1])
            with col1:
                st.write(f"📖 {dua}")
            with col2:
                if st.button("❌", key=f"delete_dua_{i}"):
                    st.session_state.saved_duas.pop(i)  
                    st.experimental_rerun() 
    else:
        st.write("❌ No saved duas yet. Start adding your own duas!")


# --- 40 Hadith ---
elif menu == "40 Hadith 📜":
    st.header("📜 40 Hadith Collection")
    hadiths = [
     "📖1. Actions are judged by intentions. (Bukhari & Muslim)",
     "  . اعمال کا دار و مدار نیتوں پر ہے۔ (بخاری و مسلم)",
    "📖2. The best among you are those who have the best manners and character. (Bukhari)","   . تم میں سب سے بہتر وہ ہے جس کا اخلاق سب سے اچھا ہے۔ (بخاری)",
    "📖3. None of you truly believes until he loves for his brother what he loves for himself. (Bukhari & Muslim)","   . تم میں سے کوئی مومن نہیں ہو سکتا جب تک کہ وہ اپنے بھائی کے لیے وہی پسند نہ کرے جو اپنے لیے پسند کرتا ہے۔ (بخاری و مسلم)",
    "📖4. Islam is built on five pillars. (Bukhari & Muslim)","   . اسلام کی بنیاد پانچ ستونوں پر ہے۔ (بخاری و مسلم)",
    "📖5. Modesty is part of faith. (Bukhari & Muslim)","   . حیاء ایمان کا حصہ ہے۔ (بخاری و مسلم)",
    "📖6. Whoever believes in Allah and the Last Day should speak good or remain silent. (Bukhari & Muslim)","   . جو شخص اللہ اور قیامت کے دن پر ایمان رکھتا ہے اسے چاہیے کہ بھلائی کی بات کرے یا خاموش رہے۔ (بخاری و مسلم)",
    "📖7. Allah does not look at your appearance, but at your hearts and deeds. (Muslim)","   . اللہ تمہاری شکل و صورت کو نہیں بلکہ تمہارے دلوں اور اعمال کو دیکھتا ہے۔ (مسلم)",
    "📖8. This religion is easy, and whoever makes it difficult will be overwhelmed. (Bukhari)","   . دین آسان ہے اور جو شخص اسے مشکل بنائے گا وہ مغلوب ہو جائے گا۔ (بخاری)",
    "📖9. Dua is the essence of worship. (Tirmidhi)","   . دعا عبادت کا مغز ہے۔ (ترمذی)",
    "📖10. A strong believer is better than a weak believer. (Muslim)","   . طاقتور مومن کمزور مومن سے بہتر اور اللہ کے نزدیک زیادہ محبوب ہے۔ (مسلم)",
    "📖11. Smiling is charity. (Tirmidhi)","   . اپنے بھائی کے چہرے پر مسکراہٹ ڈالنا صدقہ ہے۔ (ترمذی)",
    "📖12. Removing harm from the road is a charity. (Bukhari & Muslim)","   . راستے سے تکلیف دہ چیز ہٹانا صدقہ ہے۔ (بخاری و مسلم)",
    "📖13. Pray as you have seen me praying. (Bukhari)","   . نماز اس طرح پڑھو جیسے تم نے مجھے پڑھتے دیکھا ہے۔ (بخاری)",
    "📖14. The most beloved actions to Allah are those done consistently. (Bukhari & Muslim)","   . اللہ کے نزدیک سب سے محبوب عمل وہ ہے جو مستقل کیا جائے چاہے وہ تھوڑا ہی کیوں نہ ہو۔ (بخاری و مسلم)",
    "📖15. The closest a servant is to Allah is in prostration. (Muslim)","   . بندہ اپنے رب کے سب سے قریب سجدے کی حالت میں ہوتا ہے۔ (مسلم)",
    "📖16. Fast and you will be healthy. (Ibn Majah)","   . روزہ رکھو، صحت مند رہو گے۔ (ابن ماجہ)",
    "📖17. Whoever builds a mosque for Allah, Allah will build for him a house in Jannah. (Bukhari & Muslim)","   . جو شخص اللہ کے لیے مسجد بنائے گا، اللہ اس کے لیے جنت میں گھر بنائے گا۔ (بخاری و مسلم)",
    "📖18. Seeking knowledge is an obligation upon every Muslim. (Ibn Majah)","   . علم حاصل کرنا ہر مسلمان پر فرض ہے۔ (ابن ماجہ)",
    "📖19. Supplicate to Allah with certainty. (Tirmidhi)","   . اللہ سے دعا کرو اور یقین رکھو کہ وہ قبول کرے گا۔ (ترمذی)",
    "📖20. Whoever guides someone to good will have a reward similar to the one doing it. (Muslim)","   . جو شخص کسی نیکی کی راہ دکھائے گا، اسے اس کے برابر اجر ملے گا جو وہ نیکی کرے گا۔ (مسلم)",
    "📖21. Do not get angry. (Bukhari)","   . غصہ نہ کرو۔ (بخاری)",
    "📖22. The best among you are those who are best to their family. (Tirmidhi)","   . تم میں سب سے بہتر وہ ہے جو اپنے اہل خانہ کے لیے سب سے بہتر ہے۔ (ترمذی)",
    "📖23. It is not lawful to cut off relations with a fellow Muslim for more than three days. (Bukhari & Muslim)","   . کسی مسلمان کے لیے جائز نہیں کہ وہ اپنے بھائی سے تین دن سے زیادہ قطع تعلق کرے۔ (بخاری و مسلم)",
    "📖24. Giving charity does not decrease wealth. (Muslim)","   . صدقہ مال کو کم نہیں کرتا۔ (مسلم)",
    "📖25. Make things easy, do not make them difficult. (Bukhari & Muslim)","   . لوگوں کے لیے آسانی پیدا کرو، مشکلات نہ پیدا کرو۔ (بخاری و مسلم)",
    "📖26. A good word is charity. (Bukhari & Muslim)","   . اچھی بات کہنا صدقہ ہے۔ (بخاری و مسلم)",
    "📖27. He who does not show mercy will not be shown mercy. (Bukhari & Muslim)","   . جو رحم نہیں کرتا اس پر رحم نہیں کیا جائے گا۔ (بخاری و مسلم)",
    "📖28. Do not envy one another. (Muslim)","   . حسد نہ کرو۔ (مسلم)",
    "📖29. Allah helps those who help others. (Muslim)","   . اللہ اس بندے کی مدد کرتا ہے جو اپنے بھائی کی مدد کرتا ہے۔ (مسلم)",
    "📖30. The best of you is the one who learns the Quran and teaches it. (Bukhari)","   . تم میں سب سے بہتر وہ ہے جو قرآن سیکھے اور سکھائے۔ (بخاری)",
    "📖31. Paradise is surrounded by hardships. (Muslim)","   . جنت کو مشکلات سے گھیر دیا گیا ہے۔ (مسلم)",
    "📖32. Allah is more merciful than a mother to her child. (Bukhari & Muslim)","   . اللہ اپنے بندے پر اس کی ماں سے بھی زیادہ مہربان ہے۔ (بخاری و مسلم)",
    "📖33. Three things follow a dead person, but only one stays. (Bukhari & Muslim)","   . میت کے ساتھ تین چیزیں جاتی ہیں، مگر صرف ایک باقی رہتی ہے۔ (بخاری و مسلم)",
    "📖34. The best of people are those who bring most benefit to others. (Tabarani)","   . سب سے بہترین انسان وہ ہے جو دوسروں کو سب سے زیادہ فائدہ پہنچائے۔ (طبرانی)",
    "📖35. Allah loves those who repent. (Quran 2:222)","   . بے شک اللہ توبہ کرنے والوں سے محبت کرتا ہے۔ (قرآن 2:222)",
    "📖36. Sins are erased by good deeds. (Tirmidhi)","   . نیکیاں گناہوں کو مٹا دیتی ہیں۔ (ترمذی)",
    "📖37. Allah does not burden a soul beyond its capacity. (Quran 2:286)","   . اللہ کسی جان پر اس کی طاقت سے زیادہ بوجھ نہیں ڈالتا۔ (قرآن 2:286)",
    "📖38. The reward for patience is Paradise. (Quran 39:10)","   . صبر کا بدلہ جنت ہے۔ (قرآن 39:10)",
    "📖39. Every hardship comes with ease. (Quran 94:6)","  . ہر مشکل کے ساتھ آسانی ہے۔ (قرآن 94:6)",
    "📖40. Allah forgives all sins for those who sincerely repent. (Quran 39:53)","   . اللہ تمام گناہ معاف کر دیتا ہے جو سچے دل سے توبہ کریں۔ (قرآن 39:53)"
    ]
    for hadith in hadiths:
        st.write(f" {hadith}")

# --- Tasbeeh Counter ---
elif menu == "Tasbeeh Counter 📿":
    st.header("📿 Tasbeeh Counter")

    if "tasbeeh_list" not in st.session_state:
        st.session_state.tasbeeh_list = {}

    new_tasbeeh = st.text_input("Enter the name of the Tasbeeh you are reciting:", placeholder="SubhanAllah, Alhamdulillah, AllahuAkbar")

    if st.button("Add Tasbeeh"):
        if new_tasbeeh and new_tasbeeh not in st.session_state.tasbeeh_list:
            st.session_state.tasbeeh_list[new_tasbeeh] = 0
            st.success(f"Added '{new_tasbeeh}' to your Tasbeeh list!")

    for tasbeeh, count in st.session_state.tasbeeh_list.items():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(f"📿 **{tasbeeh}**: {count}")
        with col2:
            if st.button(f"➕ Add 1", key=f"add_{tasbeeh}"):
                st.session_state.tasbeeh_list[tasbeeh] += 1
        with col3:
            if st.button(f"🔄 Reset", key=f"reset_{tasbeeh}"):
                st.session_state.tasbeeh_list[tasbeeh] = 0
