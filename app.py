import streamlit as st

# ตั้งค่าหน้าตาของเว็บ
st.set_page_config(page_title="Animal Vocabulary Quiz", page_icon="🐾")

st.title("🎮 GAME: ENGLISH VOCABULARY QUIZ (A-J)")
st.write("ทายคำศัพท์ภาษาอังกฤษจากคำใบ้ด้านล่าง แล้วกดปุ่มส่งคำตอบเพื่อดูคะแนนได้เลย!")

quiz_data = [
    ("ข้อที่ 1 (A): 'ฉันอยู่ในน้ำ ปากยาว ฟันแหลม อย่าเหมารวมฉันกับจระเข้!'", "alligator", "อัลลิเกเตอร์ / จระเข้ตีนเป็ด"),
    ("ข้อที่ 2 (B): 'เคยเป็นหนอน โตขึ้นมีปีกสวย บินดูดน้ำหวานจากดอกไม้'", "butterfly", "ผีเสื้อ"),
    ("ข้อที่ 3 (C): 'ตัวสีน้ำตาล หนวดยาว ชอบวิ่งในบ้าน พอเปิดไฟก็วิ่งหนี!'", "cockroach", "แมลงสาบ"),
    ("ข้อที่ 4 (D): 'บนหัวมีเขาสวยงาม เป็นตัวเอกในเรื่องแบมบี้'", "deer", "กวาง"),
    ("ข้อที่ 5 (E): 'นกตัวใหญ่ บินอยู่บนฟ้าสูงๆ ระวังจะโฉบเอาจับกิน!'", "eagle", "นกอินทรี"),
    ("ข้อที่ 6 (F): 'หน้าคล้ายหมา หางฟูสีส้ม ใครๆ ก็บอกว่าฉันเจ้าเล่ห์'", "fox", "หมาจิ้งจอก"),
    ("ข้อที่ 7 (G): 'ตัวใหญ่ คอยาว ร้องก๊าบๆ ถ้าเรียกเป็ดจะวิ่งไล่จิก!'", "goose", "ห่าน"),
    ("ข้อที่ 8 (H): 'ฉันคือหมูเด้ง!! ตัวใหญ่ ปากกว้าง ชอบอยู่ในน้ำ'", "hippopotamus", "ฮิปโปโปเตมัส"),
    ("ข้อที่ 9 (I): 'สัตว์เลื้อยคลาน คล้ายกิ้งก่ายักษ์ มีหนามบนหลัง'", "iguana", "อีกัวน่า"),
    ("ข้อที่ 10 (J): 'อยู่ในทะเล ตัวใสๆ นิ่มๆ มีหนวดห้อยลงมาเยอะๆ'", "jellyfish", "แมงกะพรุน")
]

# ช่องกรอกคำตอบ
user_answers = []
for i, (q_text, _, _) in enumerate(quiz_data):
    ans = st.text_input(q_text, key=f"q_{i}", placeholder="พิมพ์คำตอบภาษาอังกฤษที่นี่...")
    user_answers.append(ans)

# ปุ่มส่งคำตอบ
if st.button("ส่งคำตอบและดูผลคะแนน", type="primary"):
    score = 0
    results = []
    
    for i, (q_text, correct_word, thai_meaning) in enumerate(quiz_data):
        ans = user_answers[i].lower().strip() if user_answers[i] else ""
        is_correct = ans == correct_word
        
        if is_correct:
            score += 1
            status = "✅ ถูกต้อง"
        else:
            status = "❌ ผิด"
            
        results.append(f"ข้อ {i+1}: คุณตอบ '{ans}' | {status} (เฉลย: {correct_word} = {thai_meaning})")
    
    st.divider()
    st.header(f"🏆 คะแนนรวมทั้งหมดของคุณ: {score} / 10 คะแนน")
    for res in results:
        st.write(res)
