import sys
import os
from pathlib import Path


import dotenv 
dotenv.load_dotenv()

# Now import after path is set
from src.tools.search import get_search_results


def run_tavily_test():
    """Performs a test search and prints the results."""
    
    print("--- Running Tavily Search Test ---")
    
    # You can change the test query
    test_query = "latest news on AI developments"
    
    print(f"Query: {test_query}")
    
    # Call the function from your search.py file
    results = get_search_results(test_query)
    
    print("\nSearch Results (Snippets):")
    print("====================================")
    print(results)
    print("====================================")
    
    # Check for success/failure
    if "Search failed to return results" in results or "Error during Tavily search" in results:
        print("\n❌ TEST FAILED: Check your TAVILY_API_KEY and network connection.")
    else:
        print("\n✅ TEST SUCCESSFUL: Search results were returned.")
        
        
if __name__ == "__main__":
    run_tavily_test()