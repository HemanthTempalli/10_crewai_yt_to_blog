# 🧠 YouTube to Blog Writer using CrewAI & Groq

This project uses **CrewAI agents** powered by **Groq's LLaMA 3** to automatically:

1. 🔍 **Search and extract** transcripts from a specific YouTube channel
2. ✍️ **Summarize** and **transform** the content into well-structured blog posts

---

## 🚀 Features

- 🤖 Two specialized agents: `BlogResearcher` and `BlogWriter`
- 🎥 Custom tool to fetch YouTube transcripts without using `crewai-tools`
- ⚡ Uses **Groq's `llama-3.1-8b-instant`** via `langchain-groq`
- 🧩 Modular code using `crew.py`, `agents.py`, and `tools/yt_tool.py`

---

## 🛠️ Tech Stack

- [CrewAI](https://docs.crewai.com/)
- [Groq API](https://console.groq.com/)
- [LangChain](https://www.langchain.com/)
- Python 3.10+
- `youtube-transcript-api` (for transcript extraction)
- `dotenv` for secure API keys

---

## 📁 Project Structure

```bash
yt-to-blog-project/
├── crew.py                # Crew and task runner
├── agents.py              # CrewAI agent definitions
├── tools/
│   └── yt_tool.py         # Custom YouTube transcript tool
├── .env                   # Contains GROQ_API_KEY
├── requirements.txt       # Python dependencies
└── README.md              # You're here!
