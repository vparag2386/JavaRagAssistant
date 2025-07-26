from typing import Dict, Tuple

from indexer import index_codebase, load_index
from retriever import retrieve_relevant_chunks
from agents.architect import run_architect
from agents.engineer import run_engineer
from agents.reviewer import run_reviewer
from agents.tester import run_tester
from file_writer import write_code_file


def parse_engineer_output(output: str) -> Tuple[str, str]:
    """Extract file path and code from engineer agent output."""
    file_path = ""
    code_lines = []
    in_code = False
    for line in output.splitlines():
        if line.startswith("FILE:"):
            file_path = line[len("FILE:"):].strip()
        elif line.strip() == "CODE:" or line.startswith("CODE:"):
            in_code = True
            if line.strip() != "CODE:":
                code_lines.append(line.split("CODE:",1)[1])
        elif in_code:
            code_lines.append(line)
    code = "\n".join(code_lines).strip()
    return file_path, code


def process_feature_request(request: str) -> Dict[str, str]:
    """Coordinate agents to process the feature request."""
    index = load_index()
    if not index:
        index = index_codebase()

    retrieved = retrieve_relevant_chunks(request, index)
    context = "\n".join(chunk["text"] for chunk in retrieved)

    design = run_architect(request, context)
    engineer_output = run_engineer(design, context)
    file_path, code = parse_engineer_output(engineer_output)
    if file_path:
        write_code_file(file_path, code)

    review = run_reviewer(code, context)
    tests = run_tester(code, context)

    return {
        "design": design,
        "code": engineer_output,
        "review": review,
        "tests": tests,
    }
