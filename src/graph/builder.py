from langgraph.graph import StateGraph, END
from .state import GraphState
from .nodes import (refine_search_prompt, search_the_web, extract_lead_data, save_leads_to_file)

def build_graph():
    """
    Builds the LangGraph workflow
    """
    workflow = StateGraph(GraphState)

    # 1. Add the nodes
    # Each node is a function we defined in nodes.py

    workflow.add_node("refiner", refine_search_prompt)
    workflow.add_node("searcher", search_the_web)
    workflow.add_node("extractor", extract_lead_data)
    workflow.add_node("saver", save_leads_to_file)

    # 2. Define the edges
    # This is i simple, linear graph

    workflow.set_entry_point("refiner")
    workflow.add_edge("refiner", "searcher")
    workflow.add_edge("searcher", "extractor")
    workflow.add_edge("extractor", "saver")
    workflow.add_edge("extractor", END) # The graph finishes at the 'saver' node

    # 3. Compile the graph
    print( "Compiling graph ...")
    app = workflow.compile()
    print("Graph compiled successfully.")

    return app