# 🤖 AskBuddy – GenAI QnA Chatbot

🚀 **Live Demo:**
👉 https://chatbot-ggjjyuhnhdb5gkijdvhappw.streamlit.app/

---

## 📌 Project Overview

AskBuddy is an **End-to-End AI-powered Question Answering Chatbot** built using:

* **LangChain** for prompt orchestration
* **Google Gemini (LLM)** for intelligent responses
* **Streamlit** for interactive UI

The chatbot allows users to ask questions in real-time and receive AI-generated answers in a clean chat interface.

---

## 🧠 Features

* 💬 Chat-style UI (like ChatGPT)
* 🔁 Session-based chat history
* ⚡ Fast responses using Gemini Flash model
* 🧩 Clean integration using LangChain
* 🌐 Live deployed using Streamlit Cloud

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Google Generative AI (Gemini)
* python-dotenv

---

## 📂 Project Structure

```
chatbot/
│
├── qna_bot.py          # Main Streamlit chatbot app
├── requirements.txt   # Project dependencies
├── .gitignore         # Ignore env & sensitive files
└── README.md
```

---

## ⚙️ Setup Instructions (Run Locally)

### 1. Clone Repository

```
git clone https://github.com/Harsh7114/chatbot.git
cd chatbot
```

---

### 2. Create Virtual Environment

```
python -m venv env
env\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run the App

```
streamlit run qna_bot.py
```

---

## 💡 How It Works

1. User enters a query in the chat input
2. Query is sent to Gemini via LangChain
3. Model generates response
4. Output is parsed and displayed
5. Chat history is stored using Streamlit session state

---

## ⚠️ Limitations

* ❌ No real-time internet access
* ❌ Cannot answer latest news/events
* (Future upgrade: RAG / Search integration)

---

## 🚀 Future Improvements

* 🔍 Add real-time search (RAG)
* 🧠 Add conversation memory
* 🎨 Improve UI/UX
* ☁️ Deploy on custom domain
* 📄 Chat with PDFs / documents

---

## 📚 Learnings

This project helped in understanding:

* Prompt engineering
* LangChain pipelines
* LLM integration
* Streamlit deployment
* Git & GitHub workflow

---

## 🙌 Acknowledgment

Built as part of learning **Generative AI & LLM-based applications**.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
