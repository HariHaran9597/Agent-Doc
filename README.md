Agent Doc: Intelligent Document Assistant 📂🤖
Agent Doc is a cutting-edge, AI-powered document assistant app that helps you efficiently manage and interact with your PDFs. Designed with simplicity and intelligence in mind, Agent Doc allows users to upload, process, and chat with documents like never before. By integrating state-of-the-art embeddings, natural language processing, and vector search technology, Agent Doc offers seamless document management with real-time insights, making your work smarter and faster. 🚀

Key Features 🔑:
📥 Easy PDF Uploads: Upload any PDF document effortlessly and view a live preview of the content.
⚡ Fast Embedding Generation: Instantly create document embeddings to enhance search and retrieval capabilities.
💬 AI Chatbot Interaction: Chat with your document! Ask questions and get context-driven answers based on the content of the uploaded PDFs.
🧠 Intelligent Search: Harness the power of embeddings for efficient, semantic document search and retrieval.
🌍 Modern UI: Enjoy an intuitive, minimalistic interface built for a smooth user experience across devices.
🔒 Local Deployment: Runs entirely on your local machine with technologies like Qdrant and Llama 3.2, ensuring full control over your data.
Tech Stack 🛠️:
LangChain: Powers the backend orchestration, enabling seamless management of document embeddings and interactions.
Qdrant: A scalable vector database, used to store and manage document embeddings for quick retrieval.
BGE Embeddings: A reliable source for creating high-quality semantic embeddings, ensuring accuracy in document processing and search.
LLaMA 3.2: The advanced language model that powers intelligent interactions with documents, delivering precise and context-rich responses.
Streamlit: The framework for building the app's interactive, responsive web interface.
Directory Structure 📁:
Copy code
agent_doc/
│── assets/
│   └── logo.png
├── app.py
├── chatbot.py
├── embeddings.py
├── requirements.txt
Getting Started 🚀:
Follow these easy steps to get Agent Doc running on your machine:

Clone the Repository:

bash
Copy code
git clone https://github.com/xxxxxx/Agent-Doc.git
cd Agent-Doc
Set Up a Virtual Environment:

Using venv:
On Windows: python -m venv venv then venv\Scripts\activate
On macOS/Linux: python3 -m venv venv then source venv/bin/activate
Using Anaconda:
bash
Copy code
conda create --name agent_doc python=3.9
conda activate agent_doc
Install Dependencies: Once in your environment, install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application: Start the Streamlit app:

bash
Copy code
streamlit run app.py
Your application will be available in your web browser at http://localhost:8501.

Contributing 🤝:
We welcome contributions to Agent Doc! If you have ideas for new features or improvements, please feel free to contribute. Here's how:

Fork the Repository to your GitHub account.
Clone Your Fork to your local machine.
Create a New Branch:
bash
Copy code
git checkout -b feature/your-feature-name
Make Changes and Commit them:
bash
Copy code
git commit -m "Describe your changes"
Push the branch back to your fork:
bash
Copy code
git push origin feature/your-feature-name
Create a Pull Request to the main repository.
We appreciate all contributions, big or small!

License 📝:
This project is licensed under the MIT License. See the LICENSE file for more details.

Agent Doc is here to help you work smarter with your documents. Start now and let AI assist you in transforming how you manage and interact with your PDFs! 🌟

Useful Resources 📚:
Streamlit Documentation: Streamlit Docs
LangChain Documentation: LangChain Docs
Qdrant Documentation: Qdrant Docs
LLaMA Documentation: LLaMA Docs
Happy coding! 🎉

