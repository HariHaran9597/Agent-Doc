import streamlit as st
from streamlit import session_state
import time
import base64
import os
from vectors import EmbeddingsManager
from chatbot import ChatbotManager

# PDF display function
def displayPDF(file):
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Initialize session state
if 'temp_pdf_path' not in st.session_state:
    st.session_state['temp_pdf_path'] = None
if 'chatbot_manager' not in st.session_state:
    st.session_state['chatbot_manager'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "Home"

# Page config
st.set_page_config(
    page_title="Document Buddy",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
        }
        .css-1d391kg {
            padding: 2rem 1rem;
        }
        .stSidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        h1 {
            color: #1E88E5;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        .user-message {
            background-color: #E3F2FD;
        }
        .bot-message {
            background-color: #F5F5F5;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("logo.png", use_column_width=True)
    st.markdown("### 📚 Agent:DOC")
    st.markdown("---")
    
    # Modern navigation
    pages = {
        "Home": "🏠",
        "Chat": "💬",
        "About": "ℹ️"
    }
    
    for page, icon in pages.items():
        if st.sidebar.button(f"{icon} {page}", key=page):
            st.session_state['current_page'] = page

    st.markdown("---")
    st.markdown("### 🛠️ Quick Settings")
    st.markdown("Model: Llama 3.2")
    st.markdown("Embeddings: BGE")

# Main content
if st.session_state['current_page'] == "Home":
    st.markdown("# Welcome to Document Buddy")
    st.markdown("### Your AI-Powered Document Assistant")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Transform how you interact with documents:
        - 📄 **Smart Document Analysis**
        - 💡 **Intelligent Responses**
        - 🔍 **Quick Information Retrieval**
        """)
        
        uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])
        if uploaded_file:
            st.success("✅ Document uploaded successfully!")
            
            # Save file
            temp_pdf_path = "temp.pdf"
            with open(temp_pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.session_state['temp_pdf_path'] = temp_pdf_path
            
            # Process button
            if st.button("🚀 Process Document"):
                with st.spinner("Processing..."):
                    try:
                        embeddings_manager = EmbeddingsManager(
                            model_name="BAAI/bge-small-en",
                            device="cpu",
                            encode_kwargs={"normalize_embeddings": True},
                            qdrant_url="http://localhost:6333",
                            collection_name="vector_db"
                        )
                        result = embeddings_manager.create_embeddings(temp_pdf_path)
                        st.session_state['chatbot_manager'] = ChatbotManager()
                        st.success("✨ Document processed successfully!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

    with col2:
        if uploaded_file:
            st.markdown("### 📑 Document Preview")
            displayPDF(uploaded_file)

elif st.session_state['current_page'] == "Chat":
    st.markdown("# Chat with your Document")
    
    if not st.session_state['chatbot_manager']:
        st.info("👆 Please upload and process a document first")
    else:
        # Chat interface
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state['messages']:
                with st.chat_message(msg['role']):
                    st.markdown(msg['content'])

        # Input
        if prompt := st.chat_input("Ask about your document..."):
            st.session_state['messages'].append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = st.session_state['chatbot_manager'].get_response(prompt)
                    st.markdown(response)
            st.session_state['messages'].append({"role": "assistant", "content": response})

elif st.session_state['current_page'] == "About":
    '''st.markdown("# About Document Buddy")
    st.markdown("""
    ### 🚀 Built with Advanced Technology
    - **LLM**: Llama 3.2
    - **Embeddings**: BGE
    - **Vector Store**: Qdrant
    
    ### 📬 Contact
    - Email: h@gmail.com
    - GitHub: [Document-Buddy-App](https://github.com/AIAnytime/Document-Buddy-App)
    
    ### 🛡️ Privacy & Security
    Your documents are processed locally and securely.
    """)'''

# Minimal footer
st.markdown("---")
st.markdown("Made with ❤️")