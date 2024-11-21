# app.py

import streamlit as st
from streamlit import session_state
import time
import base64
import os
from vectors import EmbeddingsManager  # Import the EmbeddingsManager class
from chatbot import ChatbotManager     # Import the ChatbotManager class

# Function to display the PDF of a given file
def displayPDF(file):
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Initialize session_state variables
if 'temp_pdf_path' not in st.session_state:
    st.session_state['temp_pdf_path'] = None

if 'chatbot_manager' not in st.session_state:
    st.session_state['chatbot_manager'] = None

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Page configuration
st.set_page_config(
    page_title="Agent:DOC",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar
with st.sidebar:
    st.image("logo.png", use_column_width=True)
    st.markdown("## 📚 Your Personal Document Assistant")
    menu = st.radio(
        "Navigate", 
        ["🏠 Home", "🤖 Chatbot", "📧 Contact"],
        index=0,
        key="sidebar_menu",
    )
    st.markdown("---")
    st.markdown("**🛠 Built with:**\n- Llama 3.2\n- BGE Embeddings\n- Qdrant")

# Home Page
if menu == "🏠 Home":
    st.title("📄 Welcome to Document Buddy App")
    st.markdown("""
    **Your AI-powered assistant for managing and interacting with documents. 🚀**

    ### Features:
    - **Upload Documents:** Quickly upload your PDFs.
    - **Generate Insights:** Summarize and analyze your content.
    - **AI-Powered Chatbot:** Ask questions directly from your documents.

    Start by uploading a document or head to the chatbot to interact with your content!
    """)
    st.image("home_banner.png", use_column_width=True)

# Chatbot Page
elif menu == "🤖 Chatbot":
    st.title("🤖 Chat with Your Document")
    st.markdown("---")
    col1, col2, col3 = st.columns([1.2, 1, 1.5], gap="medium")

    # Column 1: File Uploader
    with col1:
        st.header("📂 Upload Document")
        uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
        if uploaded_file:
            st.success("📄 File Uploaded Successfully!")
            st.markdown(f"**Filename:** `{uploaded_file.name}`")
            st.markdown(f"**Size:** `{uploaded_file.size / 1024:.2f} KB`")
            displayPDF(uploaded_file)
            temp_pdf_path = "temp.pdf"
            with open(temp_pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.session_state['temp_pdf_path'] = temp_pdf_path

    # Column 2: Create Embeddings
    with col2:
        st.header("🧠 Generate Embeddings")
        if st.button("🔄 Create Embeddings", key="embed_button"):
            if st.session_state['temp_pdf_path'] is None:
                st.warning("⚠️ Please upload a PDF first.")
            else:
                try:
                    embeddings_manager = EmbeddingsManager(
                        model_name="BAAI/bge-small-en",
                        device="cpu",
                        encode_kwargs={"normalize_embeddings": True},
                        qdrant_url="http://localhost:6333",
                        collection_name="vector_db"
                    )
                    with st.spinner("Generating embeddings..."):
                        result = embeddings_manager.create_embeddings(st.session_state['temp_pdf_path'])
                        time.sleep(1)
                    st.success("✅ Embeddings generated successfully!")
                    st.session_state['chatbot_manager'] = ChatbotManager(
                        model_name="BAAI/bge-small-en",
                        device="cpu",
                        encode_kwargs={"normalize_embeddings": True},
                        llm_model="llama3.2:3b",
                        llm_temperature=0.7,
                        qdrant_url="http://localhost:6333",
                        collection_name="vector_db"
                    )
                except Exception as e:
                    st.error(f"Error: {e}")

    # Column 3: Chatbot Interface
    with col3:
        st.header("💬 Chat with Your Document")
        if st.session_state['chatbot_manager'] is None:
            st.info("Upload a document and generate embeddings to start chatting.")
        else:
            for msg in st.session_state['messages']:
                st.chat_message(msg["role"]).markdown(msg["content"])
            user_input = st.chat_input("Type your message...")
            if user_input:
                st.chat_message("user").markdown(user_input)
                st.session_state['messages'].append({"role": "user", "content": user_input})
                with st.spinner("Generating response..."):
                    try:
                        answer = st.session_state['chatbot_manager'].get_response(user_input)
                        st.chat_message("assistant").markdown(answer)
                        st.session_state['messages'].append({"role": "assistant", "content": answer})
                    except Exception as e:
                        st.error(f"Error: {e}")

# Contact Page
'''elif menu == "📧 Contact":
    st.title("📬 Get in Touch")
    st.markdown("""
    **Have questions or feedback? Reach out!**

    - **Email:** [developer@example.com](mailto:developer@example.com)
    - **GitHub:** [Contribute on GitHub](https://github.com/AIAnytime/Document-Buddy-App)
    - **LinkedIn:** [Follow us](https://linkedin.com)

    Thank you for supporting Document Buddy! 🙌
    """)

# Footer
st.markdown("---")
st.markdown("© 2024 Document Buddy App. All rights reserved. 🌟")'''
