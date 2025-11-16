# 🤖 AI Lead Generation Agent

A lightweight lead-generation agent built using **LangGraph**, **LangChain**, **OpenAI**, and **Tavily** to automate the process of finding and extracting structured business leads.

This project converts a simple user request into a refined search query, performs a real-time web search, extracts lead information, and saves the results directly into an Excel file — all through a clean, four-step pipeline.

---

## How It Works (4-Step Pipeline)

The agent runs on a linear **LangGraph** workflow:

1. **Refine Search Prompt:**  
   The system takes the user’s topic (e.g., "fitness coaches in Toronto") and uses an LLM to generate a focused, high-quality search query.

2. **Search the Web:**  
   The `search.py` tool uses the refined query to retrieve fresh web snippets through Tavily.

3. **Extract Lead Data:**  
   A GPT-4o model extracts structured details, For Exacple: — **Name, Email, Phone, Address, Website, Instagram, Facebook, Description** — using `with_structured_output` and a Pydantic schema.

4. **Save to File:**  
   The extracted leads are saved into an Excel file via `file_writer.py`.

---

## Core Technologies & Structure

| Technology | Purpose | Key Feature |
|-----------|---------|-------------|
| **LangGraph** | Agent workflow | Controls nodes pipeline. |
| **LangChain** | LLM tools & prompts | Powers prompt templates and chain execution. |
| **OpenAI (GPT-4o)** | Refinement & extraction | Ensures accurate structured output. |
| **Tavily** | Web search | Provides relevant search data. |
| **Pydantic** | Lead model | Validates structured lead format. |

### Project Layout

```
main.py                     # Entry point (API checks + user prompt)
src/
 ├── graphs/
 │     ├── builder.py       # Builds the LangGraph workflow
 │     ├── node.py          # Node function definitions
 │     └── state.py         # GraphState + Lead schema
 │
 ├── prompts/
 │     └── systemPrompt.py  # Search refiner & extraction prompts
 │
 └── tools/
       ├── search.py        # Tavily search
       └── file_writer.py   # Excel export
```

---

## How you can easily start with this easily

1. Set your `OPENAI_API_KEY` and `TAVILY_API_KEY` as environment variables.  
2. Install dependencies using `pip install -r requirements.txt`.  
3. Run the project with:

```
python main.py
```

You’ll be prompted to enter the type of leads you want to generate. The system will run the full pipeline and save your structured results automatically.


--- Imon Hosen ---- twitter: @ImonHosen3




