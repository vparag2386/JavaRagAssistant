from langchain_community.llms import Ollama


def run_architect(feature_request: str, context: str) -> str:
    """Generate a design overview for the requested feature."""
    prompt = (
        "You are the software architect AI. "
        "Use the following context from the codebase to propose a design.\n"\
        f"Context:\n{context}\n"\
        f"Feature request: {feature_request}\n"\
        "Provide a high level design to implement this feature." 
    )
    llm = Ollama(model="mistral")
    return llm.invoke(prompt)
