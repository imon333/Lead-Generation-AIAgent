import sys
import os
from pathlib import Path

import dotenv
dotenv.load_dotenv()

from src.graph.builder import build_graph
        
def main():
    """
    Main function to run the lead generation graph
    """

    # Check if API keys are set
    if not os.environ.get("OPENAI_API_KEY") or not os.environ.get("TAVILY_API_KEY"):
        print("Error: API keys for OPENAI_API_KEY and TAVILY_API_KEY")
        print("must be set in a .env file")

    # Build the compiled graph
    app = build_graph()

    # Get user input
    user_prompt = input("What industry or topic do you want leads for? \n> ")

    if not user_prompt:
        print("No input provided. oput somethings :))...")
        return

    # This is the input to the *first node*
    # It must match the structure of our GraphSate

    initial_input = {"user_prompt": user_prompt}

    print("\n--- Running Graph ---")

    # Run the graph
    # We use .stream() to see the output of each node as it runs

    for event in app.stream(initial_input):
        # app.stream() a dictionary where the key is the node name
        # and the value is the *output* of that node
        node_name, node_output = list(event.items())[0]
        print(f"Finished Node: {node_name}")

        #You can uncomment the line below to see the full state patch
        # print(f"Output: {node_output}\n")
    print("--- Graph Finished ---")

if __name__ == "__main__":
    main()

