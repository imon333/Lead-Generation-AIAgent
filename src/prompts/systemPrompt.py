from langchain_core.prompts import ChatPromptTemplate

prompt_refinder_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert search query generator. Your goal is to take a user's topic"
        "and craft a concise, effective search query to find leads for that topic."
        "Focus on queries that will find company names, contact, email, social media and websites"),
        ("user", "Generate a search query for the topic: {user_prompt}"),
        ("ai","Search Query:")
    )
])