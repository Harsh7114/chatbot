# End-To-End LLM QnA Chatbot

### Built with LangChain, Google Gemini & Streamlit (Gen-AI Project)

---

## 🚀 Project Overview

This project is an **End-to-End Question Answering Chatbot** built using modern Generative AI tools.
It leverages **LangChain**, **Google Gemini (LLM)**, and **Streamlit** to create an interactive and dynamic chatbot application.

The chatbot can answer user queries intelligently using prompt engineering and LLM capabilities.

---

## 🧠 Features

* Dynamic prompt generation using LangChain
* Integration with Google Gemini model
* Clean and interactive UI using Streamlit
* Structured output parsing for clean responses
* Scalable architecture for future upgrades (RAG, memory, etc.)

---

## 🛠️ Tech Stack

* Python
* LangChain
* Google Generative AI (Gemini)
* Streamlit
* dotenv (for environment variables)

---

## 📂 Project Structure

```
GENAI/
│
├── apps/
│   ├── qna_bot.py          # Main chatbot logic
│   ├── app.py              # Streamlit UI
│
├── env/                    # Virtual environment
├── .env                    # API keys
├── requirements.txt        # Dependencies
└── README.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/chatbot.git
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

### 5. Run the Application

#### Run backend (optional)

```
python qna_bot.py
```

#### Run Streamlit UI

```
streamlit run app.py
```

---

## 💡 How It Works

1. User inputs a query
2. LangChain creates a dynamic prompt
3. Gemini processes the prompt
4. Output parser formats response
5. Streamlit displays the result

---

## 🔥 Future Improvements

* Add conversation memory
* Implement RAG (Retrieval-Augmented Generation)
* Deploy on cloud (AWS / GCP / Vercel)
* Add chat history UI
* Improve prompt engineering

---

## 🧪 Example Use Cases

* General Q&A assistant
* Study helper chatbot
* Interview preparation tool
* Knowledge assistant

---

## 📌 Learnings

This project demonstrates:

* Prompt engineering
* LLM integration
* LangChain pipelines
* Real-world GenAI application building

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and improve the project.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgment

Built as part of learning **Generative AI and LLM applications**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
