# 🤖 ThinkOn Learning AI Chatbot

**ThinkOn Learning AI** is an interactive, intelligent chatbot designed to enhance the learning experience for students and educators. Built using **Streamlit** for the frontend and **Langchain** with **Ollama** for LLM integration, the chatbot simulates a personalized tutor capable of answering queries, explaining concepts, and offering educational guidance across subjects.

---

## 🎯 Objective

To build a lightweight, LLM-powered educational chatbot that:
- Assists students in understanding concepts
- Answers queries in real time
- Enhances learning through natural conversation

---

## 🌟 Features

- 💬 Chatbot powered by **Langchain** and **Ollama LLMs**
- ⚡ Fast and responsive conversational interface
- 📘 Tailored for education and conceptual learning
- 🧠 Smart response generation based on user input
- 🖼️ Optionally handles image-based input (via PIL)

---

## 🧪 Technologies Used

| Technology              | Purpose                                     |
|--------------------------|---------------------------------------------|
| **Streamlit**            | Web interface for the chatbot               |
| **Langchain**            | Framework for integrating LLM logic         |
| **Ollama**               | Local/hosted Large Language Model backend   |
| **PIL (Pillow)**         | Image handling (optional feature)           |
| **Python**               | Core programming language                   |


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/thinkon-learning-ai.git
cd thinkon-learning-ai
```
--
## 🧠 How It Works
The app initializes a Langchain-based chatbot connected to Ollama LLM.

User input is passed to the model through Langchain's interface.

The model generates an educational or contextual response.

Responses are streamed back in real time using Streamlit's st.chat_message() or st.write().
--
## 🧾 Example Use Cases
"Explain the concept of gravity to a 10-year-old."

"What is the difference between mitosis and meiosis?"

"Summarize the Industrial Revolution in 100 words."

"Help me prepare for my Python interview."
--
## 🔮 Future Enhancements
🔒 Add user authentication

📚 Add memory/context tracking for continuous learning

🌐 Enable multilingual support

✏️ Add note-taking or summarization features

📱 Make it mobile-friendly
