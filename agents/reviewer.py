from langchain_community.llms import Ollama


def run_reviewer(code: str, context: str) -> str:
    """Review the generated code for issues and improvements."""
    prompt = (
        "You are the code reviewer AI. "
        "Review the following code in light of the project context.\n"\
        f"Context:\n{context}\n"\
        f"Code:\n{code}\n"\
        "Provide feedback and suggestions." 
    )
    llm = Ollama(model="mistral")
    return llm.invoke(prompt)
