import os


def write_code_file(target_path: str, code: str, dry_run: bool = False) -> None:
    """Write or append code to a .java file under the codebase directory.

    Parameters
    ----------
    target_path: str
        Relative path to the .java file within the project (without the
        leading 'codebase/').
    code: str
        The Java code to write or append.
    dry_run: bool, optional
        If True, only print the intended actions without modifying files.
    """
    # Ensure path is relative and join with base codebase directory
    target_path = target_path.lstrip("/\\")
    base_dir = "codebase"
    full_path = os.path.join(base_dir, target_path)
    dir_name = os.path.dirname(full_path)

    if dry_run:
        action = "create" if not os.path.exists(full_path) else "update"
        print(f"[DRY RUN] Would {action} file: {full_path}")
        return

    os.makedirs(dir_name, exist_ok=True)
    exists = os.path.exists(full_path)

    with open(full_path, "a" if exists else "w", encoding="utf-8") as f:
        f.write(code.rstrip("\n") + "\n")

    status = "Updated" if exists else "Created"
    print(f"\u2705 {status} file: {full_path}")
