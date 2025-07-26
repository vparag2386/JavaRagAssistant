from typing import Dict

from indexer import index_codebase, load_index
from retriever import retrieve_relevant_chunks
from agents.architect import run_architect
from agents.engineer import run_engineer
from agents.reviewer import run_reviewer
from agents.tester import run_tester


def process_feature_request(request: str) -> Dict[str, str]:
    """Coordinate agents to process the feature request."""
    index = load_index()
    if not index:
        index = index_codebase()

    retrieved = retrieve_relevant_chunks(request, index)
    context = "\n".join(chunk["text"] for chunk in retrieved)

    design = run_architect(request, context)
    code = run_engineer(design, context)
    review = run_reviewer(code, context)
    tests = run_tester(code, context)

    return {
        "design": design,
        "code": code,
        "review": review,
        "tests": tests,
    }
