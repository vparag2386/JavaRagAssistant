from langchain_community.llms import Ollama


def run_engineer(design: str, context: str) -> str:
    """Generate code implementation along with target file path."""
    prompt = (
        "You are the software engineer AI. "
        "Implement the following design using the given context.\n"
        f"Design:\n{design}\n"
        f"Context:\n{context}\n"
        "Respond ONLY in the following format:\n"
        "FILE: <path/to/File.java>\n"
        "CODE:\n<your code here>"
    )
    llm = Ollama(model="mistral")
    return llm.invoke(prompt)
