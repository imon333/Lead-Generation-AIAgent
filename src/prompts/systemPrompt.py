from langchain_core.prompts import ChatPromptTemplate

prompt_refiner_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert search query generator. Your goal is to take a user's topic"
        "and craft a concise, effective search query to find leads for that topic."
        "Focus on queries that will find company names, contact, email, social media and websites"),
        ("user", "Generate a search query for the topic: {user_prompt}"),
        ("ai","Search Query:")
    
])

# Prompt for the data extraction node
# This prompt is crucial. It tell the LLm *what* to find and *how* to format it.

data_extractor_template = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert data extractor. You will be given a block of text from a "
     "web search. Your task is to extract the following lead information:"
     "Name, Email, Phone, Address, Website, Instagram, facebook and a brief description/context. "
     "you must follow the structure output format."),
    ("user", "Extract lead information from the following text:\n\n{search_results}")
])