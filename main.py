import streamlit as st
import os
from few_shots import FewShotPosts
from post_generator import generate_post

# ---------- Page Config ----------
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="📝",
    layout="centered",
)

# ---------- Sidebar ----------
with st.sidebar:
    st.title("🧠 AI-Powered Post Generator")
    st.markdown(
        """
        🚀 Generate engaging LinkedIn posts  
        📌 Choose your topic, tone, and length  
        🤖 Powered by LLMs (Groq, OpenAI, etc.)
        ---
        **Built by Ali**  
        [GitHub Repo](https://github.com/Muhammad-Ali-Asad/LinkedIn_post_Generator)
        """
    )

# ---------- Main Title ----------
st.markdown("<h2 style='text-align: center;'>🚀 LinkedIn Post Generator</h2>", unsafe_allow_html=True)
st.markdown("### ✍️ Select your preferences")

# ---------- Dropdowns ----------
fs = FewShotPosts()
tags = fs.get_tags()

col1, col2, col3 = st.columns(3)

with col1:
    selected_tag = st.selectbox("🎯 Topic", options=tags)

with col2:
    selected_length = st.selectbox("📏 Length", options=["Short", "Medium", "Long"])

with col3:
    selected_language = st.selectbox("🌐 Language", options=["English", "Urdulish"])

# ---------- Generate Button ----------
generate_btn = st.button("✨ Generate Post")

if generate_btn:
    with st.spinner("Generating post..."):
        post = generate_post(selected_length, selected_language, selected_tag)

    st.markdown("### ✅ Your AI-Generated Post")

    # ---------- Display Output without scrollbars ----------
    st.markdown(
        f"""
        <div style='padding: 5px 20px; border-radius: 8px; font-size: 16px; line-height: 1.6; white-space: pre-wrap;'>
            {post}
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- Footer ----------
st.markdown("---")
