import streamlit as st
import os

st.set_page_config(page_title="📘 استانداردهای ماشین‌آلات کشاورزی", layout="centered")
st.title("استانداردهای ماشین‌آلات کشاورزی 🚜")

st.write("یک ماشین انتخاب کن تا فایل‌های استانداردش رو ببینی.")

# لیست ماشین‌ها
machines = {
    "تراکتور": {
        "ایمنی": "https://example.com/tractor_safety.pdf",
        "موتور": "https://example.com/tractor_engine.pdf"
    },
    "کمباین": {
        "عملکرد": "https://example.com/combine_performance.pdf",
        "نگهداری": "https://example.com/combine_maintenance.pdf"
    }
}

# انتخاب ماشین
machine = st.selectbox("ماشین:", list(machines.keys()))

# انتخاب استاندارد
standard = st.selectbox("استاندارد:", list(machines[machine].keys()))

pdf_url = machines[machine][standard]

st.write("📄 فایل استاندارد انتخاب‌شده:")
st.markdown(f"[دانلود فایل PDF]({pdf_url})", unsafe_allow_html=True)

st.info("این نسخه‌ی نمایشی است. برای اضافه کردن فایل‌های واقعی، لینک‌های PDF خودتان را جایگزین کنید.")

