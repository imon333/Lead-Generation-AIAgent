from typing import TypedDict, List, Optional
# This defines the structure of a single lead
# We use Pydantic for strong type-checking, which OpenAI's
# structured output tools can use directly

from pydantic import BaseModel, Field

class Lead(BaseModel):
    name: Optional[str] = Field(description="The name of the company or person or business")
    email: Optional[str] = Field(description="The contact email address of the company or person ")
    phone: Optional[str] = Field(description="The contact phone number of the company or person ")
    address: Optional[str] = Field(description="The address of the company or person ")
    website: Optional[str] = Field(description="The website of the company or person ")
    facebook: Optional[str] = Field(description="Facebook profile URL")
    instagram: Optional[str] = Field(description="Instagram profile URL")
    description: Optional[str] = Field(description="A brief description or context")


# This is the main state for our graph
# It's a dictionary that will be passed and updated by each node.

class GraphState(TypedDict):
    user_prompt: str            # The initial input from the user
    search_query: str           # The refined query generation by the LLM
    search_results: str         # The raw text snippets from the web search
    extracted_leads: List[Lead] # The list of structured leads
    final_filepath: str         # The path to the saved Excel file

