from langchain_community.llms import Ollama


def run_engineer(design: str, context: str) -> str:
    """Generate code implementation based on design and context."""
    prompt = (
        "You are the software engineer AI. "
        "Implement the following design using the given context.\n"\
        f"Design:\n{design}\n"\
        f"Context:\n{context}\n"\
        "Provide the code snippet or instructions." 
    )
    llm = Ollama(model="mistral")
    return llm.invoke(prompt)
