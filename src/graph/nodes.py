from typing import List

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


def search_the_web(state: GraphState):
    """
    Node 2 : Searches the web using the refined search query.
    """
    print("---NODE: search_the_web---")
    search_query = state['search_query']

    # Call our search tool
    search_results = get_search_results(search_query)
    print(f"Search Results (snippet): {search_results[:100]}...")

    return{"search_results": search_results}

def extract_lead_data(state: GraphState):
    """
    Node 3 : Extracts structured lead data from the search results.
    """
    print("---NODE: extract_lead_data---")
    search_results = state['search_results']

    # This is key: .with_structured_output(lead)
    # This tells the LLm to format its response *exactly* like out Pydantic 'Lead' class
    # And to return a *list* of them.
    class Leads(BaseModel):
        leads: List[Lead]

    extractor_chain = data_extractor_template | model.with_structured_output(Leads)


