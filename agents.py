from crewai import Agent 
from langchain_groq import ChatGroq
from tools import yt_tool
from dotenv import load_dotenv

import os

load_dotenv()

groq_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 🎯 Blog Researcher Agent
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Get the relevant video transcription for the topic {topic} from the provided YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, and Generative AI "
        "and providing key suggestions and summaries."
    ),
    llm=groq_llm,
    tools=[yt_tool],
    allow_delegation=True
)

# ✍️ Blog Writer Agent
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    llm=groq_llm,
    tools=[yt_tool],
    allow_delegation=False
)
