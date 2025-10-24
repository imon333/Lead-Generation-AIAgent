from tavily import TavilyClient
import os

# we initialize the client here
# It automatically reads teh TAVILY_API_KEY from the .env file

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def get_search_results(query: str):
    """
    Uses Tavily to search the web for a given query.
    Returns a list of search result snippets.
    
    """
    try:
        results = tavily_client.search(
            query=query,
            search_depth="basic",
            max_results=5
        )
        
        return "\n---\n".join([r['content'] for r in results['results']])
    except Exception as e:
        print(f"Error during Tavily search: {e}")
        return "Search failed to return results"