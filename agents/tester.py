from langchain_community.llms import Ollama


def run_tester(code: str, context: str) -> str:
    """Suggest tests for the generated code."""
    prompt = (
        "You are the QA engineer AI. "
        "Write tests for the following code using the context.\n"\
        f"Context:\n{context}\n"\
        f"Code:\n{code}\n"\
        "Provide test cases or testing strategy." 
    )
    llm = Ollama(model="mistral")
    return llm.invoke(prompt)
