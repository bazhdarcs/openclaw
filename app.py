import os
import streamlit as st
import subprocess

# دروستکردنی نیشاندەرێکی سادە بۆ ئەوەی سێرڤەرەکە نەکوژێتەوە
st.title("OpenClaw AI Worker 🤖")
st.success("سکرتێرەکەت ئێستا ئۆنلاینە و ئامادەیە بۆ کارکردن!")
st.info("تێبینی: هەر فەرمانێکت هەیە لە تێلیگرامەوە بۆی بنێرە.")

# کارپێکردنی ئۆپن کڵاو (وەک مۆدیوڵ)
try:
    # ئەمە فەرمانی سەرەکییە بۆ هەڵکردنی بۆتەکە
    subprocess.Popen(["python", "-m", "openclaw"])
except Exception as e:
    st.error(f"هەڵەیەک ڕوویدا: {e}")
