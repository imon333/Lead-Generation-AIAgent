
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from .state import GraphState, Lead
from src.prompts.systemPrompt import prompt_refiner_template, data_extractor_template
from src.tools.search import get_search_results
from src.tools.file_writer import save_leads_to_excel

# Initialize out LLMs
# We'll use gpt-4o for its good reasoning and structured output

model = ChatOpenAI(model = "gpt-4o", temperature=0)

# ___ NODE FUNCTION ___
def refine_search_prompt(state: GraphState):
    """
    Node 1 : Refines the user's prompt into a search query.
    """
    print ("---NODE: refiner_search_prompt---")
    user_prompt = state['user_prompt']

    # Create the chain for this node
    refiner_chain = prompt_refiner_template | model

    # Invoke the chain
    response = refiner_chain.invoke({"user_prompt": user_prompt})

    # The output of an LLM call is a message object, we get the content

    search_query = response.content
    print(f"Refined Search Query: {search_query}")

    return {"search_query": search_query}
