from orchestrator import process_feature_request


def main():
    feature = input("Enter a feature request: ")
    result = process_feature_request(feature)

    print("\n=== Design ===")
    print(result["design"])
    print("\n=== Code ===")
    print(result["code"])
    print("\n=== Review ===")
    print(result["review"])
    print("\n=== Tests ===")
    print(result["tests"])


if __name__ == "__main__":
    main()
